import time
from queue import Queue

import zenoh

from zenoh_ros_type import (
    UUID,
    ActionResultRequest,
    ActionSendGoalResponse,
    Attachment,
    FibonacciFeedback,
    FibonacciResult,
    FibonacciSendGoal,
    GoalInfo,
    GoalStatus,
    GoalStatusArray,
    Time,
)


def main(conf: zenoh.Config, use_bridge_ros2dds: bool = True):
    action = 'fibonacci'
    if use_bridge_ros2dds:
        send_goal_expr = action + '/_action/send_goal'
        cancel_goal_expr = action + '/_action/cancel_goal'
        get_result_expr = action + '/_action/get_result'
        feedback_expr = action + '/_action/feedback'
        status_expr = action + '/_action/status'
    else:
        send_goal_expr = f'*/{action}/_action/send_goal/**'
        cancel_goal_expr = f'*/{action}/_action/cancel_goal/**'
        get_result_expr = f'*/{action}/_action/get_result/**'
        feedback_expr = f'*/{action}/_action/feedback/**'
        status_expr = f'*/{action}/_action/status/**'

    # rmw_zenoh attachment
    attachment = None if use_bridge_ros2dds else Attachment()

    # Queue for handling goals
    goals = Queue()

    with zenoh.open(conf) as session:
        # Declare liveliness tokens for rmw_zenoh discovery
        # Format: @ros2_lv/<domain>/<zid>/<nid>/<entity_id>/SS/<ns>/<enclave>/<node>/<service>/<type>/<hash>/<qos>
        # https://github.com/ros2/rmw_zenoh/blob/rolling/docs/design.md#graph-cache
        if not use_bridge_ros2dds:
            zid = str(session.zid())
            node = 'action_server'
            qos = '::,10:,:,:,,'

            _tokens = [
                session.liveliness().declare_token(
                    f'@ros2_lv/0/{zid}/0/0/SS/%/%/{node}/%{action}%_action%send_goal/action_tutorials_interfaces::action::dds_::Fibonacci_SendGoal_/TypeHashNotSupported/{qos}'
                ),
                session.liveliness().declare_token(
                    f'@ros2_lv/0/{zid}/0/0/SS/%/%/{node}/%{action}%_action%cancel_goal/action_msgs::srv::dds_::CancelGoal_/TypeHashNotSupported/{qos}'
                ),
                session.liveliness().declare_token(
                    f'@ros2_lv/0/{zid}/0/0/SS/%/%/{node}/%{action}%_action%get_result/action_tutorials_interfaces::action::dds_::Fibonacci_GetResult_/TypeHashNotSupported/{qos}'
                ),
                session.liveliness().declare_token(
                    f'@ros2_lv/0/{zid}/0/0/MP/%/%/{node}/%{action}%_action%feedback/action_tutorials_interfaces::action::dds_::Fibonacci_FeedbackMessage_/TypeHashNotSupported/{qos}'
                ),
                session.liveliness().declare_token(
                    f'@ros2_lv/0/{zid}/0/0/MP/%/%/{node}/%{action}%_action%status/action_msgs::msg::dds_::GoalStatusArray_/TypeHashNotSupported/{qos}'
                ),
            ]

        feedback_publisher = session.declare_publisher(feedback_expr)
        status_publisher = session.declare_publisher(status_expr)

        # Dictionaries mapping goal_id to GoalStatus, results, and queries waiting for results
        status_dict = {}
        result_dict = {}
        pending_queries = {}

        # Update the status of a goal and publish the updated status list
        def update_status(goal_id, new_status):
            now = time.time()
            timestamp = Time(sec=int(now), nanosec=int((now % 1) * 1e9))

            # Update existing status or create a new one
            if goal_id in status_dict:
                status = status_dict[goal_id]
                status.status = new_status
                status.goal_info.stamp = timestamp
                print(f'Update status {goal_id.hex()}: {new_status}')
            else:
                status = GoalStatus(
                    goal_info=GoalInfo(goal_id=UUID(uuid=goal_id), stamp=timestamp),
                    status=new_status,
                )
                status_dict[goal_id] = status
                print(f'New status {goal_id.hex()}: {new_status}')

            # Publish the updated status list
            status_publisher.put(
                GoalStatusArray(status_list=list(status_dict.values())).serialize(),
                attachment=None if use_bridge_ros2dds else attachment.serialize(),
            )

            # Check and reply to any pending result queries if the goal is completed
            if new_status == GoalStatus.STATUS.STATUS_SUCCEEDED.value:
                if goal_id in pending_queries:
                    query, query_attachment = pending_queries.pop(goal_id)
                    result = FibonacciResult(
                        status=new_status,
                        sequence=result_dict[goal_id],
                    )
                    print(f'Send result {goal_id.hex()}: {result.sequence}')
                    query.reply(
                        get_result_expr,
                        result.serialize(),
                        attachment=None if use_bridge_ros2dds else query_attachment.serialize(),
                    )

        # Callback to handle a new goal request
        def send_goal_callback(query):
            send_goal = FibonacciSendGoal.deserialize(query.payload.to_bytes())
            print(f'Receive goal {send_goal.goal_id.uuid.hex()}: {send_goal.goal}')

            # rmw_zenoh attachment
            query_attachment = None if use_bridge_ros2dds else Attachment.deserialize(query.attachment.to_bytes())

            # Mark the goal as accepted
            update_status(send_goal.goal_id.uuid, GoalStatus.STATUS.STATUS_ACCEPTED.value)

            # Reply to the client that the goal was accepted
            now = time.time()
            send_goal_response = ActionSendGoalResponse(
                accept=True,
                timestamp=Time(sec=int(now), nanosec=int((now % 1) * 1e9)),
            )
            query.reply(
                send_goal_expr,
                send_goal_response.serialize(),
                attachment=None if use_bridge_ros2dds else query_attachment.serialize(),
            )

            # Add the goal to the queue
            goals.put(send_goal)

        # Callback to handle a request for the result of a goal
        def get_result_callback(query):
            result_request = ActionResultRequest.deserialize(query.payload.to_bytes())
            goal_id = result_request.goal_id.uuid
            print(f'Receive result request: {goal_id.hex()}')

            # rmw_zenoh attachment
            query_attachment = None if use_bridge_ros2dds else Attachment.deserialize(query.attachment.to_bytes())

            goal_status = status_dict.get(goal_id, None)
            if goal_status and goal_status.status == GoalStatus.STATUS.STATUS_SUCCEEDED.value:
                # If the goal is completed, send the result immediately
                result = FibonacciResult(
                    status=goal_status.status,
                    sequence=result_dict[goal_id],
                )

                print(f'Send result {goal_id.hex()}: {result.sequence}')
                query.reply(
                    get_result_expr,
                    result.serialize(),
                    attachment=None if use_bridge_ros2dds else query_attachment.serialize(),
                )
            else:
                # Otherwise, store the query and attachment to reply later when the goal is completed
                pending_queries[goal_id] = (query, query_attachment)

        # TODO: Callback to handle a cancel goal request
        def cancel_goal_callback(query):
            print(query)

        session.declare_queryable(send_goal_expr, send_goal_callback, complete=True)
        session.declare_queryable(get_result_expr, get_result_callback, complete=True)
        session.declare_queryable(cancel_goal_expr, cancel_goal_callback, complete=True)

        try:
            while True:
                # Process the next goal in the queue
                send_goal = goals.get()
                goad_id = send_goal.goal_id.uuid
                goal = send_goal.goal

                # Mark the goal as executing
                update_status(goad_id, GoalStatus.STATUS.STATUS_EXECUTING.value)

                # Compute the Fibonacci sequence
                sequence = [0, 1]
                for i in range(1, goal + 1):
                    if len(sequence) < 2:
                        sequence.append(1)
                    else:
                        sequence.append(sequence[-1] + sequence[-2])

                    # Publish feedback after each computation
                    print(f'Publish feedback {goad_id.hex()}: {sequence}')
                    feedback = FibonacciFeedback(
                        goal_id=UUID(uuid=goad_id),
                        partial_sequence=sequence[:],
                    )
                    feedback_publisher.put(
                        feedback.serialize(),
                        attachment=None if use_bridge_ros2dds else attachment.serialize(),
                    )
                    result_dict[goad_id] = sequence[:]
                    time.sleep(1)

                # Mark the goal as completed
                update_status(goad_id, GoalStatus.STATUS.STATUS_SUCCEEDED.value)

        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    import argparse

    from zenoh_ros_type.examples.common import add_config_arguments, get_config_from_args

    parser = argparse.ArgumentParser(prog='action_server', description='zenoh action server example')
    add_config_arguments(parser)

    args = parser.parse_args()
    conf = get_config_from_args(args)

    main(conf, use_bridge_ros2dds=not args.use_rmw_zenoh)

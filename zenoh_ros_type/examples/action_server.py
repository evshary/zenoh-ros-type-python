import time
from queue import Queue

import zenoh

from zenoh_ros_type import (
    UUID,
    ActionResultRequest,
    ActionSendGoalResponse,
    FibonacciFeedback,
    FibonacciResult,
    FibonacciSendGoal,
    GoalInfo,
    GoalStatus,
    GoalStatusArray,
    Time,
)


def main(conf: zenoh.Config):
    key_expr = 'fibonacci'
    send_goal_expr = key_expr + '/_action/send_goal'
    cancel_goal_expr = key_expr + '/_action/cancel_goal'
    get_result_expr = key_expr + '/_action/get_result'
    feedback_expr = key_expr + '/_action/feedback'
    status_expr = key_expr + '/_action/status'

    # Queue for handling goals
    goals = Queue()

    with zenoh.open(conf) as session:
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
            status_publisher.put(GoalStatusArray(status_list=list(status_dict.values())).serialize())

            # Check and reply to any pending result queries if the goal is completed
            if new_status == GoalStatus.STATUS.STATUS_SUCCEEDED.value:
                if goal_id in pending_queries:
                    query = pending_queries.pop(goal_id)
                    result = FibonacciResult(
                        status=new_status,
                        sequence=result_dict[goal_id],
                    )
                    print(f'Send result {goal_id.hex()}: {result.sequence}')
                    query.reply(get_result_expr, result.serialize())

        # Callback to handle a new goal request
        def send_goal_callback(query):
            send_goal = FibonacciSendGoal.deserialize(query.payload.to_bytes())
            print(f'Receive goal {send_goal.goal_id.uuid.hex()}: {send_goal.goal}')

            # Mark the goal as accepted
            update_status(send_goal.goal_id.uuid, GoalStatus.STATUS.STATUS_ACCEPTED.value)

            # Reply to the client that the goal was accepted
            now = time.time()
            send_goal_response = ActionSendGoalResponse(
                accept=True,
                timestamp=Time(sec=int(now), nanosec=int((now % 1) * 1e9)),
            )
            query.reply(send_goal_expr, send_goal_response.serialize())

            # Add the goal to the queue
            goals.put(send_goal)

        # Callback to handle a request for the result of a goal
        def get_result_callback(query):
            result_request = ActionResultRequest.deserialize(query.payload.to_bytes())
            goal_id = result_request.goal_id.uuid
            print(f'Receive result request: {goal_id.hex()}')

            goal_status = status_dict.get(goal_id, None)
            if goal_status and goal_status.status == GoalStatus.STATUS.STATUS_SUCCEEDED.value:
                # If the goal is completed, send the result immediately
                result = FibonacciResult(
                    status=goal_status.status,
                    sequence=result_dict[goal_id],
                )

                print(f'Send result {goal_id.hex()}: {result.sequence}')
                query.reply(get_result_expr, result.serialize())
            else:
                # Otherwise, store the query to reply later when the goal is completed
                pending_queries[goal_id] = query

        # TODO: Callback to handle a cancel goal request
        def cancel_goal_callback(query):
            print(query)

        session.declare_queryable(send_goal_expr, send_goal_callback)
        session.declare_queryable(get_result_expr, get_result_callback)
        session.declare_queryable(cancel_goal_expr, cancel_goal_callback)

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
                    feedback_publisher.put(feedback.serialize())
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

    main(conf)

import time
from uuid import uuid4

import zenoh

from zenoh_ros_type import (
    UUID,
    # CancelGoalRequest,
    # CancelGoalResponse,
    # GoalInfo,
    # Time,
    ActionResultRequest,
    ActionSendGoalResponse,
    FibonacciFeedback,
    FibonacciResult,
    FibonacciSendGoal,
    GoalStatusArray,
)


def main(conf: zenoh.Config):
    key_expr = 'fibonacci'
    send_goal_expr = key_expr + '/_action/send_goal'
    # cancel_goal_expr = key_expr + "/_action/cancel_goal"
    get_result_expr = key_expr + '/_action/get_result'
    feedback_expr = key_expr + '/_action/feedback'
    status_expr = key_expr + '/_action/status'

    with zenoh.open(conf) as session:
        send_goal_client = session.declare_querier(send_goal_expr)
        get_result_client = session.declare_querier(get_result_expr)
        # cancel_goal_client = session.declare_querier(cancel_goal_expr)

        def feedback_callback(sample):
            feedback = FibonacciFeedback.deserialize(sample.payload.to_bytes())
            goal_id = feedback.goal_id.uuid.hex()
            print(f'The feedback of {goal_id}: {feedback.partial_sequence}')

        def status_callback(sample):
            status_array = GoalStatusArray.deserialize(sample.payload.to_bytes())
            for goal_status in status_array.status_list:
                goal_id = goal_status.goal_info.goal_id.uuid.hex()
                status_value = goal_status.status
                print(f'The status of {goal_id}: {status_value}')

        session.declare_subscriber(feedback_expr, feedback_callback)
        session.declare_subscriber(status_expr, status_callback)

        time.sleep(1)

        # Send goal request
        goal_id = uuid4().bytes  # Generate a random UUID
        req = FibonacciSendGoal(goal_id=UUID(uuid=goal_id), goal=10)
        try:
            recv_handler = send_goal_client.get(payload=req.serialize())
            reply_sample = recv_handler.recv()
            reply = ActionSendGoalResponse.deserialize(reply_sample.ok.payload.to_bytes())
            print(f'The result of SendGoal: {reply.accept}')
        except Exception as e:
            print(f'Error occurred: {e}')

        # # Cancel goal client
        # req = CancelGoalRequest(goal_info=GoalInfo(goal_id=UUID(uuid=goal_id), stamp=Time(sec=0, nanosec=0)))
        # try:
        #     recv_handler = cancel_goal_client.get(payload=req.serialize())
        #     reply_sample = recv_handler.recv()
        #     reply = CancelGoalResponse.deserialize(reply_sample.ok.payload.to_bytes())
        #     for goal in reply.goals_canceling:
        #         print(f'Cancel {goal.goal_id.uuid.hex()}: {reply.return_code}')
        # except Exception as e:
        #     print(f'Error occurred: {e}')

        # Wait for the result
        time.sleep(10)

        # Get result client
        req = ActionResultRequest(goal_id=UUID(uuid=goal_id))
        recv_handler = get_result_client.get(payload=req.serialize())
        try:
            reply_sample = recv_handler.recv()
            reply = FibonacciResult.deserialize(reply_sample.ok.payload.to_bytes())
            print(f'The result: {reply.status} {reply.sequence}')
        except Exception as e:
            print(f'Error occurred: {e}')


if __name__ == '__main__':
    import argparse

    from zenoh_ros_type.examples.common import add_config_arguments, get_config_from_args

    parser = argparse.ArgumentParser(prog='action_client', description='zenoh action client example')
    add_config_arguments(parser)

    args = parser.parse_args()
    conf = get_config_from_args(args)

    main(conf)

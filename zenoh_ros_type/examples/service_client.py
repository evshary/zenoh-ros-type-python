import os
import time

import zenoh

from zenoh_ros_type import AddTwoIntsReply, AddTwoIntsRequest, Attachment


def main(conf: zenoh.Config, use_bridge_ros2dds: bool = True):
    a = 1
    b = 2
    service = 'add_two_ints'
    key = service if use_bridge_ros2dds else f'*/{service}/**'

    # For rmw_zenoh attachment
    publisher_seq = 0
    attachment = Attachment(
        sequence_number=0,
        timestamp_ns=0,
        gid_length=16,
        gid=list(os.urandom(16)),
    )

    def get_attachment():
        nonlocal publisher_seq
        if use_bridge_ros2dds:
            return None
        publisher_seq += 1
        attachment.sequence_number = publisher_seq
        attachment.timestamp_ns = int(time.time() * 1e9)
        return attachment.serialize()

    with zenoh.open(conf) as session:
        client = session.declare_querier(key)

        print(f'Send AddTwoIntsRequest: a={a}, b={b}')
        req = AddTwoIntsRequest(a=a, b=b)

        try:
            recv_handler = client.get(payload=req.serialize(), attachment=get_attachment())
            reply_sample = recv_handler.recv()

            reply = AddTwoIntsReply.deserialize(reply_sample.ok.payload.to_bytes())
            print(f'Get result: sum={reply.sum}')
        except Exception as e:
            print(f'Error occurred: {e}')


if __name__ == '__main__':
    import argparse

    from zenoh_ros_type.examples.common import add_config_arguments, get_config_from_args

    parser = argparse.ArgumentParser(prog='service_client', description='zenoh service client example')
    add_config_arguments(parser)

    args = parser.parse_args()
    conf = get_config_from_args(args)

    main(conf, use_bridge_ros2dds=not args.use_rmw_zenoh)

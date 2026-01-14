import time

import zenoh

from zenoh_ros_type import AddTwoIntsReply, AddTwoIntsRequest


def main(conf: zenoh.Config):
    key = 'add_two_ints'

    with zenoh.open(conf) as session:

        def callback(query):
            request = AddTwoIntsRequest.deserialize(query.payload.to_bytes())
            print(f'Receive a={request.a}, b={request.b}')

            response = AddTwoIntsReply(sum=request.a + request.b)
            print(f'Send back {response.sum}')
            query.reply(key, response.serialize())

        session.declare_queryable(key, callback)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    import argparse

    import common

    parser = argparse.ArgumentParser(prog='service_server', description='zenoh service server example')
    common.add_config_arguments(parser)

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf)

import time

import zenoh

from zenoh_ros_type import String


def main(conf: zenoh.Config):
    key = 'chatter'

    with zenoh.open(conf) as session:
        publisher = session.declare_publisher(key)

        cnt = 0
        try:
            while True:
                data = f'Hello World {cnt}!'
                print(f'Publish: {data}')
                msg = String(data=data)
                publisher.put(msg.serialize())

                time.sleep(1)
                cnt += 1
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    import argparse

    import common

    parser = argparse.ArgumentParser(prog='talker', description='zenoh talker example')
    common.add_config_arguments(parser)

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf)

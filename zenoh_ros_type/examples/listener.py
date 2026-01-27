import time

import zenoh

from zenoh_ros_type import String


def main(conf: zenoh.Config, use_bridge_ros2dds: bool = True):
    topic = 'chatter'
    key = topic if use_bridge_ros2dds else f'*/{topic}/**'

    with zenoh.open(conf) as session:

        def callback(sample):
            print(f'Receive: {String.deserialize(sample.payload.to_bytes()).data}')

        session.declare_subscriber(key, callback)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    import argparse

    from zenoh_ros_type.examples.common import add_config_arguments, get_config_from_args

    parser = argparse.ArgumentParser(prog='listener', description='zenoh listener example')
    add_config_arguments(parser)

    args = parser.parse_args()
    conf = get_config_from_args(args)

    main(conf, use_bridge_ros2dds=not args.use_rmw_zenoh)

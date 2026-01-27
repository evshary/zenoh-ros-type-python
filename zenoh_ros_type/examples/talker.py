import time

import zenoh

from zenoh_ros_type import Attachment, String


def main(conf: zenoh.Config, use_bridge_ros2dds: bool = True):
    topic = 'chatter'
    key = topic if use_bridge_ros2dds else f'*/{topic}/**'

    # rmw_zenoh attachment
    attachment = None if use_bridge_ros2dds else Attachment()

    with zenoh.open(conf) as session:
        publisher = session.declare_publisher(key)

        cnt = 0
        try:
            while True:
                data = f'Hello World {cnt}!'
                print(f'Publish: {data}')
                msg = String(data=data)
                publisher.put(
                    msg.serialize(),
                    attachment=None if use_bridge_ros2dds else attachment.serialize(),
                )

                time.sleep(1)
                cnt += 1
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    import argparse

    from zenoh_ros_type.examples.common import add_config_arguments, get_config_from_args

    parser = argparse.ArgumentParser(prog='talker', description='zenoh talker example')
    add_config_arguments(parser)

    args = parser.parse_args()
    conf = get_config_from_args(args)

    main(conf, use_bridge_ros2dds=not args.use_rmw_zenoh)

import time

import zenoh

from zenoh_ros_type import String


def main():
    key = 'chatter'

    conf = zenoh.Config()
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
    main()

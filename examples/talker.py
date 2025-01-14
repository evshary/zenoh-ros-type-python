import time
import zenoh
from zenoh_ros_type import String


def main():
    key = "chatter"

    conf = zenoh.Config()
    with zenoh.open(conf) as session:
        publisher = session.declare_publisher(key)

        cnt = 0
        try:
            while True:
                data = f"Hello World {cnt}!"
                print(f"Publish: {data}")
                msg = String(data=data)
                publisher.put(msg.serialize())

                time.sleep(1)
                cnt += 1
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()

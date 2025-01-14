import time

import zenoh

from zenoh_ros_type import AddTwoIntsReply, AddTwoIntsRequest


def main():
    key = 'add_two_ints'

    conf = zenoh.Config()
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
    main()

import zenoh
from zenoh_ros_type import AddTwoIntsRequest, AddTwoIntsReply


def main():
    a = 1
    b = 2
    key = "add_two_ints"

    conf = zenoh.Config()
    with zenoh.open(conf) as session:
        client = session.declare_querier(key)

        print(f"Send AddTwoIntsRequest: a={a}, b={b}")
        req = AddTwoIntsRequest(a=a, b=b)

        try:
            recv_handler = client.get(payload=req.serialize())
            reply_sample = recv_handler.recv()

            reply = AddTwoIntsReply.deserialize(reply_sample.ok.payload.to_bytes())
            print(f"Get result: sum={reply.sum}")
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()

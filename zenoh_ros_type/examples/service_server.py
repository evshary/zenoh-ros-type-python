import time

import zenoh

from zenoh_ros_type import AddTwoIntsReply, AddTwoIntsRequest, Attachment


def main(conf: zenoh.Config, use_bridge_ros2dds: bool = True):
    service = 'add_two_ints'
    key = service if use_bridge_ros2dds else f'*/{service}/**'

    with zenoh.open(conf) as session:
        # Declare liveliness token for rmw_zenoh discovery
        # Format: @ros2_lv/<domain>/<zid>/<nid>/<entity_id>/SS/<ns>/<enclave>/<node>/<service>/<type>/<hash>/<qos>
        # https://github.com/ros2/rmw_zenoh/blob/rolling/docs/design.md#graph-cache
        if not use_bridge_ros2dds:
            _token = session.liveliness().declare_token(
                f'@ros2_lv/0/{str(session.zid())}/0/0/SS/%/%/service_server/%{service}/example_interfaces::srv::dds_::AddTwoInts_/TypeHashNotSupported/::,10:,:,:,,'
            )

        def callback(query):
            request = AddTwoIntsRequest.deserialize(query.payload.to_bytes())
            print(f'Receive a={request.a}, b={request.b}')

            # rmw_zenoh attachment
            # Deserialize attachment, re-serialize to update timestamp
            attachment = None if use_bridge_ros2dds else Attachment.deserialize(query.attachment.to_bytes())

            response = AddTwoIntsReply(sum=request.a + request.b)
            print(f'Send back {response.sum}')
            query.reply(
                key,
                response.serialize(),
                attachment=None if use_bridge_ros2dds else attachment.serialize(increase=False),
            )

        session.declare_queryable(key, callback, complete=True)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    import argparse

    from zenoh_ros_type.examples.common import add_config_arguments, get_config_from_args

    parser = argparse.ArgumentParser(prog='service_server', description='zenoh service server example')
    add_config_arguments(parser)

    args = parser.parse_args()
    conf = get_config_from_args(args)

    main(conf, use_bridge_ros2dds=not args.use_rmw_zenoh)

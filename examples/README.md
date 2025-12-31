# Examples

Here are some basic usages for the library.
The examples code are in [zenoh_ros_type/examples](zenoh_ros_type/examples).

Setup the environment before running the examples.

```bash
uv sync --extra dev
```

## Talker

```bash
# Run bridge
zenoh-bridge-ros2dds
# Zenoh
uv run python3 -m zenoh_ros_type.examples.talker
# ROS
ros2 run demo_nodes_cpp listener
```

## Listener

```bash
# Run bridge
zenoh-bridge-ros2dds
# Zenoh
uv run python3 -m zenoh_ros_type.examples.listener
# ROS
ros2 run demo_nodes_cpp talker
```

## Service client

```bash
# Run bridge
zenoh-bridge-ros2dds
# ROS (Need to switch to CycloneDDS or it can't work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run demo_nodes_cpp add_two_ints_server
# Zenoh
uv run python3 -m zenoh_ros_type.examples.service_client
```

## Service server

```bash
# Run bridge
zenoh-bridge-ros2dds
# Zenoh
uv run python3 -m zenoh_ros_type.examples.service_server
# ROS (Need to switch to CycloneDDS or it can't work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run demo_nodes_cpp add_two_ints_client
```

## Action client

```bash
# Run bridge
zenoh-bridge-ros2dds
# ROS (Need to switch to CycloneDDS or it can't work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run action_tutorials_cpp fibonacci_action_server
# Zenoh
uv run python3 -m zenoh_ros_type.examples.action_client
```

## Action server

```bash
# Run bridge
zenoh-bridge-ros2dds
# Zenoh
uv run python3 -m zenoh_ros_type.examples.action_server
# ROS (Need to switch to CycloneDDS or it can't work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run action_tutorials_cpp fibonacci_action_client
```

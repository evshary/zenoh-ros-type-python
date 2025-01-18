# Examples

Here are some basic usages for the library.

## Talker

```bash
# Run bridge
zenoh-bridge-ros2dds
# Zenoh
python3 talker.py
# ROS
ros2 run demo_nodes_cpp listener
```

## Listener

```bash
# Run bridge
zenoh-bridge-ros2dds
# Zenoh
python3 listener.py
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
python3 service_client.py
```

## Service server

```bash
# Run bridge
zenoh-bridge-ros2dds
# Zenoh
python3 service_server.py
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
python3 action_client.py
```

## Action server

```bash
# Run bridge
zenoh-bridge-ros2dds
# Zenoh
python3 action_server.py
# ROS (Need to switch to CycloneDDS or it can't work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run action_tutorials_cpp fibonacci_action_client

```

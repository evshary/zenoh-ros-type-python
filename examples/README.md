# Examples

Here are some basic usages for the library.
The examples code are in [zenoh_ros_type/examples](../zenoh_ros_type/examples) and support both `zenoh-bridge-ros2dds` and `rmw_zenoh` modes.

Setup the environment before running the examples.

```bash
uv sync --extra dev
```

## Talker

### Talker - zenoh-bridge-ros2dds

```bash
# Run the bridge
zenoh-bridge-ros2dds

# Zenoh
uv run python3 -m zenoh_ros_type.examples.talker

# ROS (must switch to CycloneDDS, otherwise it will not work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run demo_nodes_cpp listener
```

### Talker - rmw_zenoh

```bash
# Start the Zenoh router
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run rmw_zenoh_cpp rmw_zenohd

# Zenoh
uv run python3 -m zenoh_ros_type.examples.talker --rmw_zenoh -e tcp/localhost:7447

# ROS
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run demo_nodes_cpp listener
```

## Listener

### Listener - zenoh-bridge-ros2dds

```bash
# Run the bridge
zenoh-bridge-ros2dds

# Zenoh
uv run python3 -m zenoh_ros_type.examples.listener

# ROS (must switch to CycloneDDS, otherwise it will not work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run demo_nodes_cpp talker
```

### Listener - rmw_zenoh

```bash
# Start the Zenoh router
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run rmw_zenoh_cpp rmw_zenohd

# Zenoh
uv run python3 -m zenoh_ros_type.examples.listener --rmw_zenoh -e tcp/localhost:7447

# ROS
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run demo_nodes_cpp talker
```

## Service Client

### Service Client - zenoh-bridge-ros2dds

```bash
# Run the bridge
zenoh-bridge-ros2dds

# ROS (must switch to CycloneDDS, otherwise it will not work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run demo_nodes_cpp add_two_ints_server

# Zenoh
uv run python3 -m zenoh_ros_type.examples.service_client
```

### Service Client - rmw_zenoh

```bash
# Start the Zenoh router
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run rmw_zenoh_cpp rmw_zenohd

# ROS
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run demo_nodes_cpp add_two_ints_server

# Zenoh
uv run python3 -m zenoh_ros_type.examples.service_client --rmw_zenoh -e tcp/localhost:7447
```

## Service Server

### Service Server - zenoh-bridge-ros2dds

```bash
# Run the bridge
zenoh-bridge-ros2dds

# Zenoh
uv run python3 -m zenoh_ros_type.examples.service_server

# ROS (must switch to CycloneDDS, otherwise it will not work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run demo_nodes_cpp add_two_ints_client
```

### Service Server - rmw_zenoh

```bash
# Start the Zenoh router
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run rmw_zenoh_cpp rmw_zenohd

# Zenoh
uv run python3 -m zenoh_ros_type.examples.service_server --rmw_zenoh -e tcp/localhost:7447

# ROS
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run demo_nodes_cpp add_two_ints_client
```

## Action Client

### Action Client - zenoh-bridge-ros2dds

```bash
# Run the bridge
zenoh-bridge-ros2dds

# ROS (must switch to CycloneDDS, otherwise it will not work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run action_tutorials_cpp fibonacci_action_server

# Zenoh
uv run python3 -m zenoh_ros_type.examples.action_client
```

### Action Client - rmw_zenoh

```bash
# Start the Zenoh router
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run rmw_zenoh_cpp rmw_zenohd

# ROS
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run action_tutorials_cpp fibonacci_action_server

# Zenoh
uv run python3 -m zenoh_ros_type.examples.action_client --rmw_zenoh -e tcp/localhost:7447
```

## Action Server

### Action Server - zenoh-bridge-ros2dds

```bash
# Run the bridge
zenoh-bridge-ros2dds

# Zenoh
uv run python3 -m zenoh_ros_type.examples.action_server

# ROS (must switch to CycloneDDS, otherwise it will not work)
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ros2 run action_tutorials_cpp fibonacci_action_client
```

### Action Server - rmw_zenoh

```bash
# Start the Zenoh router
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run rmw_zenoh_cpp rmw_zenohd

# Zenoh
uv run python3 -m zenoh_ros_type.examples.action_server --rmw_zenoh -e tcp/localhost:7447

# ROS
export RMW_IMPLEMENTATION=rmw_zenoh_cpp
ros2 run action_tutorials_cpp fibonacci_action_client
```

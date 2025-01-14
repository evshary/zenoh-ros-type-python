# zenoh-ros-type-python

The repository contains common class for ROS 2 messages used by Zenoh.

The messages come from:

* [common_interface](https://github.com/ros2/common_interfaces): Common-used ROS message
* [rcl_interface](https://github.com/ros2/rcl_interfaces): Common interface in RCL
* [autoware_auto_msgs](https://github.com/tier4/autoware_auto_msgs/tree/tier4/main): messages used in Autoware
* [tier4_autoware_msgs](https://github.com/tier4/tier4_autoware_msgs/tree/tier4/universe): messages used in Autoware
* [autoware_adapi_msgs](https://github.com/autowarefoundation/autoware_adapi_msgs): messages used in Autoware
* [geographic_info](https://github.com/ros-geographic-info/geographic_info/tree/master): ROS geographic information project

## Usage

You can download the packages via [PyPI](https://pypi.org/project/zenoh-ros-type/).

```shell
python3 -m pip install zenoh-ros-type
```

## Examples

You can check the examples folder for the basic usage.
Also, there are some examples for how to use zenoh-ros-type-python in your application.

* [zenoh_autoware_fms](https://github.com/evshary/zenoh_autoware_fms): Fleet management system prototype of Autoware based on Zenoh.
* [zenoh_autoware_v2x](https://github.com/evshary/zenoh_autoware_v2x): Integrate the autonomous system between multiple vehicles and the traffic light manager with zenoh.

## For developers

* Install pre-commit hook

```shell
pre-commit install --install-hooks
```

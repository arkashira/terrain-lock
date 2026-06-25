# VIO Engine

Visual-Inertial Odometry Engine for drone autopilot systems.

## Features

* Outputs 6-DOF pose at ≥ 30 Hz on target hardware (e.g., NVIDIA Jetson Nano)
* Pose error ≤ 0.5 m on benchmark dataset (EuRoC MAV)
* API is a Python module with init, update(frame, imu), and getPose() functions
* Fails gracefully with error codes when camera frames are dropped

## Usage

1. Initialize the VIO engine: `vio = VIOEngine()`
2. Update the VIO engine with frame and IMU data: `vio.update(b"frame_data", (1, 2, 3))`
3. Get the current pose: `pose = vio.get_pose()`

## Testing

Run the tests using `pytest`: `pytest tests/test_vio_engine.py`

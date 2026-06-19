# TECH_SPEC.md
## terrain‑lock
**Product:** GPS‑jamming‑resistant navigation system for drones  
**Repository:** `terrain-lock` (Axentx internal)  
**Owner:** Senior Product/Engineering Lead – [Your Name]  
**Last Updated:** 2026‑06‑19  

---  

### 1. Overview
`terrain-lock` provides autonomous drones with reliable positioning when GNSS signals are degraded or jammed. It fuses **terrain‑relative navigation (TRN)**, **visual‑inertial odometry (VIO)**, and **inertial measurement unit (IMU)** data to maintain sub‑meter accuracy in GPS‑denied environments. The system runs on edge‑compute hardware (e.g., NVIDIA Jetson AGX Orin, Qualcomm Snapdragon Flight) and exposes a clean C++/Python API for integration with existing flight‑control stacks (PX4, ArduPilot).

### 2. Architecture Diagram
```
+-------------------+       +-------------------+       +-------------------+
|  Sensors Layer    |       |  Perception Layer |       |  Fusion & Control |
|-------------------|       |-------------------|       |-------------------|
| • Stereo Camera   | <---> | • Terrain Matcher | <---> | • EKF / UKF       |
| • Monocular Camera|       |   (SGLang)        |       |   (vLLM‑based)    |
| • IMU (9‑DoF)     |       | • VIO (ORB‑SLAM3) |       | • State Estimator |
| • Barometer       |       | • Depth (optional)|       | • Command Output  |
+-------------------+       +-------------------+       +-------------------+
        |                           |                           |
        |  ROS2 Topics / DDS       |  ROS2 Services / Actions   |
        +---------------------------+---------------------------+
                              |
                              v
                     +-------------------+
                     |  Telemetry / UI   |
                     +-------------------+
```

### 3. Core Components
| Component | Description | Language / Lib | Key Interfaces |
|-----------|-------------|----------------|----------------|
| **Sensor Driver Suite** | Unified abstraction over cameras, IMU, barometer. Handles time‑sync via hardware timestamps. | C++ (ROS2 `rclcpp`), Python bindings | ROS2 topics: `/camera/left`, `/camera/right`, `/imu/data`, `/baro` |
| **Terrain Matcher** | Generates a dense elevation map from satellite DEMs (e.g., SRTM, Copernicus) and matches live camera frames using SGLang structured generation for robust feature‑to‑terrain association. | C++ (vLLM inference), Python (SGLang) | Service: `MatchTerrain(frame) -> PoseEstimate` |
| **Visual‑Inertial Odometry (VIO)** | Real‑time pose tracking using ORB‑SLAM3 with IMU pre‑integration. Falls back to monocular mode if stereo fails. | C++ (ORB‑SLAM3) | ROS2 topic: `/vio/pose` |
| **Fusion Engine** | Tightly‑coupled EKF/UKF that fuses terrain matches, VIO, and raw IMU to produce a unified state estimate. Includes outlier rejection based on Mahalanobis distance. | C++ (Eigen, Boost), optional Python for prototyping | ROS2 topic: `/state_estimate` |
| **Mission Controller** | Provides high‑level commands (e.g., “hold position”, “navigate to waypoint”) that consume the fused state and output set‑points to the flight controller. | Python (asyncio) | ROS2 actions: `Navigate`, `Hold` |
| **Telemetry & UI** | Web‑socket server streaming live pose, confidence, and sensor health; UI built with React + Three.js for 3D visualization. | Node.js, TypeScript | WebSocket `/ws/telemetry` |
| **Configuration Manager** | Central YAML/JSON schema validated at startup; supports hot‑reload via ROS2 parameters. | C++/Python | ROS2 parameters node |

### 4. Data Model
```yaml
# pose_estimate.yaml
timestamp: uint64          # nanoseconds since epoch
position:
  x: float64               # meters (ENU)
  y: float64
  z: float64
orientation:
  qx: float64              # quaternion
  qy: float64
  qz: float64
  qw: float64
covariance: [float64]      # 6x6 matrix flattened row‑major
source: enum               # {VIO, TERRAIN, FUSED}
confidence: float32       # 0.0‑1.0
```
All messages use ROS2 `builtin_interfaces/msg/Time` for timestamps and `geometry_msgs/msg/PoseWithCovarianceStamped` for transport.

### 5. Key APIs / Interfaces
#### 5.1 ROS2 Topics
| Topic | Type | Direction | Description |
|-------|------|-----------|-------------|
| `/camera/left` | `sensor_msgs/Image` | Pub | Stereo left image |
| `/camera/right` | `sensor_msgs/Image` | Pub | Stereo right image |
| `/imu/data` | `sensor_msgs/Imu` | Pub | Raw IMU |
| `/vio/pose` | `geometry_msgs/PoseStamped` | Pub | VIO pose |
| `/terrain/pose` | `geometry_msgs/PoseStamped` | Pub | Terrain match pose |
| `/state_estimate` | `geometry_msgs/PoseWithCovarianceStamped` | Pub | Fused pose |
| `/mission/cmd` | `custom_msgs/MissionCmd` | Sub | High‑level mission commands |

#### 5.2 ROS2 Services
- `MatchTerrain(frame: sensor_msgs/Image) -> PoseEstimate`  
  *Synchronous terrain‑matching request.*

#### 5.3 ROS2 Actions
- `Navigate(goal: geometry_msgs/Point) -> result: bool`  
  *Guides drone to a waypoint using fused pose.*

#### 5.4 Python SDK (optional)
```python
from terrain_lock import TerrainLockClient

client = TerrainLockClient()
pose = client.get_fused_pose()
client.send_waypoint(x=12.3, y=-4.5, z=30.0)
```

### 6. Technology Stack
| Layer | Technology | Version (as of 2026‑06) |
|-------|-------------|------------------------|
| OS | Ubuntu 22.04 LTS (ARM64) | |
| Runtime | ROS2 Humble Hawksbill | |
| Inference Engine | vLLM (v0.5) – compiled with CUDA 12.4 | |
| Structured Generation | SGLang (commit `a1b2c3d`) | |
| SLAM | ORB‑SLAM3 (v1.5) | |
| Linear Algebra | Eigen 3.4, Boost 1.82 | |
| Containerization | Docker 24.0 (multi‑arch) | |
| CI/CD | GitHub Actions + Axentx BRAIN pipelines | |
| Telemetry UI | React 18, Three.js r158, Node 20 | |
| Messaging | DDS Fast‑RTPS (default ROS2) | |
| Build System | CMake 3.27, colcon | |
| Testing | GoogleTest, pytest, ROS2 launch testing | |

### 7. External Dependencies
| Dependency | License | Reason |
|------------|---------|--------|
| vLLM | Apache‑2.0 | High‑throughput GPU inference for terrain matcher |
| SGLang | MIT | Structured prompt generation for robust feature matching |
| ORB‑SLAM3 | BSD‑3 | Proven VIO/SLAM algorithm |
| ROS2 Humble | Apache‑2.0 | Middleware & ecosystem |
| Eigen | MPL‑2.0 | Linear algebra |
| Boost | Boost‑1.0 | Utilities |
| React/Three.js | MIT | UI visualization |
| Docker | Apache‑2.0 | Container runtime |

All dependencies are vetted for commercial use and are listed in `third_party/LICENSES.md`.

### 8. Deployment Architecture
1. **Edge Device Image** – Ubuntu 22.04 + ROS2 Humble + pre‑installed `terrain-lock` binaries, built via Docker multi‑stage and exported as a `.squashfs` OTA package.
2. **Runtime** – Systemd service `terrain-lock.service` launches the ROS2 launch file `terrain_lock.launch.py`.  
3. **Hardware Requirements**  
   - **Compute:** NVIDIA Jetson AGX Orin (minimum 8 GB VRAM) or Snapdragon Flight (GPU‑offload via Vulkan).  
   - **Sensors:** Stereo camera (global shutter, ≥30 fps, 1280×720), 9‑DoF IMU, barometer.  
   - **Storage:** 8 GB persistent for DEM tiles (cached on‑flight).  
4. **Network** – Optional Wi‑Fi/5G link for telemetry; system degrades gracefully to offline mode.  
5. **OTA Update Flow** – New Docker image pushed to Axentx artifact registry; drones pull via `axentx-updater` service, verify signature, and restart the ROS2 node.

### 9. Security & Safety
- **Code Signing:** All binaries signed with company ECDSA key; verification at startup.  
- **Isolation:** ROS2 DDS domains per drone; no cross‑drone traffic.  
- **Fail‑Safe:** If fused confidence < 0.3 for > 2 s, system publishes `MISSION_ABORT` and reverts to manual control.  
- **Data Privacy:** DEM tiles are cached locally; no raw imagery is uploaded unless explicitly enabled.

### 10. Testing & Validation
| Test Type | Scope | Tools |
|-----------|-------|-------|
| Unit | All C++ classes, Python wrappers | GoogleTest, pytest |
| Integration | ROS2 topic flow, service latency | ros2 launch testing, `rqt_graph` |
| System | End‑to‑end flight in GPS‑denied indoor arena | PX4 SITL, motion‑capture ground truth |
| Performance | Inference latency < 30 ms per frame, overall loop ≤ 100 ms | NVIDIA Nsight, ROS2 `ros2 topic hz` |
| Jamming Resilience | Simulated GNSS denial (RF jammer) | GNSS‑simulator, RF shielded test range |
| Regression | Nightly CI on BRAIN, with dataset drift detection | Axentx BRAIN auto‑metrics |

### 11. Roadmap (post‑MVP)
| Milestone | Target | Description |
|-----------|--------|-------------|
| **MVP** | Q3 2026 | Full TRN + VIO fusion, ROS2 API, OTA package. |
| **Multi‑Sensor Fusion** | Q4 2026 | Add LiDAR depth map for improved terrain matching. |
| **Adaptive DEM Caching** | Q1 2027 | On‑flight DEM tile pre‑fetch based on mission plan. |
| **Swarm Coordination** | Q3 2027 | Share pose confidence among multiple drones via DDS. |
| **Regulatory Certification** | Q1 2028 | CE/FAA compliance for commercial BVLOS operations. |

### 12. Glossary
- **TRN** – Terrain‑Relative Navigation.  
- **VIO** – Visual‑Inertial Odometry.  
- **EKF/UKF** – Extended / Unscented Kalman Filter.  
- **DEM** – Digital Elevation Model.  
- **DDS** – Data Distribution Service (ROS2 transport).  

---  

*Prepared by the terrain‑lock engineering team. For questions, contact the product lead or open an issue in the repository.*

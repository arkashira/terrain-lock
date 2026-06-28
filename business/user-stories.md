```markdown
# User Stories for Terrain-Lock

## Epic 1: GPS Jamming Detection
### User Story 1
**As a** drone operator, **I want** the system to detect GPS jamming attempts, **so that** I can be alerted and take necessary actions.

**Acceptance Criteria:**
- The system should identify and log any GPS signal anomalies.
- Alerts should be sent to the operator's mobile device in real-time.
- The detection system should work in various environmental conditions (urban, rural, etc.).
- The system should provide a historical log of detected jamming attempts.

**Estimated Complexity:** M

### User Story 2
**As a** drone operator, **I want** to receive notifications when GPS jamming is detected, **so that** I can switch to alternative navigation methods promptly.

**Acceptance Criteria:**
- Notifications should be customizable (e.g., sound, vibration).
- The system should allow for different notification methods (SMS, app notification, email).
- Notifications should include the type of jamming detected and its intensity.

**Estimated Complexity:** S

## Epic 2: Alternative Navigation Methods
### User Story 3
**As a** drone operator, **I want** the system to utilize terrain recognition for navigation, **so that** I can maintain flight paths even when GPS is unavailable.

**Acceptance Criteria:**
- The terrain recognition algorithm should be able to process real-time data.
- The system should provide a visual representation of the terrain being navigated.
- The navigation should be accurate within a specified margin of error (e.g., 5 meters).

**Estimated Complexity:** L

### User Story 4
**As a** drone operator, **I want** to configure the system to switch to inertial measurement navigation, **so that** I can continue operations seamlessly during GPS loss.

**Acceptance Criteria:**
- The system should allow for manual or automatic switching to inertial navigation.
- The accuracy of inertial navigation should be validated against known benchmarks.
- The system should provide feedback on the current navigation method in use.

**Estimated Complexity:** M

## Epic 3: User Interface and Experience
### User Story 5
**As a** drone operator, **I want** an intuitive user interface, **so that** I can easily access navigation options and alerts.

**Acceptance Criteria:**
- The interface should be user-friendly and require minimal training.
- Key functionalities (alerts, navigation methods) should be easily accessible.
- The interface should be responsive and work on various devices (tablets, smartphones).

**Estimated Complexity:** M

### User Story 6
**As a** drone operator, **I want** to view real-time navigation data on a map, **so that** I can make informed decisions during flight.

**Acceptance Criteria:**
- The map should display the drone's current position, flight path, and any detected jamming.
- The map should update in real-time with minimal latency.
- Users should be able to zoom in/out and switch between map views (satellite, terrain).

**Estimated Complexity:** L

## Epic 4: Performance and Reliability
### User Story 7
**As a** drone operator, **I want** the system to maintain high reliability under various conditions, **so that** I can trust it during critical missions.

**Acceptance Criteria:**
- The system should have a minimum uptime of 99.9%.
- Performance metrics should be logged and available for review.
- The system should recover from failures without user intervention.

**Estimated Complexity:** L

### User Story 8
**As a** drone operator, **I want** the system to be lightweight and energy-efficient, **so that** it does not impact the drone's performance.

**Acceptance Criteria:**
- The system's resource usage should be within specified limits (e.g., CPU, memory).
- The energy consumption should not exceed a predefined threshold during operation.
- The system should provide feedback on resource usage in real-time.

**Estimated Complexity:** M
```
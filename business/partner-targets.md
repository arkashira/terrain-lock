# partner-targets.md

## Partner Integration Roadmap

**Strategy:** `terrain-lock` solves the "Positioning Void" created by GPS jamming. We do not replace GPS; we replace the *positioning source* with visual/terrain correlation. Partners must provide high-fidelity terrain data or visual context to enable this correlation.

### 1. Mapbox (Vector Tiles & Navigation API)
*   **Type:** Navigation & Terrain Data
*   **Rationale:** Essential for providing the "Digital Twin" of the environment. Mapbox Vector Tiles allow for offline, high-performance rendering of terrain contours (contours, elevation) which is the primary input for `terrain-lock`'s fallback navigation.
*   **Integration Effort:** **Medium** (Requires custom tile styling and API key management in the drone firmware).
*   **Value-Add:** Enables precise altitude holding and path planning in 3D space when GPS is lost. Solves the "Lost in Space" job for surveyors.
*   **Free Tier:** 50,000 loads/month (insufficient for heavy drone fleets, requires paid tier).
*   **Revenue Model:** **Usage-based Affiliate** (Mapbox pays for successful API calls routed through our platform).

### 2. DroneDeploy (Surveying Platform)
*   **Type:** Vertical SaaS (Surveying)
*   **Rationale:** The primary use case for GPS-denied navigation is critical infrastructure inspection (pipelines, cell towers) where GPS is often jammed by the facility itself or by nearby military exercises.
*   **Integration Effort:** **Large** (Requires SDK integration into their flight planning interface).
*   **Value-Add:** Adds a "Geo-Fence Safety Layer" that activates if the drone detects signal loss, forcing it to land or hold position using terrain data. Solves the "Regulatory Compliance" job for enterprise clients.
*   **Free Tier:** 1 mission/month (limited utility for integration testing).
*   **Revenue Model:** **Reseller/Revenue Share** (DroneDeploy pays for enterprise seats sold with `terrain-lock` as a safety module).

### 3. Planet Labs (Satellite Imagery)
*   **Type:** Pre-flight Data Source
*   **Rationale:** Before a drone enters a jammed zone, it needs a high-resolution map of the terrain. Planet Labs provides the fastest revisit times for high-res imagery.
*   **Integration Effort:** **Small** (API fetch for mission planning).
*   **Value-Add:** Allows operators to "pre-load" the terrain mesh for a specific zone, ensuring `terrain-lock` has the best possible data to match against visual sensors.
*   **Free Tier:** 5 scenes/month.
*   **Revenue Model:** **Usage-based Affiliate** (Planet Labs pays for API credits consumed).

### 4. AWS Rekognition (Computer Vision)
*   **Type:** Visual Obstacle Avoidance
*   **Rationale:** `terrain-lock` relies on visual odometry (SLAM). We need an API to classify terrain features (e.g., "power line," "tree canopy," "building wall") to avoid collisions in GPS-denied environments.
*   **Integration Effort:** **Medium** (Video stream processing pipeline).
*   **Value-Add:** Provides semantic understanding of the environment, allowing the drone to distinguish between "safe ground" and "dangerous obstacles" purely by sight.
*   **Free Tier:** 5,000 image analysis calls/month.
*   **Revenue Model:** **Pay-per-use** (Standard AWS model; no direct affiliate, but drives platform stickiness).

### 5. DroneShield (Anti-Jamming Hardware Partner)
*   **Type:** Hardware / Sensor Fusion
*   **Rationale:** They are the market leader in detecting GPS jamming. We are the market leader in surviving it. They detect the *threat*; we provide the *solution*.
*   **Integration Effort:** **Large** (Hardware serial integration).
*   **Value-Add:** Creates a "Fail-Safe" bundle. If DroneShield detects a jam, it triggers `terrain-lock` to engage immediately. Solves the "Operational Continuity" job for defense contractors.
*   **Free Tier:** N/A (Hardware sales).
*   **Revenue Model:** **Hardware Affiliate** (DroneShield pays for hardware bundles sold together).

### 6. Pix4D (Photogrammetry)
*   **Type:** Mapping & 3D Terrain Generation
*   **Rationale:** Surveyors need to map the terrain *after* the flight. `terrain-lock` can ingest Pix4D outputs to create a local map for future flights in the same area.
*   **Integration Effort:** **Medium** (File format conversion and mesh import).
*   **Value-Add:** Turns `terrain-lock` into a "Surveying Assistant" that remembers the terrain geometry of a site, improving accuracy over multiple passes.
*   **Free Tier:** 1 project/month (Processing time limited).
*   **Revenue Model:** **Reseller** (Pix4D pays for enterprise licenses sold via our platform).

### 7. Skydio (Hardware Partner - via 3rd Party Integrators)
*   **Type:** Hardware Platform
*   **Rationale:** Skydio drones are famous for autonomous navigation but rely heavily on GPS. Integrating `terrain-lock` as a "backup nav" for Skydio hardware creates a high-value niche product for enterprise users.
*   **Integration Effort:** **Large** (Requires access to Skydio's internal API/SDK).
*   **Value-Add:** Allows enterprise users to fly Skydios in "GPS Denied Zones" (e.g., inside warehouses, near cell towers) where Skydio normally fails.
*   **Free Tier:** N/A.
*   **Revenue Model:** **Hardware License** (Skydio pays for software licenses embedded in their hardware sales).
```markdown
# Dataflow Architecture for Terrain-Lock

## External Data Sources
- **Terrain Data**: High-resolution terrain maps and elevation data from sources like USGS or similar.
- **Inertial Measurement Units (IMUs)**: Data from onboard sensors providing acceleration and angular velocity.
- **Environmental Sensors**: Weather data (wind speed, temperature) affecting drone navigation.
- **User Input**: Flight plans and operational parameters from drone operators.

## Ingestion Layer
- **Data Ingestion Service**: 
  - Collects data from external sources.
  - Validates and preprocesses incoming data.
- **Authentication Service**: 
  - Ensures secure access to data sources.
  - Validates user credentials and permissions.

## Processing/Transform Layer
- **Terrain Recognition Engine**: 
  - Analyzes terrain data for navigation.
  - Utilizes machine learning algorithms for pattern recognition.
- **Sensor Fusion Module**: 
  - Combines data from IMUs and environmental sensors.
  - Provides a cohesive navigation solution.
- **GPS Jamming Detection Module**: 
  - Monitors for GPS signal anomalies.
  - Triggers alternative navigation methods when jamming is detected.

## Storage Tier
- **Data Lake**: 
  - Stores raw and processed data for historical analysis.
  - Supports various data formats (structured and unstructured).
- **Database**: 
  - Stores user profiles, flight plans, and operational logs.
  - Utilizes a relational database for structured data.

## Query/Serving Layer
- **API Gateway**: 
  - Exposes endpoints for user interaction.
  - Handles authentication and authorization.
- **Query Engine**: 
  - Processes user requests for navigation data.
  - Retrieves relevant data from the database and data lake.

## Egress to User
- **User Interface**: 
  - Web or mobile application for drone operators.
  - Displays navigation data, alerts, and operational status.
- **Notification Service**: 
  - Sends alerts for GPS jamming detection and system status updates.
  - Communicates via push notifications or email.

```

```
ASCII Block Diagram:

+-------------------+        +-------------------+        +-------------------+
|  External Data    | -----> |   Ingestion Layer  | -----> | Processing/Transform |
|      Sources       |        |                   |        |        Layer        |
+-------------------+        +-------------------+        +-------------------+
                                   |                            |
                                   |                            |
                                   v                            v
                            +-------------------+        +-------------------+
                            |     Storage Tier   | <----> |  Query/Serving    |
                            |                   |        |        Layer       |
                            +-------------------+        +-------------------+
                                   |
                                   |
                                   v
                            +-------------------+
                            |   Egress to User   |
                            +-------------------+
```
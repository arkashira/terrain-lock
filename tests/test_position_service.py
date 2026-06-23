import pytest
from position_service import Position, PositionService

@pytest.fixture
def position_service():
    return PositionService()

def test_get_position(position_service):
    drone_id = "drone1"
    token = "valid_token"
    position = Position(37.7749, -122.4194, 10.0)
    position_service.update_position(drone_id, position)
    result = position_service.get_position(drone_id, token)
    assert result == position

def test_get_position_invalid_token(position_service):
    drone_id = "drone1"
    token = "invalid_token"
    position = Position(37.7749, -122.4194, 10.0)
    position_service.update_position(drone_id, position)
    result = position_service.get_position(drone_id, token)
    assert result is None

def test_get_position_drone_not_found(position_service):
    drone_id = "drone1"
    token = "valid_token"
    result = position_service.get_position(drone_id, token)
    assert result is None

def test_update_position(position_service):
    drone_id = "drone1"
    position = Position(37.7749, -122.4194, 10.0)
    position_service.update_position(drone_id, position)
    result = position_service.get_position(drone_id, "valid_token")
    assert result == position

def test_handle_sensor_fusion_failure(position_service):
    drone_id = "drone1"
    position_service.handle_sensor_fusion_failure(drone_id)
    # No exception raised

def test_handle_low_confidence(position_service):
    drone_id = "drone1"
    position_service.handle_low_confidence(drone_id)
    # No exception raised

def test_concurrent_connections(position_service):
    num_drones = 50
    for i in range(num_drones):
        drone_id = f"drone{i}"
        position = Position(37.7749, -122.4194, 10.0)
        position_service.update_position(drone_id, position)
    for i in range(num_drones):
        drone_id = f"drone{i}"
        result = position_service.get_position(drone_id, "valid_token")
        assert result is not None

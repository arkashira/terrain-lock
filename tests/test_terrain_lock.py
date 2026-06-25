import pytest
from src.terrain_lock import TerrainLock, Pose

def test_init():
    lock = TerrainLock()
    lock.init()
    assert lock.get_pose() == Pose(0, 0, 0)

def test_update():
    lock = TerrainLock()
    lock.init()
    data = {'dx': 1, 'dy': 2, 'dz': 3}
    lock.update(data)
    assert lock.get_pose() == Pose(1, 2, 3)

def test_get_pose():
    lock = TerrainLock()
    lock.init()
    data = {'dx': 1, 'dy': 2, 'dz': 3}
    lock.update(data)
    pose = lock.get_pose()
    assert pose.x == 1
    assert pose.y == 2
    assert pose.z == 3

def test_update_invalid_data():
    lock = TerrainLock()
    lock.init()
    data = {'invalid': 'data'}
    lock.update(data)
    assert lock.get_pose() == Pose(0, 0, 0)

def test_get_pose_before_init():
    lock = TerrainLock()
    with pytest.raises(AttributeError):
        lock.get_pose()

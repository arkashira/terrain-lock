import pytest
from vio_engine import VIOEngine, Pose

def test_vio_engine_init():
    vio = VIOEngine()
    assert vio.pose == Pose(0, 0, 0, 0, 0, 0)

def test_vio_engine_update():
    vio = VIOEngine()
    vio.update(b"frame_data", (1, 2, 3))
    assert vio.pose.x == 0.01
    assert vio.pose.y == 0.02
    assert vio.pose.z == 0.03

def test_vio_engine_get_pose():
    vio = VIOEngine()
    vio.update(b"frame_data", (1, 2, 3))
    pose = vio.get_pose()
    assert pose.x == 0.01
    assert pose.y == 0.02
    assert pose.z == 0.03

def test_vio_engine_fail_gracefully():
    vio = VIOEngine()
    with pytest.raises(RuntimeError):
        vio.fail_gracefully(1)

def test_vio_engine_update_rate():
    vio = VIOEngine()
    for _ in range(30):
        vio.update(b"frame_data", (1, 2, 3))
    assert vio.frame_count == 30

def test_vio_engine_pose_error():
    vio = VIOEngine()
    vio.update(b"frame_data", (1, 2, 3))
    pose = vio.get_pose()
    assert abs(pose.x) <= 0.5
    assert abs(pose.y) <= 0.5
    assert abs(pose.z) <= 0.5

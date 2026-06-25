import json
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Pose:
    x: float = 0
    y: float = 0
    z: float = 0

class TerrainLock:
    def __init__(self):
        self._initialized = False
        self.pose = None

    def init(self):
        # Initialize the terrain lock system
        self.pose = Pose(0, 0, 0)
        self._initialized = True
        return True

    def update(self, data: Dict):
        # Update the pose based on the provided data
        if not self._initialized:
            raise AttributeError("TerrainLock instance not initialized")
        self.pose.x += data.get('dx', 0)
        self.pose.y += data.get('dy', 0)
        self.pose.z += data.get('dz', 0)
        return True

    def get_pose(self):
        # Return the current pose
        if not self._initialized:
            raise AttributeError("TerrainLock instance not initialized")
        return self.pose

def main():
    # Create a terrain lock instance
    lock = TerrainLock()
    # Initialize the terrain lock system
    lock.init()
    # Update the pose
    data = {'dx': 1, 'dy': 2, 'dz': 3}
    lock.update(data)
    # Get the current pose
    pose = lock.get_pose()
    print(pose)

if __name__ == '__main__':
    main()

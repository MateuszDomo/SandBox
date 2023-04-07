import random
import numpy as np

class BoxBounds:
    def __init__(self, top: float, right: float, bottom: float, left: float):
        self.top: float = top
        self.right: float = right
        self.bottom: float = bottom
        self.left: float = left

        
class SandBox:
    def __init__(self, num_grains: int, box_bounds: BoxBounds): 
        self.num: int = num_grains
        self.grainsX: list = np.random.uniform(box_bounds.left,box_bounds.right, size = num_grains)
        self.grainsY: list = np.random.uniform(box_bounds.bottom,box_bounds.top, size = num_grains)
        self.bbox: BoxBounds = box_bounds

    def update(self):
        displacement = 3.0

        dx = np.random.uniform(-displacement, displacement, size=self.num)
        dy = np.random.uniform(-displacement, displacement, size=self.num)
        self.grainsX += dx
        self.grainsY += dy

        # make sure the grains stay within the bounding box
        np.clip(self.grainsX, self.bbox.left, self.bbox.right, out=self.grainsX)
        np.clip(self.grainsY, self.bbox.bottom, self.bbox.top, out=self.grainsY)
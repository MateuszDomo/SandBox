import random

class BoxBounds:
    def __init__(self, top: float, right: float, bottom: float, left: float):
        self.top: float = top
        self.right: float = right
        self.bottom: float = bottom
        self.left: float = left

class XY:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def update(self, x: int, y: int):
        self.x = x
        self.y = y
        
class SandBox:
    def __init__(self, num_grains: int, box_bounds: BoxBounds): 
        self.num: int = num_grains
        self.grainsX: list = []
        self.grainsY: list = []
        self.bbox: BoxBounds = box_bounds
        self._fillSandBox()

    def _fillSandBox(self):
        top = self.bbox.top
        right = self.bbox.right
        bottom = self.bbox.bottom
        left = self.bbox.left
    
        for i in range(self.num):
            self.grainsX.append(random.uniform(left,right))
            self.grainsY.append(random.uniform(bottom,top))

    def update(self):
        top = self.bbox.top
        right = self.bbox.right
        bottom = self.bbox.bottom
        left = self.bbox.left
        displacement = 1

        for i in range(self.num):
            dx = random.uniform(-displacement, displacement)
            dy = random.uniform(-displacement, displacement)
            self.grainsX[i] += dx
            self.grainsY[i] += dy

            # make sure the grains stay within the bounding box
            self.grainsX[i] = max(self.grainsX[i], left)
            self.grainsX[i] = min(self.grainsX[i], right)
            self.grainsY[i] = max(self.grainsY[i], bottom)
            self.grainsY[i] = min(self.grainsY[i], top)
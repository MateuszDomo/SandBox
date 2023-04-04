import random

class SandBox:
    def __init__(self, rows: int, cols: int): 
        self.box = [[0 for c in range(cols)] for r in range(rows)]
        self.rows = rows
        self.cols = cols
        self.fillSandBox()

    def fillSandBox(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.box[r][c] = random.choice([0,1])
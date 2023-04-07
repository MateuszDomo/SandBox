from sand_box import SandBox, BoxBounds
from matplotlib.animation import FuncAnimation

import numpy as np
import matplotlib.pyplot as plt
import time

# TODO: make each grain of sand have x,y and paint them. In order to apply wave functions on them.
def main():
    
    sandbox = SandBox(1000,BoxBounds(100.0,100.0,0.0,0.0))
    fig, ax = plt.subplots(figsize=(6,6), facecolor = 'white',frameon=False)
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
    ax.set_axis_off()

    ax.scatter(sandbox.grainsX,sandbox.grainsY,s=3)

    def update(frame):
        sandbox.update()
        ax.clear()
        scatter = ax.scatter(sandbox.grainsX,sandbox.grainsY,s=3)
        return scatter,
    anim = FuncAnimation(fig,update,frames = 100, interval =16.67, blit = True)

    plt.show()


if __name__ == "__main__":
    main()



    

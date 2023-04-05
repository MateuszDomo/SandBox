from sand_box import SandBox, BoxBounds
from matplotlib.animation import FuncAnimation

import matplotlib.pyplot as plt

# TODO: make each grain of sand have x,y and paint them. In order to apply wave functions on them.
def main():
    
    sandbox = SandBox(100,BoxBounds(100.0,100.0,0.0,0.0))

    fig, ax = plt.subplots(figsize=(6,6), facecolor = 'white',frameon=False)
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

    ax.set_axis_off()
    def update(frame):
        sandbox.update()
        ax.clear()
        ax.scatter(sandbox.grainsX,sandbox.grainsY,s=3)
    
    anim = FuncAnimation(fig,update,frames=100,interval=16.67)

    plt.show()

def update(ax,sandbox,frame):
    sandbox.update()
    ax.clear()
    ax.scatter(sandbox.grainsX,sandbox.grainsY,s=3)

if __name__ == "__main__":
    main()



    

from sand_box import SandBox
import matplotlib.pyplot as plt

# TODO: make each grain of sand have x,y and paint them. In order to apply wave functions on them.
def main():
    sand_box: SandBox = SandBox(1000,1000)
    window = plt.imshow(sand_box.box, cmap='Greys')
    plt.pause(2)
    sand_box.fillSandBox()
    window.set_data(sand_box.box)
    plt.draw()
    plt.pause(5)
    plt.clf()

if __name__ == "__main__":
    main()



    

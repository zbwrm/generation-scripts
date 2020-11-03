import random
from PIL import Image
import numpy as np

def random_point(x_bound, y_bound):
    return (random.randint(0,x_bound), random.randint(0,y_bound))

def distance(p1, p2):
    return abs(int(np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)))

def generate(filename, x_size=500, y_size=500):

    red_point = random_point(x_size, y_size)
    green_point = random_point(x_size, y_size)
    blue_point = random_point(x_size, y_size)
    im = Image.new('RGB', (x_size, y_size))
    pixels = im.load()
    for x in range(x_size):
        for y in range(y_size):
            red = distance((x,y), red_point)
            green = distance((x,y), green_point)
            blue = distance((x,y), blue_point)
            pixels[x, y] = (red, green, blue)
    
    im.save(filename)


if __name__ == '__main__':
    for i in range(10):
        generate('images/test'+str(i)+'.png')

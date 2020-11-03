import random
from PIL import Image
import numpy as np

def random_point(x_bound, y_bound):
    return (random.randint(0,x_bound), random.randint(0,y_bound))

def distance(p1, p2):
    return abs(int(np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)))

def remap(val, valmax, mapmax):
    return (val / valmax) * mapmax

hsv2rgbfunc = lambda h,s,v,n: v - v*s*max(0, min((n+(h/60)%6),
                                                 4-(n+(h/60)%6),
                                                 1))
def hsv2rgb(h, s, v):
    r = int(hsv2rgbfunc(h,s,v,5)) * 255
    g = int(hsv2rgbfunc(h,s,v,3)) * 255
    b = int(hsv2rgbfunc(h,s,v,1)) * 255
    return r,g,b
    

def generate(filename, x_size=500, y_size=500, num_points=100):

    points = []
    for i in range(num_points):
        points.append(random_point(x_size,y_size))

    im = Image.new('RGB', (x_size, y_size))
    pixels = im.load()

    for x in range(x_size):
        for y in range(y_size):
            mindist = x_size
            minpoint = (0,0)
            for point in points:
                dist = distance((x,y), point)
                if dist < mindist:
                    mindist = dist
                    minpoint = point
            h = remap(minpoint[0], x_size, 360)
            s = remap(minpoint[1], y_size, 1)
            v = 1
            r, g, b = hsv2rgb(h, s, v)
            pixels[x, y] = (int(remap(minpoint[0],x_size,255)), int(remap(minpoint[1],y_size,255)), 255)

    im.save(filename)


if __name__ == '__main__':
    for i in range(3):
        generate('../images/voronoi'+str(i+1)+'.png', 1500, 500, 250)

import turtle

t = turtle.Turtle()

def triline(t, length, min_length):
    """
    Draws a triangle line of total length length using turtle t.
    """
    if (length <= min_length):
        t.fd(length)
        return 0
    triline(t, length/3, min_length)
    t.lt(60)
    triline(t, length/3, min_length)
    t.rt(120)
    triline(t, length/3, min_length)
    t.lt(60)
    triline(t, length/3, min_length)

def hex(t, sidelength, min_length):
    for i in range(6):
        triline(t,sidelength,min_length)
        t.lt(60)

t.speed(0)
t.ht()
hex(t, 150, 10)
turtle.done()

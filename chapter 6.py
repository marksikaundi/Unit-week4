# incremental development
import math
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is', dx)
    print('dy is', dy)

    return 0.0

# Next we compute the sum of squares of dx and dy:
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    print('dsquared is: ', dsquared)
    return 0.0

# Again, you would run the program at this stage and check the output (which should be25). Finally, you can use math.sqrt to compute and return the result:
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

def is_divisible(x, y): # boolean function
    if x % y == 0:
        return True
    else:
        return False
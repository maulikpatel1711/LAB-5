import math

class Point:
        def __init__(self):
                self.x = 0
                self.y = 0

def dist_btw_points(a,b):
        d1 = a.x - b.x
        d2 = a.y - b.y
        dist = math.sqrt(d1**2 + d2**2)
        return dist

x = Point()
y = Point()
print(x)
print(y)
print(x != y)

q0 = Point()
q0.x = 10
q0.y = 12
q1 = Point()
q1.x = 15
q1.y = 20

print('Distance')
print(dist_btw_points(q1,q0))
print('')


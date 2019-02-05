import Point

class Rectangle:
	def __init__(self):
		self.width = 0
		self.height = 0
		self.corner = 0


def find_center(r):
	c = Point()
	c.x = r.corner.x + r.width/2.0
	c.y = r.corner.y + r.height/2.0
	return c

def move_rectangle(a, dx, dy):
	a.corner.x += dx
	a.corner.y += dy

def modified_moverectangle(a, dx, dy):
	res = copy.deepcopy(a)
	move_rectangle(res, dx, dy)
	return res


rect = Rectangle()
rect.width = 50.0
rect.height = 70.0
rect.corner = Point()
rect.corner.x = 0.0
rect.corner.y = 0.0

print('Center')
c = find_center(rect)
print('(%g, %g)' % (c.x,c.y))
print('')

print('(%g, %g)' % (rect.corner.x, rect.corner.y))
print('move')
move_rectangle(rect, 100, 50)
print('(%g, %g)' % (rect.corner.x, rect.corner.y))
print('')

print('New move')
n_rect = modified_moverectangle(rect, 50, 100)
print('(%g, %g)' % (n_rect.corner.x, n_rect.corner.y))






	




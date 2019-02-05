class Time:
	def __init__(self):
		self.hour = 0
		self.minute = 0
		self.second = 0
	

def print_time(time):
	print("%.2d:%.2d:%.2d" %(time.hour,time.minute,time.second))




time = Time()
time.hour = 17
time.minute = 60
time.second = 30
print_time(time)


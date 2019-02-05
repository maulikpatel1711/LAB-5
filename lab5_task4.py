import Time

def is_after(t1,t2):
	return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


time = Time()
time.hour = 17
time.minute = 60

time.second = 30


time1 = Time()
time1.hour = 16
time1.minute = 45
time1.second = 59

print(is_after(time1,time))


import time

class TimerError(Exception):
	pass

class Timer:
	def __init__(self):
		self.start_time = None
		self.elapsed_time = -1
	
	def start(self):
		if self.start_time is not None:
			raise TimerError("Timer is already running.")
		self.start_time = time.perf_counter()
		self.elapsed_time = None
	
	def stop(self):
		if self.start_time is None:
			raise TimerError("Timer has not been started.")
		self.elapsed_time = time.perf_counter() - self.start_time
		self.start_time = None
	
	def elapsed(self):
		if self.elapsed_time is None:
			raise TimerError("Timer has not been stopped yet.")
		if self.elapsed_time == -1:
			raise TimerError("Timer has never been started.")
		return self.elapsed_time
		
	def __str__(self):	#print(<timer_object>) comes here
		return str(self.elapsed_time)
		
t = Timer()

n = int(input("Enter the value of n:- "))

t.start()

for i in range(1,n+1):
	for j in range(1,i+1):
		print(j, end=" ")
	print()

t.stop()
print("Time taken = ",t.elapsed())

# File Caching using lru_cache.

from functools import lru_cache 
import time 


# Function that computes Fibonacci 
# numbers without lru_cache 

def fib_without_cache(n): 
	if n < 2: 
		return n 
	return fib_without_cache(n-1) + fib_without_cache(n-2) 
	
# Execution start time 
begin = time.time() 
fib_without_cache(30) 

# Execution end time 
end = time.time() 

print("Time taken to execute the function without lru_cache is", end-begin) 

# Function that computes Fibonacci 
# numbers with lru_cache 
@lru_cache(maxsize = 128) 
def fib_with_cache(n): 
	if n < 2: 
		return n 
	return fib_with_cache(n-1) + fib_with_cache(n-2) 
	
begin = time.time() 
fib_with_cache(30) 
end = time.time() 

print("Time taken to execute the function with lru_cache is", end-begin) 


#---------------End------------------
@lru_cache(maxsize=2,typed=True)
def time_inter(n):
    time.sleep(n)
    return n

print("First Interval Starts.")
time_inter(2)
print("First Interval Over.")

time_inter(2)
print("Cached Interval 1 Done.")
time_inter(2)
print("Cached Interval 2 Done.")

print("Second Interval Starts.")
time_inter(3)
print("Second Interval Over.")

time_inter(3)
print("Cached Interval 3 Done.")
time_inter(3)
print("Cached Interval 4 Done.")

print("Third Interval Starts.")
time_inter(4)
print("Third Interval Over.")

time_inter(4)
print("Cached Interval 5 Done.")
time_inter(4)
print("Cached Interval 6 Done.")

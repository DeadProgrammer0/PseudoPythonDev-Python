# Time module 

import time

# Trying to find which is Fast While or For loop. Both are equally fast as they boil down into same level of machine level code.

initial = time.time()

print(initial)

for i in range(10):
    print("Hello")
print(f"For Loop runs in {time.time()-initial}")

initial2 = time.time()

k=0

while k<10:
    print("Hello")
    k += 1
print(f"While Loop runs in {time.time()-initial2}")


# Printing Local time.

local = time.asctime(time.localtime(time.time()))

print(local)

# Stoping Time in your programs.

# This command stops the time till given seconds.
time.sleep(3)
print(local)

time.sleep(3)
print(local)

time.sleep(3)
print(local)
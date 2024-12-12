import time

from sol1 import d04s01
from sol2 import d04s02

timer_start = time.time_ns()
sol1 = d04s01()
sol1_time = time.time_ns() - timer_start

timer_start = time.time_ns()
sol2 = d04s02()
sol2_time = time.time_ns() - timer_start


print(f'Answer 1: {sol1}, time taken: {sol1_time / 1000000} ms')
print(f'Answer 2: {sol2}, time taken: {sol2_time / 1000000} ms')

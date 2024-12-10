import time

from day06.sol01 import d06s01start
from day06.sol02 import d06s02start

start = time.time_ns()
s01 = d06s01start()
end = time.time_ns()
time_taken_ms_s01 = (end - start) / 1000000

start = time.time_ns()
s02 = d06s02start()
end = time.time_ns()
time_taken_ms_s02 = (end - start) / 1000000


print(f'answer 1: {s01}, time taken: {time_taken_ms_s01}ms')
print(f'answer 2: {s02}, time taken: {time_taken_ms_s02}ms')
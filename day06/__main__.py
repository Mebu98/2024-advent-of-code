import time

from day06.sol01 import d06s01start

start = time.time_ns()
s01 = d06s01start()
end = time.time_ns()
time_taken_ms = (end-start)/1000000
print(f'answer 1: {s01}, time taken: {time_taken_ms}ms')
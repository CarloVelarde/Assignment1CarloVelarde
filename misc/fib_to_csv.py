from functools import lru_cache
from functools import wraps
import time
import csv

def timer(func):
   """Print the runtime of a decorated function"""
   @wraps(func)
   def wrapper(*args, **kwargs):
      start = time.perf_counter()
      value = func(*args, **kwargs)
      end = time.perf_counter()
      run_time = end - start
      print(f"Finished in {run_time:.8f} secs: {func.__name__}({args[0]}) -> {value} ")
      execution_times.append((args[0], round(run_time,8)))
      return value
   return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
   if n == 0 or n == 1:
      return n
   else:
      return fib(n-1) + fib(n-2)
   

execution_times = []

if __name__ == "__main__":
   print(fib(100))
   for i in range(101):
      fib(i)
   
   with open('fib_runtime.csv', 'w', newline = '') as file:
      writer = csv.writer(file)
      writer.writerow(["Fib Num", "Runtime"])
      writer.writerows(execution_times)
from functools import lru_cache
from functools import wraps
import time

def timer(func):
   """Print the runtime of a decorated function"""
   @wraps(func)
   def wrapper(*args, **kwargs):
      start = time.perf_counter()
      value = func(*args, **kwargs)
      end = time.perf_counter()
      run_time = end - start
      print(f"Finished in {run_time:.8f} secs: {func.__name__}({args[0]}) -> {value} ")
      return value
   return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
   if n == 0 or n == 1:
      return n
   else:
      return fib(n-1) + fib(n-2)


if __name__ == "__main__":
   print(fib(50))
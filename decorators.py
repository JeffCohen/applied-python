# Examples: logging, timing, memoization

import time

def greet(name):
    print("Hello", name)

def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

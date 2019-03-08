import time
# Closures are an essential feature of Python.
# They provide the ability to capture the current stack
# and resume execution later.
#
# Common applications:
# - Use in callback functions
# - Delayed evaluation
# - Wrapper functions

def after(seconds, func):
    time.sleep(seconds)
    func()

def greeting():
    print(f'Hello, Guido')

after(3, greeting)

# 1. But what about...

# after(3, greeting("Jeff"))


# 2. Can we generalize it?
#    What if we had to wrap this function?
#
#    def add(x, y):
#      print(f'Adding {x} + {y} -> {x + y}')

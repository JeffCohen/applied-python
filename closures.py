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
    print(f'Hello, Luke Skywalker')

after(3, greeting)

# But what about...

# after(3, greeting("Jeff"))

# Can we generalize it?

# def add(x, y):
#     print(f'Adding {x} + {y} -> {x + y}')

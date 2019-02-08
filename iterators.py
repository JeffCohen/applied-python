# Custom Iterators
#

#
#   for x in obj:
#       # statements
#
#
# is actually...
#
#   _iter = obj.__iter__()  # Get iterator object
#
#   while True:
#     try:
#          x = _iter.__next__() # Get next item
#     except StopIteration:     # No more items
#          break
#     # statements
#
#

# Next: lab_3.py

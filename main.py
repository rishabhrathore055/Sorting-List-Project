# Using Python sorted() funtion to sorting a list:
# The sorted() function returns a sorted list of the specified iterable object.
# You can specify ascending or descending orders. Strings are sorted alphabetically, and numbers are sorted numerically. 
# You cannot sort a list that contains both string values as well as numeric values.

# Sorting numeric values:
a = (87,23,3,87,99,54,5,10,8,28)
x = sorted(a)
print(x)

# Sorting strings ascending order:
a = ("m", "k", "a", "c", "f", "o", "e", "v")
x = sorted(a)
print(x)

# Sorting strings descending order:
a =  ("m", "k", "a", "c", "f", "o", "e", "v")
x = sorted(a, reverse=True)
print(x)

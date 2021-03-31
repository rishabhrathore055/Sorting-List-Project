# Using Python sorted() funtion to sort a list:
# The sorted() function returns a sorted list of the specified iterable object.
# You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically. 
# You cannot sort a list that contains both string values and numeric values.

# Sort numeric:
a = (87,23,3,87,99,54,5,10,8,28)
x = sorted(a)
print(x)

# Sort strings ascending order:
a = ("m", "k", "a", "c", "f", "o", "e", "v")
x = sorted(a)
print(x)

# Sort strings descending order:
a =  ("m", "k", "a", "c", "f", "o", "e", "v")
x = sorted(a, reverse=True)
print(x)

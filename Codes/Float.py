# Float numbers

f = 1.2
print(f) #output: 1.2
print(type(f)) #output: <class 'float'>

f=123_42.222_013 #output: 12342.222013
print(f)

f=2e400
print(f) #output: inf


# Scienticific Numbers

f = 1e3
print(f) #output: 1000.0

f = 1e5
print(f) #output:100000.0

f = 3.4556789e2
print(f) #output:
print(type(f)) #output:345.56789

# Use the float() function to convert string, int to float.

f=float('5.5')
print(f) #output: 5.5

f=float('5')
print(f) #output: 5.0

f=float('     -5')
print(f) #output: -5.0

f=float('1e3')
print(f) #output: 1000.0

f=float('-Infinity')
print(f) #output: -inf

f=float('inf')
print(f)  #output: inf
print(type(f)) #output:<class 'float'>

import numpy

#DECLARING THE ARRAY
one_d_array = numpy.ndarray(shape=(5), dtype=int)

#PRINTING ARRAY FEATURES
print('SIZE OF THE ARRAY =',one_d_array.size)
print('DIMENSION =',one_d_array.ndim)

#TAKING ELEMENTS INSIDE THE ARRAY
n=one_d_array.size

print('Enter %d elemrnts inside the array',n)
for i in range(n):
    one_d_array[i]=int(input())

print(one_d_array)
import numpy

rows=int(input('Enter number of rows:-'))
columns=int(input('Enter number of columns:-'))

matrix = numpy.ndarray(shape=(rows,columns), dtype=int)

print('Size:-',matrix.size)
print('Shape',matrix.shape)
print('Dimensions', matrix.ndim)
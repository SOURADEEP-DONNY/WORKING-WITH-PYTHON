from numpy import *

arr=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])
print(arr)         #RETURNS THE ARRAY.
print(arr.ndim)    #RETURNS THE DIMENSION OF THE ARRAY.
print(arr.shape)   #RETURNS A TUPLE SHOWING NUMBER OF ROWS AND COLUMNS
print(arr.size)    #RETURNS TOTAL NUMBER OF ELEMENTS IN THE ARRAY.
print(diagonal(arr)) #RETURNS THE DIAGONAL ELEMENTS
print(arr.min()) #RETURNS THE MINIMUM ELEMENT FROM THE MATRIX
print(arr.max()) #RETURNS THE MAXIMUM ELEMENT FROM THE MATRIX

arr2=arr.flatten()
print(arr2)  #RETURNS A N-MATRIX IN 1 DIMENSION
print('\n')

arr=array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(6,2))


m1=matrix('1 2 3; 4 5 6; 7 8 9')
m2=matrix('1 2 3; 4 5 6; 7 8 9')
m3=m1+m2
print(m3)

m1=matrix('1 0; 0 1')
m2=matrix('1 3; 6 5')
m3=m1*m2
print(m3)











#CREATING A CLASS AND CALCULATING AREA AND PERIMETER OF TWO RECTANGLES.

class Rectangle:
    pass

#CREATING TWO OBJECTS.

rect1=Rectangle()
rect2=Rectangle()

rect1.length=int(input('\nEnter length for rectangle 1:='))
rect2.length=int(input('\nEnter length for rectangle 2:='))


rect1.breadth=int(input('\nEnter breadth for rectangle 1:-'))
rect2.breadth=int(input('\nEnter breadth for rectangle 2:-'))

print('The area of rectangle 1 is',rect1.length * rect1.breadth)
print('The area of rectangle 2 is',rect2.length * rect2.breadth)

print('\n')

print('The perimeter of rectangle 1 is',2*(rect1.length + rect1.breadth))
print('The perimeter of rectangle 2 is',2*(rect2.length + rect2.breadth))


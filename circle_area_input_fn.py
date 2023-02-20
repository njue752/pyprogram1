#function to find the area of a circle with input from the user
def Area(Radius):
    CircleArea=3.142*Radius*Radius
    return CircleArea
Radius=int(input("Enter the radius of the circle"))
A=Area(Radius)
print("Area of the circle is",A)


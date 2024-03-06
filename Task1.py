#Task 1: Calculate Area with Conditions

width = int(input("Enter width:"))
length = int(input("Enter length:"))

def calculate_area(a,b):
    if a==b:
        area ="This is a square"
    else:
        area = b*a
    return area

print(calculate_area(width,length))

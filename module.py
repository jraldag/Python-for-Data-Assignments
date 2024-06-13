def printName(name):
    return "Hello Mr/Ms " + name + "...we've been waiting for you!"


def calc_sq_footage():
    length = int(input("Enter the length of the house in feet. "))
    width = int(input("Enter the width of the house in feet. "))
    sq_footage = length * width
    print("The house is", sq_footage, "square feet.")

    
def calc_circle_circumference():
    diameter = int(input("Enter the diameter of the circle in feet. "))
    import math
    circle_circumference = diameter * math.pi
    print("The circle's circumference is", circle_circumference, "feet.")
    
    
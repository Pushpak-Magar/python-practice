import math
def square_cube():
    square=int(input("enter the square number:"))
    cube=int(input("enter the cube number:"))
    num1=math.sqrt(square)  #calculates square of number
    num2=math.cbrt(cube)   #calculates cube of number

    print(f"square root of {square} is {num1} ")
    print(f"cube root of {cube} is {num2} ")
 

square_cube()
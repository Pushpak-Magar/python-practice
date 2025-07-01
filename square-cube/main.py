import math
def square():
    square_num=int(input("enter the square value:"))
    
    num1= math.sqrt(square_num)  #calculates square of number
  

    print(f"number of {square_num} is {num1} ")
 


square()

def cube():
    cube_num=int(input("enter the cube value:"))

    num2= math.cbrt(cube_num)   #calculates cube of number
    print(f"cube of {cube_num} is {num2}")

cube()



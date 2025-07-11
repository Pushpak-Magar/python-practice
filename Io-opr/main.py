#Input Ouput functionality and use 

# input is mostly given by an external user and the input value is assigned a variable

# Create a program that receives that user's name and age, then calculates and prints how old they will be in 10 years.

# The output should be in the format: "In 10 years, [name] will be [age] years old."

# You will need to:

# Use input() to get the user's name and age.
# Store the inputs in variables.
# Convert the age to an integer and add 10 to it.
# Print the result using an f-string.

name_of_user = input()
age = int(input())

print(f"In 10 years , {name_of_user} will be  {age + 10 } years old  ")


def str_opr():
    str1 = input()
    str2 = input()
    
    print(f"{str1 + "" + str2}")
    
str_opr()

def casting_opr():
    
    var1 = int(input())
    var2 = float(input())
    
    print(f"{var1 + var2}")
    
casting_opr()






# You are given a code which gets as input a number that indicates the wind speed and stores it in a variable named wind.

# Note: we will learn in next lessons how to get input from the user, currently just don't touch the first line.

 

# Your task is to initialize variable status based on the conditions:

# "Calm" if wind is smaller than 8,
# "Breeze" if wind is between 8 and 31 (including 8 and 31).
# "Gale" if wind is between 32 and 63 (including 32 and 63)
# "Storm" otherwise

wind = int(input()) # Don't change this line
status = "unset"
# Type your code below
if wind < 8:
    status="calm"

elif wind >= 8 and wind <= 31 :
    status="breeze"

elif wind >=32 and wind <=63 :
    status="Gale"

else :
    status="storm"
    

# Don't change the line below
print(f"status = {status}")
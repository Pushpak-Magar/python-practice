# Create a program for a game character creation system. The requirements are:

# The character's level determines what weapons they can use:

# Level 1-5: Can only use Basic weapons
# Level 6-10: Can use Advanced weapons if they completed training
# Level 11+: Can use any weapon
# Set level_message variable with these messages based on the conditions:

# If level 1-5: Basic weapons only
# If level 6-10 and no training: Need weapon training first
# If level 6-10 and has training: Access to advanced weapons granted
# If level 11+: Access to all weapons granted
# If level is 0 or negative: Invalid level

level = int(input())  
has_training = True
level_message = "None"  

if level <= 0:
    level_message = "Invalid level"
elif level <= 5:
    level_message = "Basic weapons only"
elif level <= 10:
    if has_training:
        level_message = "Access to advanced weapons granted"
    else:
        level_message = "Need weapon training first"
else:
    level_message = "Access to all weapons granted"


print(level_message)


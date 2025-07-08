# You're helping a pet shop create a system to determine if they can sell a pet to a customer.

# initialize the following variables:

# has_license with the value True
# has_space with the value True
# has_experience with the value False
# Write the following logical expressions to determine if:

# can_sell_regular_pet: Customer needs EITHER a license OR experience, AND must have space
# can_sell_exotic_pet: Customer needs BOTH a license AND experience, AND must have space
# cannot_sell_any_pet: Customer has NO license AND NO experience, OR has NO space

# Initialize variables

has_license=True
has_space=True
has_experience=False

# Calculate conditions
can_sell_regular_pet = has_license or has_experience and has_space
can_sell_exotic_pet =  has_license and has_experience and has_experience
cannot_sell_any_pet =  ( not has_experience) and ( not has_license) or (not has_space)

# Don't delete the lines below
print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)
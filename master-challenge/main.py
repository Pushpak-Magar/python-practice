# Challenge
# You're helping a transportation company create a system to determine if a person can drive certain vehicles.

# Initialize the following variables:

# has_license with the value True
# has_experience with the value False
# has_clean_record with the value True
# Write the following logical expressions to determine if:

# can_drive_car: Person needs a license AND a clean record
# can_drive_truck: Person needs a license AND experience AND a clean record
# cannot_drive_any: Person has NO license OR NO clean record


has_license = True
has_experience =  False
has_clean_record = True

can_drive_car = has_license and has_clean_record
can_drive_truck = has_license and has_experience and has_clean_record
cannot_drive_any = (not has_license) or (not has_clean_record)

print(" the Driver with license and clean record can drive a  Car: " , can_drive_car)
print(" the Driver with  license and experience and clean record can drive a Truck: ", can_drive_truck)
print("the driver with no license or no clean record can drive any: ",cannot_drive_any )


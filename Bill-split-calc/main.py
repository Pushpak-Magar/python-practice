print("Bill Split Calculator")

bill_amount = float(input())
tip_percentage = float(input())
num_of_people = int(input())

tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount

print(f"Total (including tip): ${total_amount}")

amount_per_person = total_amount / num_of_people

print(f"Each person pays: ${amount_per_person}")





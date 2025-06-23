even = [2,4,6,8]
odd = [1,3,5,7]
all_numbers=[]
for i in range(len(even)) :
    all_numbers.append(odd[i] + even[i])
print(all_numbers)
num = input("Enter numbers: ")
num_list = num.split()

unique_numbers = set(num_list)
count = len(unique_numbers)

print("count unique numbers:", count)

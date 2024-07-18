with open('input.txt', 'r') as file:
    numbers = list(map(int, file.readline().split()))

product = 1
for number in numbers:
    product *= number

with open('output.txt', 'w') as file:
    file.write(str(product))

with open('input.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

sorted_numbers = sorted(numbers, key=lambda x: sum(int(digit) for digit in str(x)))


with open('output.txt', 'w') as file:
    for number in sorted_numbers:
        file.write(str(number) + '\n')

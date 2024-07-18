import numpy as np


def run_length_encoding(x):

    values = []
    counts = []

    current_value = x[0]
    current_count = 1

    for i in range(1, len(x)):
        if x[i] == current_value:
            current_count += 1
        else:
            values.append(current_value)
            counts.append(current_count)

            current_value = x[i]
            current_count = 1

    values.append(current_value)
    counts.append(current_count)

    return np.array(values), np.array(counts)


input_numbers = list(map(int, input("Enter numbers: ").split()))

values, counts = run_length_encoding(np.array(input_numbers))

print("Numbers:", values)
print("Repeat:", counts)

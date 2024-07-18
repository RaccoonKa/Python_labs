x = list(map(int, input("Enter elements: ").split()))
max_element = None

for i in range(1, len(x)):
    if x[i-1] == 0:
        if max_element is None or x[i] > max_element:
            max_element = x[i]

if max_element is not None:
    print(f"Max: {max_element}")
else:
    print("ERROR")

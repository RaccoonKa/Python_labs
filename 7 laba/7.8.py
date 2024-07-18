lst = [0, 1, 2, 0, 0, 4, 0, 6, 9]
non_zero = [index for index, element in enumerate(lst) if element != 0]
print("Index:", non_zero)

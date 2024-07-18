set1 = set(map(int, input("Enter elements (1): ").split()))
set2 = set(map(int, input("Enter elements (2): ").split()))

if set1.issubset(set2) and set1 != set2:
    print(True)
else:
    print(False)

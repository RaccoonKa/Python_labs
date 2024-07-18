import numpy as np

arr = np.random.normal(size=(10, 4))
min_val = np.min(arr)
max_val = np.max(arr)
mean_val = np.mean(arr)
std_val = np.std(arr)
first_5_rows = arr[:5]

print("Min:", min_val)
print("Max:", max_val)
print("Middle:", mean_val)
print("Deviation:", std_val)
print("\nFirst 5 strings:")
print(first_5_rows)

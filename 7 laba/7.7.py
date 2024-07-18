import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

unique_values, counts = np.unique(iris[:, 4], return_counts=True)

for value, count in zip(unique_values, counts):
    print(f"{value} - {count}")

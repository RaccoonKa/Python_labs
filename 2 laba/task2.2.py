n = int(input('Enter numb of size: '))
arr = list()
arr.append('  * ')
arr.append(' * *')
for i in range(1, n):
    for j in range(2 ** i):
        arr.append(arr[j] + arr[j])
    for jj in range(2 ** i):
        arr[jj] = ' ' * (2 ** i) + arr[jj] + ' ' * (2 ** i)

for h in arr:
    print(h)

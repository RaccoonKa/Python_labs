n = int(input("enter size of triangle: "))
triangle = []
for i in range(n):
    row = [1] * (i+1)
    triangle.append(row)
    for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
for row in triangle:
    print(' '.join(map(str, row)).center(n*2))

def print_matrix(matrix):
    for row in matrix:
        print(row)


def are_columns_linearly_dependent(matrix):
    column1 = [row[0] for row in matrix]
    column2 = [row[1] for row in matrix]
    column3 = [row[2] for row in matrix]

    det = column1[0] * (column2[1] * column3[2] - column2[2] * column3[1]) - column1[1] * (
                column2[0] * column3[2] - column2[2] * column3[0]) + column1[2] * (
                      column2[0] * column3[1] - column2[1] * column3[0])

    if det == 0:
        return True
    else:
        return False


matrix = []


print("Введите числа для заполнения матрицы 3x3:")
for _ in range(3):
    row = [int(num) for num in input().split()]
    matrix.append(row)

print("Матрица:")
print_matrix(matrix)

result = are_columns_linearly_dependent(matrix)

if result:
    print("\nСтолбцы матрицы линейно зависимы.", sep='\n')
else:
    print("Столбцы матрицы линейно не зависимы.", sep='\n')

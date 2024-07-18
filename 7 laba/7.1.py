def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix


def get_matrix_stats(matrix):
    total_sum = sum(sum(row) for row in matrix)
    flat_matrix = [elem for row in matrix for elem in row]
    max_element = max(flat_matrix)
    min_element = min(flat_matrix)
    return total_sum, max_element, min_element


filename = "matrix.txt"
matrix = read_matrix_from_file(filename)
total_sum, max_element, min_element = get_matrix_stats(matrix)

print(f"Sum: {total_sum}")
print(f"Max: {max_element}")
print(f"Min: {min_element}")

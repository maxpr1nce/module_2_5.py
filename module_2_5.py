def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        row = [value] * m
        matrix.append(row)
    return matrix

# Пример использования
result = get_matrix(3, 4, 10)
print(result)
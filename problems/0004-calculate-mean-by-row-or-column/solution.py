def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    means = []
    if mode == 'row':
        for i in range(num_rows):
            row_sum = 0
            for j in range(num_cols):
                row_sum += matrix[i][j]
            means.append(row_sum / num_cols)
    elif mode == 'column':
        for j in range(num_cols):
            col_sum = 0
            for i in range(num_rows):
                col_sum += matrix[i][j]
            means.append(col_sum / num_rows)
            
    return means
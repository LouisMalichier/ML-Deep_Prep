def calculate_matrix_mean(matrix, mode="row"):
    mean_list = []
    if mode == "row":
        for row in matrix:
            mean_list.append(sum(row) / len(row))
        return mean_list

    elif mode == "column":
        num_cols = len(matrix[0])
        for j in range(num_cols):
            mean = 0
            for i in range(len(matrix)):
                mean += matrix[i][j]   
            mean_list.append(mean / len(matrix))
        return mean_list
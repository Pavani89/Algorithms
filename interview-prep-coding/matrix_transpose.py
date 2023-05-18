'''
Write a Python function that takes a matrix (list of lists) as input and returns the transpose of the matrix.
'''

def matrix_transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transposed = [[matrix[j][i] for j in range(rows)] for i in range(columns)]
    return transposed

# Test the function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = matrix_transpose(matrix)
print(result)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

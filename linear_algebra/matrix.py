'''

matrix = [[0 for _ in range(3)] for _ in range(3)]

 matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

'''

def print_matrix(matrix: list[list[int]]):
    '''
    print matrix
    '''
    print("[")
    for row in matrix:
        print(f"    {row},")
    print("]")


def create_identity_matrix(size: int) -> list[list[int]]: 
    '''
    create identity matrix of given size
    '''
    matrix = []
    for i in range(size):
        row = []

        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        
        matrix.append(row)
    
    return matrix

def matrix_addition(matrixA: list[list[int]], matrixB: list[list[int]]) -> list[list[int]]:
    '''
    add to matrices
    '''

    if len(matrixA) != len(matrixB) or len(matrixA[0]) != len(matrixB[0]):
        raise ValueError("Matrices must have the same dimensions")

    rows = len(matrixA)
    cols = len(matrixA[0])

    res = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            res[i][j] = matrixA[i][j] + matrixB[i][j]
    
    return res 


if __name__ == '__main__':

    # --- Test creation and print ---
    print("--- Identity Matrix Test ---")
    identity_4x4 = create_identity_matrix(4)
    print_matrix(identity_4x4)
    print("\n" + "="*30 + "\n") # Separator

    # --- Test addition ---
    print("--- Matrix Addition Test ---")
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    print("Matrix A:")
    print_matrix(matrix1)
    
    print("Matrix B:")
    print_matrix(matrix2)

    # Perform addition and store the result
    sum_matrix = matrix_addition(matrix1, matrix2)

    print("Result of A + B:")
    print_matrix(sum_matrix)


    


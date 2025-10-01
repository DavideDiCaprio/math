'''
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

if __name__ == '__main__':
    identity_4x4 = create_identity_matrix(4)
    
    print_matrix(identity_4x4)
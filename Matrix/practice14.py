                                                #Hard
'''Given an integer k and matrix mat . Left rotate the matrix k times.

Examples:

Input: k=1, mat=[[1,2,3],[4,5,6],[7,8,9]]
Output:
2 3 1
5 6 4
8 9 7
Explanation: Left rotating the matrix once gives this result.'''
def func(matrix,k):
    row=len(matrix)
    column=len(matrix[0])

    k=k%len(matrix)

    if k==0:
        return matrix

    rotated_matrix=[[0]*column for _ in range(row)]

    for i in range(row):
        for j in range(column):

            rotated_matrix[i][(j - k) % column] = matrix[i][j]
    return rotated_matrix


k = 2

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = func(mat, k)

for row in result:
    print(" ".join(map(str,row)))


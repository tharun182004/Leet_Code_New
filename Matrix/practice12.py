                                                    #Easy
'''
Given a square matrix of size N x N. The task is to rotate it by 90 degrees in anti-clockwise
direction without using any extra space. 

Example 1:

Input:
N = 3 
matrix[][] = {{1, 2, 3},
              {4, 5, 6}
              {7, 8, 9}}
Output: 
Rotated Matrix:
3 6 9
2 5 8
1 4 7
'''

class Matrix:
    def anticlock(self,matrix):
        n=len(matrix)


        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(n):
            for j in range(n//2):
                matrix[j][i],matrix[n-j-1][i]=matrix[n-j-1][i],matrix[j][i]

        return matrix



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
sol=Matrix()
sol.anticlock(matrix)

for row in matrix:
    print(" ".join(map(str,row)))

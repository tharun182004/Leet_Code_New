'''
Given an n x m integer matrix 'matrix', your task is to return the elements
of the matrix in a specific diagonal order. The traversal of the matrix should
start from the top-left element, move to the right across the top row, and
then continue from the leftmost element of each subsequent row, zigzagging
through the diagonals. If a diagonal starts at an even index, the elements
should be added in collected order; if the diagonal starts at an odd index,
the elements should be added in reverse order.

EXAMPLE:
input:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
output:
[1, 2, 4, 7, 5, 3, 6, 8, 9]
'''

class Solution:
    def func(self,matrix):

        if not matrix or not matrix[0]:
            return []

        n=len(matrix)
        result=[]

        for row in range(n):
            i,j=0,row
            while i<n and j>=0:
                result.append(matrix[i][j])
                i+=1
                j-=1

        for col in range(1,n):
            j=n-1
            i=col
            while i<n and j>=0:
                result.append(matrix[i][j])
                i+=1
                j-=1
        return result





n = 3
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sol=Solution()
print(sol.func(mat))
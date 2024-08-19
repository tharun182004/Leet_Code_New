                                                        #EASY
'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Input: matrix = [
[0,1,2,0]
[3,4,5,2]
[1,3,1,5]
]
Output: [
[0,0,0,0]
[0,4,5,0]
[0,3,1,0]
]
'''

class Solution:
    def func(self,matrix):

        m=len(matrix)
        n=len(matrix[0])

        row_arr=set()
        col_arr=set()

        if not matrix:
            return []

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row_arr.add(i)
                    col_arr.add(j)


        for i in row_arr:
            for j in range(n):
                matrix[i][j]=0

        for k in col_arr:
            for l in range(m):
                matrix[l][k]=0

        return matrix


matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
sol=Solution()
a=sol.func(matrix)


for i in a:
    print(" ".join(map(str,i)))




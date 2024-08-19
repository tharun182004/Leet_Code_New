                                                      #Easy
'''
Given a 2D binary matrix(1-based indexed) a of dimensions nxm , determine the row
that contains the minimum number of 1's.
Note: The matrix contains only 1's and 0's. Also, if two or more rows contain the
minimum number of 1's, the answer is the lowest of those indices.

Example 1:
Input:
n = 4,m = 4
a = [[1, 1, 1, 1],
     [1, 1, 0, 0], 
     [0, 0, 1, 1],
     [1, 1, 1, 1]]
Output:
2
Explanation:
Rows 2 and 3 contain the minimum number 
of 1's(2 each).Since,row 2 is less than row 3.
Thus, the answer is 2.
'''


class Solution:
    def min_one(self,matrix):
        count_sum=float('inf')
        row_index=-1
        n=len(matrix)

        for i in range(n):
            count=sum(matrix[i])
            if count<count_sum or (count==count_sum and i<row_index):
                count_sum=count
                row_index=i+1

        return row_index


a = [
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
]
sol=Solution()
print(sol.min_one(a))
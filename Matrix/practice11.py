                                              #MATRIX
                                              #EASY
'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''


class Solution(object):
    def searchMatrix(self, matrix, target):

        m=len(matrix)
        n=len(matrix[0])

        low=0
        high=(m*n)-1

        while low<=high:
            mid=(low+high)//2
            row=mid//n
            column=mid%n
            if matrix[row][column]==target:
                return True
            elif matrix[row][column]<target:
                low=mid+1
            else:
                high=mid-1
        return False

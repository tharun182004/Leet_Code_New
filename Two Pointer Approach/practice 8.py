                                                    #EASY
'''
Given an array Arr[] that contains N integers (may be positive, negative or zero).
Find the product of the maximum product subarray.

Example 1:
Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}
Output: 180
Explanation: Subarray with maximum product
is [6, -3, -10] which gives product as 180.
'''


class Solution:
    def maxProduct(self, arr, n):

        n = len(arr)
        prefix = 1
        suffix = 1
        maxi = -float('inf')

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix *= arr[i]
            suffix *= arr[n - 1 - i]
            maxi = max(maxi, max(prefix, suffix))
        return maxi


arr = [6, -3, -10, 0, 2]
solution=Solution()
print(solution.maxProduct(arr,len(arr)))
                                      #Medium
'''
Given an array Arr[] of N integers. 
Find the contiguous sub-array(containing at least one number),
which has the maximum sum and return its sum.

Example 1:
Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
'''



class Solution:
    def func(self,arr):
        max_el=-float('inf')
        sum=0
        for i in range(len(arr)):
            sum += arr[i]
            if sum>max_el:
                max_el=sum
            if sum<0:
                sum=0
        return max_el

sol=Solution()
arr=[-2,-3,4,-1,-2,1,5,-3]
print(sol.func(arr))


'''
class Solution:
    def func(self, arr):                    [-2,-3,4,-1,-2,1,5,-3]
        max_el = -float('inf')
        sum = 0

        for i in range(len(arr)):
            sum += arr[i]
            if sum > max_el:
                max_el = sum
            if sum < 0:
                sum = 0

        return max_el
'''
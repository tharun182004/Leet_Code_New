'''
Minimum Number in a sorted rotated array

Given an array of distinct elements which was initially sorted.
This array may be rotated at some unknown point. The task is to
find the minimum element in the given sorted and rotated array.

Example 1:

Input:
N = 10
arr[] = {2,3,4,5,6,7,8,9,10,1}
Output: 1
Explanation: The array is rotated
once anti-clockwise. So minimum
element is at last index (n-1)
which is 1.
'''


def min_ele(arr):
    low,high=0,len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]>arr[high]:
            low=mid+1
        else:
            high=mid
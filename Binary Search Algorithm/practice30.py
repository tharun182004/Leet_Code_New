'''
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


def func(arr):
    low=0
    high=len(arr)-1
    min_val=float('inf')
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=min_val:
            min_val=arr[mid]
        if arr[mid]>arr[high]:
            low=mid+1
        else:
            high=mid-1
    return min_val

arr=[3,4,5,1,2]
print(func((arr)))
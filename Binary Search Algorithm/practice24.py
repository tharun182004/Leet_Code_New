                                                      #Easy
'''
Given an array arr[] sorted in ascending order of size N and an integer K. Check if K is present in the array or not.

Example 1:
Input:
N = 5, K = 6
arr[] = {1,2,3,4,6}
Output: 1
Exlpanation: Since, 6 is present in 
the array at index 4 (0-based indexing),
output is 1.
'''


def func(arr,k):
    st=0
    en=len(arr)-1
    mid=len(arr)//2

    while st<=en:
        if arr[mid]==k:
            return 1

        elif k>arr[mid]:
            st = mid+1
            mid = (st + en) // 2
        else:
            en=mid-1
            mid=(st+en)//2

    return -1


arr=[1,2,3,4,6]
print(func(arr,6))
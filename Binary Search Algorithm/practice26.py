                                            #Medium
'''Given a sorted array arr containing n elements with possibly some duplicate, 
the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.


Example 1:

Input:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  
2 5
Explanation: 
First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5.'''


def find_first(arr,key):
    st=0
    en=len(arr)-1
    min_index=-1
    while st<=en:
        mid=(st+en)//2
        if arr[mid]==key:
            min_index=mid
            en=mid-1
        elif arr[mid]>key:
            en=mid-1
        else:
            st=mid+1

    return min_index

def find_last(arr,key):
    st = 0
    en = len(arr)-1
    max_index = -1
    while st <= en:
        mid = (st + en) // 2
        if arr[mid] == key:
            max_index = mid
            st = mid + 1
        elif arr[mid] > key:
            en = mid - 1
        else:
            st = mid + 1

    return max_index

def find_first_last(arr,key):
    first=find_first(arr,key)
    last=find_last(arr,key)
    return first,last

arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
key = 5
print(find_first_last(arr,key))
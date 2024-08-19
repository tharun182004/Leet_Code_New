'''PROBLEM STATEMENT:
Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K.
The task is to find the element that would be at the kth position of the final sorted array.'''

def find_kth_element(arr1,arr2,k):
    if len(arr1)>len(arr2):
        return find_kth_element(arr2,arr1,k)
    low,high=0,len(arr1)
    while low<=high:
        mid1=(low+high)//2
        mid2=k-mid1

        l1=arr1[mid1-1] if mid1>0else float('-inf')
        l2=arr2[mid2-1] if mid2>0 else float('-inf')
        r1=arr1[mid1]   if mid1<len(arr1) else float('inf')
        r2=arr2[mid2]   if mid2<len(arr2) else float('inf')


        if l1>r2:
            high=mid1-1
        elif l2>r1:
            low=mid1+1
        else:
            return max(l1,l2)
    return -1


arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
print(find_kth_element(arr1, arr2, k))  # Output: 6




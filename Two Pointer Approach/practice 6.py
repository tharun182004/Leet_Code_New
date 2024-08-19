                                                        #MEDIUM
'''
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted.
If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Example 1:
Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3)
'''
def merge_split(arr):          #[12, 11, 13, 5, 6, 7]
    n=len(arr)
    if n>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]

        left_inversions = merge_split(left_half)
        right_inversions = merge_split(right_half)

        merge_inversions = merge(arr, left_half, right_half)

        return left_inversions + right_inversions + merge_inversions
    else:
        return 0
def merge(arr,left_half,right_half):
    count=0
    i,j,k=0,0,0
    while i<len(left_half) and j<len(right_half):      #[2,3,5]   [1,4]
        if left_half[i]<=right_half[j]:

            arr[k]=left_half[i]
            i+=1
        else:

            arr[k]=right_half[j]
            count += ((len(left_half)-1)-i)+1
            j+=1
        k+=1

    while i<len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j<len(right_half):
        arr[k] = right_half[j]
        j += 1
        k +=1
    return count

arr= [12, 11, 13, 5, 6, 7]

result=merge_split(arr)
print(result)







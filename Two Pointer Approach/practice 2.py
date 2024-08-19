'''
Given an array containing N integers and an integer K.,
Your task is to find the length of the longest Sub-Array with the
sum of the elements equal to the given value K.
'''

#CHALLENGING
def longest_subarray_with_sum_k(arr,k):
    dict={}
    sum=0
    max_len=0
    for i in range(len(arr)):
        sum+=arr[i]

        if sum==k:
            max_len=i+1
        if sum-k in dict:
            max_len=max(max_len,i-dict[sum-k])
        if sum not in dict:
            dict[sum]=i

    return max_len

A = [10, 5, 2, 7, 1, 9]
K = 15
print(longest_subarray_with_sum_k(A, K))


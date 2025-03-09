                                                   #EASY
'''Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.'''

def func(arr):
    #One Method of solving
    '''n=len(arr)
    init_arr=[0]*(n+1)
    print(init_arr)
    for i in range(n):
        b=arr[i]
        init_arr[b]+=1

    return init_arr
'''
    #Another method of solving
    n=len(arr)
    total_sum=(n*(n+1))//2
    arr_sum=sum(arr)
    return total_sum-arr_sum



arr=[3,0,1]
print(func(arr))
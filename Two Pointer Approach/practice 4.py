#QUITE SIMPLE, BUT TRICKY
'''
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3
'''


class Solution(object):
    def majorityElement(self, nums):
        count=0
        max_el=0
        n=len(nums)
        for i in range(n):
            if count==0:
                max_el=nums[i]
                count+=1
            else:
                if nums[i]==max_el:
                    count+=1
                else:
                    count-=1
        count=0
        for i in range(n):
            if nums[i]==max_el:
                count+=1
        if count>n//2:
            return max_el
        else:
            return None


#TRAPPING THE RAIN WATER
'''
Given an array arr[] of N non-negative integers representing the height of blocks.
If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.
'''
class Solution:
    def func(self,arr):
        left=0
        right=len(arr)-1
        left_max=0
        right_max=0
        water_trapped=0

        while left<=right:
            if arr[left]<=arr[right]:
                if arr[left]<left_max:
                    water_trapped+=left_max-arr[left]
                else:
                    left_max=arr[left]
                left+=1
            else:
                if right>right_max:
                    right_max=right
                else:
                    water_trapped=right_max-arr[right]
                right-=1

        return water_trapped

arr = [3, 0, 0, 2, 0, 4]
ans=Solution()
print(ans.func(arr))

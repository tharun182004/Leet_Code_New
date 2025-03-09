# EASY
'''
Given a positive integer, N. Find the factorial of N.

 Example 1:
Input:
N = 5
Output:
120
Explanation:
5*4*3*2*1 = 120
'''


class Solution:
    def func(self, n):
        if n >= 1:
            return n * self.func(n - 1)
        else:
            return 1

        self.func(n)


sum = 1
sol = Solution()
print(sol.func(5))







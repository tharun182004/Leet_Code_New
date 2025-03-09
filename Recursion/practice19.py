'''
Given a positive integer n, find the nth fibonacci number.
Since the answer can be very large, return the answer modulo 1000000007.

Note: for the reference of this question take first fibonacci number to be 1.
Example 1:
Input:
n = 2
Output:
1
Explanation:
1 is the 2nd number of fibonacci series.
'''

class Solution:
    def nthFibonacci(self, n):
        MOD = 1000000007
        if n <= 1:
            return 1
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, (a + b) % MOD
        return b

# Creating an instance of the Solution class
sol = Solution()

# Test case
test_cases = [2, 10, 50, 100, 14521]
for n in test_cases:
    print(f"nthFibonacci({n}) = {sol.nthFibonacci(n)}")

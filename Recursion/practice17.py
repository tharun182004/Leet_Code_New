                                         #EASY
'''
Print numbers from 1 to N without the help of loops.

Example 1:

Input:
N = 10
Output: 1 2 3 4 5 6 7 8 9 10
'''
def func(n):
    def recur(current,n):
        if current>n:
            return
        print(current,end=' ')
        recur(current+1,n)
    recur(1,n)

n=10
func(n)
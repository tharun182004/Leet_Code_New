class Solution:
    def func(self,n,p):
        mod=1000000007
        res=1
        if p==0:
            return 1
        elif p==1:
            return n
        while p>0:
            if p%2==1:
                res=(res*n)%mod
                p=p-1
            else:
                n=(n*n)%mod
                p=p//2
        return res


sol=Solution()
print(sol.func(2,10))

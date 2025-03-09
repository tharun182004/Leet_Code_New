#Find Square Root
def func(x):
    st,en=1,x
    ans=0
    while st<=en:
        mid=(st+en)//2
        if (mid*mid)<=x:
            ans=mid
            st=mid+1
        else:
            en=mid-1
    return en

x=35
print(func(x))
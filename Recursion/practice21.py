def func(n):
    def function(n, current, decrease, result):
        result.append(current)
        if current==n and decrease==False:
            return result
        if decrease:
            if current-5>0:
                function(n, current - 5, True, result)
            else:
                function(n, current-5,False, result)
        else:
            function(n, current+5,False,result)
        return result
    return function(n,n,True,[])
n=7
print(func(n))
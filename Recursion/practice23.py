#Pascal Triangle                                 #Medium


class Solution:

    def nthRowOfPascalTriangle(self, n):
        # code here
        mod = 10 ** 9 + 7

        result = 1
        row = [result]

        for i in range(1, n):
            result = (result * (n - i)) % mod
            inv_i = pow(i, mod - 2, mod)  # Modular inverse of i under mod
            result = (result * inv_i) % mod
            row.append(result)

        return row

'''def single_number(row,col):

    row-=1
    col-=1

    result=1
    for i in range(col):
        result=result*(row-i)
        result=result//(i+1)
    return result

def row_print(row):

    result=1
    print(result,end=' ')
    for i in range(1,row):
        result=result*(row-i)
        result=result//i
        print(result, end=' ')'''




row=5
col=4
#print(single_number(row,col))
sol=Solution()
print(sol.nthRowOfPascalTriangle(row))



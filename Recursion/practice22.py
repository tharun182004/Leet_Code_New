def func(s):
    if not s:
        return -1

    index=0

    if s[0]=='-':
        return "Not valid"
    else:
        result=0

        for i in range(index,len(s)):
            digit_found=ord(s[i])-ord('0')
            result=(result*10)+digit_found
        return result
    



s='123'
print(func(s))

def func(arr,key):              #[0,1,2,3,4,5,6,7]
    st=0                        #[1,2,2,3,4,5,6,6]
    en=len(arr)-1
    floor_index=-1
    while st<=en:
        mid=(st+en)//2
        if arr[mid]<=key:
            floor_index=mid
            st=mid+1
        else:
            en=mid-1
    if floor_index!=-1:
        return floor_index
    else:
        return "Not Found"
#   [0,1,2,3,4,5,6]
arr=[1,2,3,4,6,7,8]
key=5
print(func(arr,key))


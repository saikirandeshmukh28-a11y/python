def binarysearch(l,v):
    found=False
    low=0
    high=len(l) - 1
    while low<=high:
        if low==high:
            if l[low]==v:
                found=True
            break
        else:
            mid=(low+high)//2
            if l[mid]==v:
                found=True
                break
            elif l[mid]>v:
                high=mid-1
            else:
                low=mid+1
    return found    

print(binarysearch([1,2,3,4,5],3))
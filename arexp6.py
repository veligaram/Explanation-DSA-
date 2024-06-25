#search ,insert,delete in sorted array

def binsearch(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1        
def inserting(arr,target):
    if len(arr)==0:
        return [target]
    pos=0
    while pos<len(arr) and arr[pos]<target:
        pos+=1
    arr=arr[:pos]+[target]+arr[pos+1:]
    return arr
def deleting(arr,target):
    pos=binsearch(arr,target)
    if pos==-1:
        return arr
    arr=arr[:pos]+arr[pos+1:]
    return arr
print(binsearch([2,3,4,5,6],3))
print(inserting([2,4,5,6],3))
print(deleting([2,3,4,5,6],3))

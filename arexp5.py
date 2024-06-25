#search,delete,insert in unsorted array

def searching(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    return -1
#delete
def deleting(arr,target):
    pos=searching(arr,target)
    return (arr[:pos]+arr[pos+1:])
print(deleting([2,3,4,5,7],4))
#inserting
def inserting(arr,val):
    arr.append(val)
    return arr
print(inserting([2,3,4,5,7],9))
    

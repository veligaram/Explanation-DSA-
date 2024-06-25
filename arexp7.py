#generate subarray

def generatesubarr(arr):
    n=len(arr)
    subarrays=[]
    for i in range(n):
        for j in range(i,n):
            subarray=arr[i:j+1]
            subarrays.append(subarray)
    return subarrays
print(generatesubarr([2,5,6,7,3]))

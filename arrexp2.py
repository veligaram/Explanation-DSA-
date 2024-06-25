#searching in a list

n=int(input())
a=[1,4,5,6]#[5,6,1,4]
for i in range(len(a)):
    if a[i]==n:
        print("element found at :",i)


#List
n=int(input("enter the size of the list"))
lst = list(map(int, input("Enter the integer\
elements:").strip().split()))[:n]
print(lst)
lst.extend(['hello',3])
print(lst)
#comprehension
x=list([x for x in range(3)])
print(x)

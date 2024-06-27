#tuples
var=("hello","hi","bye")
print(var)
var1=("dev",)
print(type(var1))

tep=tuple(("hello","hi","bye"))
print(tep)
#acceesing
print(tep[0])
print(tep[2])
#scling the tuple
print(tep[:2])
#concatenation
print(tep+var)
#nesting
tuple2=(var,tep)
print(tuple2)
#repeating a value in tuple
tep1=('devanandh',)*3
print(tep1)
#tuple in to list
tup1=list(tep1)
print(tup1)

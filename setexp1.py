#sets
set1={1,2,2,3}
print(set1)
myset=set([1,2,3])
print(myset)
#typecasting
#frozensets()
nrm={'a','b','c'}
print(nrm)
frz=frozenset(["e","f","g"])
print(frz)
#add()
set1.add(4)
print(set1)
#union()
print(set1.union(myset))
#intersection()
print(set.intersection(myset))
#differece
print(set1-myset)
#clear
set1.clear()
print(set1)

#Dictionaries
dict_1={1:"dev",2:"thanmai",3:"sahithi"}
print(dict_1)
dict2={'Name':"dev",1:[35,34,60]}
print(dict2)
dict1=dict([(1,"dev"),(2,"thanmai"),(3,"sahithi")])
print(dict1)
#nested dictionary
Dict={1:"dev",2:"thanmai",3:"sahithi",4:{'a':'hello','b':'hehe'}}
print(Dict)
#adding elements
dict1[4]='janani'
dict1[5]='janmabhumi'
print(dict1)
#accessing
print(Dict[4])
print(Dict[4]['a'])
#get
print(Dict.get(3))
#deleting
del(dict_1[1])
print(dict_1)

#list推导式

names=['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names=[name.upper() for name in names if len(name)>3]
print(new_names)

x=[i for i in range(30) if i%3==0]
print(x)

#dict推导式
listdemo=['Google','Runoob','Taobao']
new_dict={key:len(key) for key in listdemo}
print(new_dict)

new_dict1={x:x**2 for x in [2,4,6]}
print(new_dict1)
print(type(new_dict1))

#set推导式
new_set={x**2 for x in [1,2,3]}
print(new_set)

a={x for x in 'abracadabra' if x not in 'abc'}
print(a)

#tuple推导式

b=(x for x in range(1,10))
print(b)
print(tuple(b))

#if else 推导式

list1=['Python','test1','test2']
list2=[word if word.startswith('P') else word.upper() for word in list1]
print(list2)
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
print(type(new_names))
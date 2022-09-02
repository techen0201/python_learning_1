names=['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names=[name.upper() for name in names if len(name)>3]
print(new_names)

x=[i for i in range(30) if i%3==0]
print(x)

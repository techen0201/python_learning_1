'''’
a=['a','b','c']
b=['1','2','3']
print(a+b)
for i in b:
    print(i,end='@')
    print("hello world!")

a=b=c=1
print(a,b,c)

for i in range(0,10):
    print(i,)
'''
y=[1]
y=tuple(y)
b=y
a,=y
print(a)
print(type(a))
print(b,type(b))
c=(1,2)
print(c)
print(type(c))
#数据结构
def myfun1():
    a=[1,2,3]
    print(len(a))
    print(a[len(a):])
    try:
        a.remove(4)
        print(a)
    except:
        print('No that number!')
    a.clear()
    print(a.index(3))

#重排序
def myfun2():
    from collections import deque
    queue=deque('ABCDE')
    print(queue)
    queue.rotate(2)#重排序
    #deque(['D', 'E', 'A', 'B', 'C'])
    queue.rotate(3)
    print(queue)

#列表推导式
def myfun3():
    vec=[2,3,4,5,6]
    vec=[x**2 for x in vec]
    print(vec)
    vec1=[' banana',' loganberry','passion fruit ']
    vec1=[x.strip() for x in vec1]
    print(vec1)

#列表推导式循环
def myfun4():
    list1=[2,6,4]
    list2=[4,3,-9]
    list1.sort()
    nums1=[x*y for x in list1 for y in list2]
    print(nums1)
    nums2=[x+y for x in list1 for y in list2]
    print(nums2)
    nums3=[list1[i]*list2[i] for i in range(len(list1))]
    print(nums3)

#复杂嵌套
def myfun5():
    vec1=[str(round(355/113,i)) for i in range(1,6)]
    print(vec1)
#列表矩阵转置
def myfun6():
    list1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    list2=[[row[i] for row in list1] for i in range(4)]
    print(list2)
def myfun7():
    list1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    transposed=[]
    for i in range(4):
        transposed.append([row[i] for row in list1])
    print(transposed)
def myfun8():
    list1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    transposed=[]
    for i in range(4):
        transposed_row=[]
        for row in list1:
            print(row)
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print(transposed)
def myfun9():
    tuple1=12345,54321,'abcde'
    print(tuple1)
    t=tuple1,(1,2,3,4,5)
    print(t)
def myfun10():
    basket={'apple','orange','apple','pear','orange','banana'}
    print(basket)
    print('apple'in basket)
    print('crabgrass'in basket)
def myfun11():
    a = set('abracadabra')
    b=set('alacazam')
    print(a)
    print(b)
    print(a|b)
    print(a&b)
    print(a-b)
    print(a^b)
def myfun12():
    a = set('abracadabra')
    b = set('alacazam')
    c={x for x in a if x not in 'abc'}
    print(c)
#字典
def myfun13():
    tel={'jack':4098,'sape':4139}
    tel['guido']=4127
    print(tel)
    print(tel['jack'])
    del tel['jack']
    print(tel)
    tel['irv']=4127
    print(tel)
    print(list(tel.keys()))
    print(sorted(tel.keys()))
def myfun14():
    a=dict([('sape',4139)])
    print(a)
def myfun15():
    for i,v in enumerate(['tic','tac','toe']):
        print(i,v)


    questions=['name','quest','favorite color']
    answers=['lancelot','the holly grail','blue']
    for q,a in zip(questions,answers):
        print('What is your {0}? It is {1}'.format(q,a))
def myfun16():
    for x in reversed(range(1,10,2)):
        print(x)
    del x
    basket=['apple','orange','apple','pear','orange','banana']
    for x in sorted(set(basket)):
        print(x)
if __name__=="__main__":
    #myfun1()
    #myfun2()
    #myfun3()
    #myfun4()
    #myfun5()
    #myfun6()
    #myfun7()
    #myfun8()
    #myfun9()
    #myfun10()
    #myfun11()
    #myfun12()
    #myfun13()
    #myfun14()
    #myfun15()
    myfun16()


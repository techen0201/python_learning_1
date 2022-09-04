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

if __name__=="__main__":
    #myfun1()
    #myfun2()
    #myfun3()
    #myfun4()
    #myfun5()
    #myfun6()
    #myfun7()
    myfun8()

#迭代器
def inter1():
    list1=[1,2,3,4]
    it = iter(list1)
    print([x for x in it])


if __name__=='__main__':
    inter1()
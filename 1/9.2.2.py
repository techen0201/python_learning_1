#迭代器

def inter1():
    list1=[1,2,3,4]
    it = iter(list1)
    print([x for x in it])

def inter2():
    import sys
    list2=[1,2,3,4]
    it=iter(list2)
    while True:
        try:
            print(next(it),end=' ')
        except StopIteration:
            sys.exit()

#把一个类作为迭代器
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        self.a
        self.a+=1
        return self.a
if __name__=='__main__':
    #inter1()
    #inter2()
    myclass=MyNumbers()
    myiter=iter(myclass)
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
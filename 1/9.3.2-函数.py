#函数
#两个数比较
def max(a,b):
    if a>b:
        return a
    else:
        return b
#计算面积
def area(width,height):
    return width*height

def myfun(arg2):
    return lambda arg1:arg1+arg2

if __name__=='__main__':
    #print(max(4,5))
    #print(area(4,5))
    mydoubler=myfun(20)
    print(mydoubler(3))


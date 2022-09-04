#生成器
import sys
def fibonacci(n):
    a,b,count=0,1,0
    #方法1

    while True:
        if count>n:
            return
        yield a
        a,b=b,a+b
        count+=1

    '''
    #方法二
    for count in np.arange(n+1):
        yield a
        a,b=b,a+b
    '''
def printinfo(arg1,*,c):
    print("输出：")
    print(arg1)
    print(c)
if __name__=='__main__':
   '''
    f=fibonacci(10)
    while True:
        try:
            print(next(f),end=' ')
        except StopIteration:
            sys.exit()
    '''
   printinfo(10,c=70)

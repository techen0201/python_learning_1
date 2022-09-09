import cmath
num=float(input('请输入数字：'))
num_sqrt=cmath.sqrt(num)
print('{0}平方根是{1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))
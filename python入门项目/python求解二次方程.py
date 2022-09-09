#a*x**2+b*x+c=0
import cmath
def quadratic_equation():
    a = float(input('a:'))
    b = float(input('b:'))
    c = float(input('c:'))
    sol1 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    sol2 = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print('第一个根{0},第二个根{1}'.format(sol1,sol2))

if __name__=='__main__':

    quadratic_equation()
    #pytho()
print('Дано: ax^2+bx+c=0')
a = float(input("Введите a:"))
b = float(input("Введите b:"))
c = float(input("Введите c:"))
d=b**2-4*a*c
import math
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("x1 = " + str(x1), "x2 = " + str(x2))
elif d==0:
    x=-b/(2*a)
    print("x = %.2f" % x)
    
else:
        print("x+iy" ,"x-iy")
    
    
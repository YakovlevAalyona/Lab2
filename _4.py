x=int(input ("Введите х: "))
q=int(input ("Введите q: "))
x2=x*x
cos=1
a1=1
a2=-1
a3=2
a4=2
while (x2/a3)>=q:
    cos=cos+a2*x2/a3
    a1=a1+1
    a4=a4+2
    x2=x2*x*x
    a3=a3*(a4-1)*a4
    a2=a2*(-1)
    print("cos(x):" +str(cos))

year=int(input("Введите возраст: "))
if year<0:
    print(" Возраст не может быть отрицательным!")
if year>100:
    print("Возраст не может быть больше 100!")

t1=year % 10
t2=year % 100
if(t1 == 1 and t2 != 11):
    print(str(year) + " год")
elif(t1 >= 2 and t1 <= 4 and (t2 < 10 or t2 >= 20)):
    print(str(year) + " года")
else:
    print(str(year) + " лет")

''' bài 1'''
print('Hello World!')
''' bài 2 '''
print('Student Name:\nStudent ID:\nClass ID:\nDate of birth:\nMobile Number:')
''' bài 3 '''
fname = input('Input your firstname: ')
lnam  = input('Input your lastname: ')
age   = input('Input your year of brith: ')
print(fname, lnam, age)
''' bài 5 '''
a=input('first num: ')
b=input('second num: ')
print('a+b=',a+b)
''' bài 6 '''
# chia không lấy phần dư và chia lấy phần dư 
a=int(input('first num: '))
b=int(input('second num: '))
print('a/b=',a/b)
print('a%b =',a%b)
''' bài 7 '''
# Write a program to input two numbers and perform all arithmetic operations: sum,
#difference, product, quotient and modulus
a=float(input('first num: '))
b=float(input('second num: '))
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a%b =',a%b)
''' bài 8 '''
# Write a program to input length and width of a rectangle and calculate perimeter and area
#of the rectangle
a=float(input('length: '))
b=float(input('width: '))
print('perimeter=',(a+b)*2)
print('area=',a*b)
''' bài 9 '''
# Write a program to input radius of a circle from user and find diameter, circumference and
#area of the circle not use pi value from math module
r=float(input('radius: '))
print('diameter=',r*2)
print('circumference=',2*r*3.14)
print('area=',r*r*3.14)
''' bài 10'''
num = input('Num with 2 digits: ')
digit=[int(digits) for digits in num]
a=0
for i in digit:
    a=a+i
print('sum of digits ',digit,' : ',a)
''' bài 11'''
c=float(input('temperature in degrees Celsius: '))
print('temperature in Fahrenheit=',c*1.8+32)
''' bài 12'''
h=float(input('hours: '))
m=float(input('minutes: '))
s=float(input('seconds: '))
print('total seconds=',h*3600+m*60+s)
''' bài 13'''
s=int(input('total seconds: '))
h=s//3600
s=s%3600
m=s//60
print('hours: ',h,' minutes: ',m)
''' bài 14'''
#Write a program to input number of days from user and convert it to years, weeks and
#days
d=int(input('days: '))
y=d//365
d=d%365
w=d//7
d=d%7
print(y,' years ',w,' weeks ',d,' days')
''' bài 15'''
# write a program to input leght in centimeters and convert it to kilometers and meters
c=float(input('centimeters: '))
print('kilometers=',c/100000)
print('meters=',c/100)
''' bài 16'''
#triangle
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))
print('perimeter=',a+b+c)
p=(a+b+c)/2
print('area of triangle=',(p*(p-a)*(p-b)*(p-c))**0.5)
#square
a=float(input('a: '))
print('perimeter=',a*4)
print('area of square=',a*a)
#rectangle
a=float(input('a: '))
b=float(input('b: '))
print('perimeter=',(a+b)*2)
print('area of rectangle=',a*b)
#circle
r=float(input('radius: '))
print('perimeter=',2*r*3.14)
print('area of circle=',r*r*3.14)
''' bài 17'''
a=int(input('a: '))
b=int(input('b: '))
if a>b:
    print(a, 'is the maximun vaule')
else: 
    print(b, 'is the maximun vaule')
''' bài 19'''
# program to detect positeve, negative or zero num 
a=float(input('a: '))
if a>0:
    print('positive')
elif a<0:
    print('negative')
else:
    print('zero')
''' bài 20'''
# program to detect even or odd num
a=int(input('a: '))
if a%2==0:
    print('even')
else:
    print('odd')
''' bài 21'''
print('input three numbers: \n')
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))
if a<b and b<c :
    print(a ,b, c)
elif a<c and c<b:
    print(a, c, b)
elif b<a and a<c:
    print(b, a, c)
elif b<c and c<a:
    print(b, c, a)
elif c<a and a<b:
    print(c, a, b)
else:
    print(c, b, a)
''' bài 22'''
# program to find lagrest use conditional operator
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))
max=a if a>b and a>c else b if b>c else c
print(max)
''' bài 24'''
print('linear equation: ax+b=0 solver : \n')
print('input a and b: \n')
a=float(input('a: '))
b=float(input('b: '))
if a==0 and  b==0:
        print('infinity solution')
else:
        print('x: ', -b/a)
''' bài 23'''
yr=int(input('year: '))
if yr%4==0 and yr%100!=0 or yr%400==0:
    print(yr,'is a leap year')
''' bài 25'''
#Write a program to solve quadratic equation : ax2 + bx + c = 0
print('quadratic equation: ax2 + bx + c = 0 solver : \n')
print('input a, b and c: \n')
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))
if a==0 and b==0 and c==0:
    print('infinity solution')
elif a==0 and b==0:
    print('no solution')
elif a==0:
    print('x: ', -c/b)
else:
    delta=b*b-4*a*c
    if delta<0:
        print('no solution')
    elif delta==0:
        print('x: ', -b/(2*a))
    else:
        print('x1: ', (-b+delta**0.5)/(2*a))
        print('x2: ', (-b-delta**0.5)/(2*a))
''' bài 26'''
print('temperature reader: \n')
print('input temperature: \n')
t=float(input('temperature: '))
if t<0:
    print('Freezing weather')
elif t>=0 and t<10:
    print('Very Cold weather')
elif t>=10 and t<20:
    print('Cold weather')
elif t>=20 and t<30:
    print('Normal in Temp')
elif t>=30 and t<40:
    print('Its Hot')
elif t>=40:
    print('Its Very Hot')
''' bài 27'''
num = input('three digts Num : ')
digit = [int(digits) for digits in num]
for i in range(len(digit)):
    for j in range(len(digit)-i-1):
        if digit[j] > digit[j+1]:
            digit[j], digit[j+1] = digit[j+1], digit[j]
print(digit)
# sắp xếp tăng dần theo thuật toán bubble sort
''' bài 28'''


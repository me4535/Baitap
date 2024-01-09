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

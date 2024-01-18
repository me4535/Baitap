''' bài 1'''
def bai1():
    print('Hello World!')
''' bài 2 '''
def bai2():
    print('Student Name:\nStudent ID:\nClass ID:\nDate of birth:\nMobile Number:')
''' bài 3 '''
def bai3():
    fname = input('Input your firstname: ')
    lnam  = input('Input your lastname: ')
    age   = input('Input your year of brith: ')
    print(fname, lnam, age)
''' bài 4 '''
def bai4():
    print('*'*41)
    print('*'*7,'HUONG DAN CHEP TAP TIN','*'*7)
    print('B1.Vao thu muc "C:\ TUYEN TAP\ thotinh.txt"')
    print('B2.Click chuot phai vao tap tin thotinh.txt')
    print('B3.Chon Copy tu menu tat')
    print('B4.Chon vi tri can luu, click chuot phai chon Paste')
    print('*'*41)
''' bài 5 '''
def bai5():
    a=input('first num: ')
    b=input('second num: ')
    print('a+b=',a+b)
''' bài 6 '''
def bai6():
    a=int(input('a: '))
    b=int(input('b: '))
    print('a/b=',a/b)
    print('a%b =',a%b)
''' bài 7 '''
def bai7():
    a=float(input('first num: '))
    b=float(input('second num: '))
    print('a+b=',a+b)
    print('a-b=',a-b)
    print('a*b=',a*b)
    print('a/b=',a/b)
    print('a%b =',a%b)
''' bài 8 '''
def bai8():
    a=float(input('length: '))
    b=float(input('width: '))
    print('perimeter=',(a+b)*2)
    print('area=',a*b)
''' bài 9 '''
def bai9():
    r=float(input('radius: '))
    print('diameter=',r*2)
    print('circumference=',2*r*3.14)
    print('area=',r*r*3.14)
''' bài 10'''
def bai10():
    num = input('Num with 2 digits: ')
    digit=[int(digits) for digits in num]
    a=0
    for i in digit:
        a=a+i
    print('sum of digits ',digit,' : ',a)
''' bài 11'''
def bai11():
    c=float(input('temperature in degrees Celsius: '))
    print('temperature in Fahrenheit=',c*1.8+32)
''' bài 12'''
def bai12():
    h=float(input('hours: '))
    m=float(input('minutes: '))
    s=float(input('seconds: '))
    print('total seconds=',h*3600+m*60+s)
''' bài 13'''
def bai13():
    s=int(input('total seconds: '))
    h=s//3600
    s=s%3600
    m=s//60
    print('hours: ',h,' minutes: ',m)
''' bài 14'''
def bai14():
    d=int(input('days: '))
    y=d//365
    d=d%365
    w=d//7
    d=d%7
    print(y,' years ',w,' weeks ',d,' days')
''' bài 15'''
def bai15():
    c=float(input('centimeters: '))
    print('kilometers=',c/100000)
    print('meters=',c/100)
''' bài 16'''
def bai16():
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
def bai17():
    a=int(input('a: '))
    b=int(input('b: '))
    if a>b:
        print(a, 'is the maximun vaule')
    else: 
        print(b, 'is the maximun vaule')
''' bài 18'''
def bai18():
    a=int(input('a: '))
    if a%2==0:
        print('even')
    else:
        print('odd')
''' bài 19'''
def bai19():
    a=float(input('a: '))
    if a>0:
        print('positive')
    elif a<0:
        print('negative')
    else:
        print('zero')
''' bài 20'''
def bai20():
    print('input three numbers: \n')
    a=float(input('a: '))
    b=float(input('b: '))
    c=float(input('c: '))
    max=a if a>b and a>c else b if b>c else c
    print(max)
''' bài 21'''
def bai21():
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
def bai22():
    print('input three numbers: \n')
    a=float(input('a: '))
    b=float(input('b: '))
    c=float(input('c: '))
    max=a if a>b and a>c else b if b>c else c
    print(max)
''' bài 24'''
def bai24():
    print('linear equation: ax+b=0 solver : \n')
    print('input a and b: \n')
    a=float(input('a: '))
    b=float(input('b: '))
    if a==0 and  b==0:
        print('infinity solution')
    else:
        print('x: ', -b/a)
''' bài 23'''
def bai23():
    yr=int(input('year: '))
    if yr%4==0 and yr%100!=0 or yr%400==0:
        print(yr,'is a leap year')
''' bài 25'''
def bai25():
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
def bai26():
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
def bai27():
    num = input('three digts Num : ')
    digit = [int(digits) for digits in num]
    for i in range(len(digit)):
            for j in range(len(digit)-i-1):
                if digit[j] > digit[j+1]:
                    digit[j], digit[j+1] = digit[j+1], digit[j]
    print(digit)
''' bài 28'''
def bai28():
    day_number = int(input("Nhập một số nguyên từ khoảng 2 đến 8: "))
    if 2 <= day_number <= 8:
        day_names = {2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday', 8: 'Sunday'}
        day_name = day_names[day_number]
        print(day_name)
    else:
        print("Số nguyên phải nằm trong khoảng từ 2 đến 8.")
print('bài tập đã làm 1-28')
def thucthiham():
    tenham = input('nhập bài tập muốn chạy vd: bai27:')
    if tenham in globals():
        ham=globals()[tenham]
        ham()
    else:
        print('bài tập',tenham,'chưa được làm.')
thucthiham()




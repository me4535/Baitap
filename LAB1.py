def bai1():
    name=input("Nhap ten cua ban: ")
    print("Hello "+name)
def bai2():
    h = float(input('nhập số giờ : '))
    r = float(input('nhập số tiền : '))
    print('lương của bạn là :', h*r)
def bai3():
    #Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature
    celsius = float(input('nhập độ C : '))
    print('độ F là :', celsius*1.8+32)
def bai4():
    #Write a program that allows user inputting a simple expression containing one of four operators +, -, *, / then the result is printed out to the monitor. 
    a = float(input('nhập a : '))
    b = float(input('nhập b : '))
    c = input('nhập phép tính : ')
    if c == '+':
        print('kết quả là :', a+b)
    elif c == '-':
        print('kết quả là :', a-b)
    elif c == '*':
        print('kết quả là :', a*b)
    elif c == '/':
        print('kết quả là :', a/b)
    else:
        print('nhập sai phép tính')

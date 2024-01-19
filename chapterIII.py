''' bài 29'''
def bai29():
    n=int(input('n: '))
    giaithua=1
    for i in range(1,n+1):
        giaithua=giaithua*i
    print('n!=',giaithua)
''' bài 30'''
def bai30():
    n=int(input('n: '))
    i = 1
    sn= 0
    while i <= (2*n+1):
        sn= sn+i
        i=i+2
    print('S=',sn)
''' bài 31'''
def bai31():
    n = int(input('n: '))
    i = 1
    p = 1
    while i <= (2*n+1):
        p= p*i
        i=i+2
    print('P= ',p)
''' bài 32'''
def bai32():
    n = int(input('n: '))
    i=1
    P = 1
    s = 0
    while i <= n : 
        P = P*i
        s=s+P
        i=i+1
    print('S= ',s)
''' bài 33'''
def bai33():
    n = int(input('n: '))
    i = 0
    sodd=0
    seven=0
    while i < n:
        i = i+1
        if i %2 ==0 :
            sodd = sodd + i
        elif i %2 !=0 :
            seven = seven + i
        sn = seven-sodd
    print(sn)
''' bài 34 '''
def bai34():
    n = int(input('n: '))
    i = 1
    s = 1
    while i < n:
        i+=1
        s =s +(1/i)
    print(s)
''' bài 35'''
def bai35():
    n = int(input('n: '))
    i=1
    coutn=1
    while i<n:
        i+=1
        if n%i==0:
            coutn=coutn+1
    print(coutn)
''' bài 36'''
def bai36():
    a = int(input('a: '))
    b = int(input('b: '))
    if a > b:
        min = b
    else:
        min = a
    for i in range(1,min+1):
        if a%i==0 and b%i==0:
            gcd=i
    print('gcd: ',gcd)
    lcm=(a*b)/gcd
    print('lcm: ',lcm)
''' bài 37'''
def bai37():
    n = int(input('n: '))
    if n > 1:
        for i in range(2,n):
            if n%i==0:
                print(n,'không là số nguyên tố')
                break
        else:
            print(n,'là số nguyên tố')
    else:
        print(n,'không là số nguyên tố')
print('bài tập đã làm 29-37')
def thucthiham():
    tenham = input('nhập bài tập muốn chạy vd: bai27:')
    if tenham in globals():
        ham=globals()[tenham]
        ham()
    else:
        print('bài tập',tenham,'chưa được làm.')
thucthiham()

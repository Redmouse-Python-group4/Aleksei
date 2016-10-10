def func1(x, y):
    print(x*y)

def func2(x, y):
    print(x**y)

def func3(x):
    q=x+10
    while x<q:
        x=x+1
        print x

x=int(raw_input('Enter a number from 1 to 9:\n'))

if x >= 1 and x <= 3:
    s=raw_input('Enter the string:\n')
    n=int(raw_input('Enter number of repeat line:\n'))
    func1(s, n)
elif x<7:
    m=int(raw_input('Introduce the degree in which to build a number of:'))
    func2(x, m)
elif x<=9:
    func3(x)
else:
    print('Input error')
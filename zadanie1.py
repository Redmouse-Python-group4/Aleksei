x = int(raw_input('Enter a number from 1 to 9:'))
if x >= 1 and x <= 3:
    s = raw_input('Enter the string:')
    n = int(raw_input('Enter number of repeat line:'))
    i = 0
    while i < n:
        i = i + 1
        print(s)
elif x >= 4 and x <= 6:
    m = int(raw_input('Introduce the degree in which to build a number of:'))
    degree = x ** m
    print(degree)
elif x >= 7 and x <= 9:
    q = x + 10
    while x < q:
        x= x + 1
        print (x)
else:
    print('Input error')

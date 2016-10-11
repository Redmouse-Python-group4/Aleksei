def func():
    global x
    x = y.split(' ')
    for i in x:
        print('%s - %s')% (i, len(i))
y = raw_input('Enter some string:\n')
print func()
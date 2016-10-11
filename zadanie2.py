print "Society at the beginning of the XXI century"

x = int(raw_input('How old are you?'))
if x >= 0 and x < 7:
    print 'Go to kindergarten'
elif x >= 7 and x < 18:
    print 'Go to school'
elif x >= 18 and x < 25:
    print 'Go to university'
elif x >= 25 and x < 60:
    print 'Go to work'
elif x >= 60 and x < 120:
    print 'You are granted a choice'
else:
    i = 0
    while i < 5:
        i = i +1
        print('Wrong! This programm for people!')

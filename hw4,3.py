# -*- coding: utf-8 -*- 
import random
x = raw_input('Введите вопрос: ')
array = random.choice(['да', 'нет', 'возможно', 'не сейчас', 'точно', 'в дальнейшем', 'никогда', 'спроси позже'])
y = '%s - %s' %(x, array)
print y
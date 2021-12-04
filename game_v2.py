"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
from numpy import random

number = np.random.randint(1, 101) # загадываем число

def game_core(number):
    
    # Ваш код начинается здесь

    count = 0   # счетчик попыток
    prdict_number_min = 1  # нижняя граница поиска числа
    prdict_number_max = 101  # верхняя граница поиска числа
    
    while True:
        count+=1
        
        prdict_number = (prdict_number_max + prdict_number_min)//2

        if number > prdict_number:
            prdict_number_min = prdict_number  # смещение нижней границы поиска числа
            
        elif number < prdict_number:
            prdict_number_max = prdict_number  # смещение верхней границы поиска числа
            
        else:
            break

    return count
    
print(game_core(number))
print(number)


    


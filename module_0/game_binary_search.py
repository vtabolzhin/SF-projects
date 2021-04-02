import numpy as np

# границы диапазона для загадывания случайного числа
min_number = 1
max_number = 100

def game_core_v3(number, low=min_number, high=max_number):
    '''Функция определяет число number, загаданное в интервале [low,high]
    методом бинарного поиска и возвращает количество итераций'''

    count = 0           # счетчик итераций
 
    while low <= high:  # цикл длится, пока границы поиска не сократятся до одного элемента
        count += 1
        predict = int((low + high)/2)    # предполагаемое число
        if predict == number:
            return(count) 
        elif predict < number:    
            low = predict + 1
        else:
            high = predict - 1
    return None

def score_game(game_core, n=1000, low=min_number, high=max_number):
    '''Функция проверяет передаваемый ей алгоритм отгадывания game_core
    и возвращает среднее количество попыток за n игр'''

    count = 0           # счетчик попыток
    np.random.seed(0)   # фиксируетм seed для воспроизводимости результата
    random_numbers = np.random.randint(low, high+1, size=n) # массив загаданных чисел

    for number in random_numbers:
        count += game_core(number)

    count = round(count/n) #приводим количество попыток к среднему значению
    return(count)

avg_count = score_game(game_core_v3)
print(f'Алгоритм угадывает число в диапазоне от {min_number} до {max_number} среднем за {avg_count} попыток')
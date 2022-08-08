import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

#  Чтобы отделить вызовы функций от импорта,
#  необходимо в файле game_v2.py перенести вызовы функций 
#  в следующую конструкцию
if __name__ == '__main__':
    
# Условие __name__ == '__main__' выполнится только тогда,
# когда файл game_v2.py будет исполняемым 
# (когда мы запускаем файл через RUN). 
# Если файл является импортируемым 
# (используется в качестве внешнего модуля), 
# то условие не будет выполняться 
# и функция score_game() не будет вызываться.




# RUN
 score_game(random_predict)
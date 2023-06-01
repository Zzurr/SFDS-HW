def check():
    
    import numpy as np

    # задаем базовые значения:  
    min_number = 1            # минимум рассматриваемого диапазона (по умолчанию 1)
    max_number = 100           # максимум рассматриваемого диапазона (по умолчанию 100)
    number = np.random.randint(min_number, max_number + 1) # генерируем случайное число от 1 до 100
    predict_number = np.random.randint(min_number, max_number + 1)  # генерируем предполагаемое число в 1-й попытке
    count = 0           # количество попыток

    while True:
        count += 1
        if predict_number > number:   
            # если предлагаемое число больше искомого, то за максимум интервала берем предлагаемое число 
            max_number = predict_number
            # новое предлагаемое число будет посередине между предыдущей попыткой и минимумом
            predict_number = predict_number - int((predict_number - min_number) * 0.5)
        elif predict_number < number:
            # если предлагаемое число меньше искомого, то за минимум интервала берем предлагаемое число 
            min_number = predict_number
            # новое предлагаемое число будет посередине между предыдущей попыткой и максимумом
            predict_number = predict_number + int((max_number - predict_number) *0.5)
        else:
            print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break
    return count
check()  
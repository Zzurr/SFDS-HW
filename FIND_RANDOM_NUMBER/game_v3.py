def check() -> int:
    """_summary_

    Returns:
        int: _description_
    """
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
            max_number = predict_number
            predict_number = predict_number - int((predict_number - min_number) * 0.5)
        elif predict_number < number:
            min_number = predict_number
            predict_number = predict_number + int((max_number - predict_number) *0.5)
        else:
            print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break
    return None
    
import numpy as np


def game_core(number, min_value=1, max_value=100):
    """Функция реализует "угадывание" числа методом деления пополам.

    Args:
        number (int): Загаданное число.
        min_value (int, optional):
            Нижняя граница диапазона загадываемых чисел.
            По умолчанию 1.
        max_value (int, optional):
            Верхняя граница диапазона загадываемых чисел.
            По умолчанию 100.
    """
    count = 0
    predict = min_value - 1  # этим мы гарантируем вход в цикл

    while number != predict:
        count += 1
        predict = (max_value+min_value) // 2  # определение середины отрезка

        if number > predict:
            min_value = predict + 1  # сдвигаем нижнюю границу поиска
        elif number < predict:
            max_value = predict - 1  # сдвигаем верхнюю границу поиска

    return count


def score_game(test_fn, min_value=1, max_value=100, iters=1000):
    """Функция рассчитывает среднее число попыток,
    затраченных на "угадывание" числа переданной функцией test_fn.

    Args:
        test_fn (function): Тестируемая функция.
        min_value (int, optional):
            Нижняя граница диапазона загадываемых чисел.
            По умолчанию 1.
        max_value (int, optional):
            Верхняя граница диапазона загадываемых чисел.
            По умолчанию 100.
        iters (int, optional):
            Количество итераций.
            По умолчанию 1000.
    """
    np.random.seed(42)  # фиксируем seed, для воспроизводимости эксперимента
    results = []
    random_array = np.random.randint(min_value, max_value+1, size=(iters))

    for number in random_array:
        results.append(test_fn(number))

    mean_score = int(np.mean(results))

    return mean_score


score = score_game(game_core)
print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

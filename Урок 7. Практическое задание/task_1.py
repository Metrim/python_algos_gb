"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""


import random
import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_2(lst_obj):
    n = 1
    FLAG = False
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                FLAG = True
        if not FLAG:
            break
        n += 1
        FLAG = False
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(100)]

print(f"Исходный массив: {orig_list}")
print(f"Отсортированный массив: {bubble_sort(orig_list[:])}")


print(f"Исходный массив: {orig_list}")
print(f"Отсортированный массив: {bubble_sort_2(orig_list[:])}")


# замеры 10
print(timeit.timeit("bubble_sort(orig_list)",
    setup="from __main__ import bubble_sort, orig_list", number=100))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort(orig_list)",
    setup="from __main__ import bubble_sort, orig_list", number=100))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort(orig_list)",
    setup="from __main__ import bubble_sort, orig_list", number=100))


# замеры 10
print(timeit.timeit("bubble_sort_2(orig_list)",
    setup="from __main__ import bubble_sort_2, orig_list", number=100))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort_2(orig_list)",
    setup="from __main__ import bubble_sort_2, orig_list", number=100))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort_2(orig_list)",
    setup="from __main__ import bubble_sort_2, orig_list", number=100))


"""
Исходный массив: [64, -38, 94, 84, -90, 12, -14, -61, 75, -44, -8, -91, -32, 30, -71, 32, -5, -76, -61, -13, 54, 21, 100, 30, 100, -71, -58, -99, -35, -11, -66, 96, 100, 58, -6, 75, -12, -64, -21, -70, -27, 16, -20, -21, -6, 67, 53, 28, -52, -85, 66, -4, -66, -100, -91, -96, 28, -98, -72, 46, 40, 70, 73, 70, 15, -59, 48, -99, 78, 82, -94, -94, 6, -28, 34, -7, 34, -80, 71, 81, 41, 2, -34, -23, -29, 43, -47, 45, 62, -62, 47, -84, 48, 50, 95, 23, -80, 46, -26, 41]
Отсортированный массив: [100, 100, 100, 96, 95, 94, 84, 82, 81, 78, 75, 75, 73, 71, 70, 70, 67, 66, 64, 62, 58, 54, 53, 50, 48, 48, 47, 46, 46, 45, 43, 41, 41, 40, 34, 34, 32, 30, 30, 28, 28, 23, 21, 16, 15, 12, 6, 2, -4, -5, -6, -6, -7, -8, -11, -12, -13, -14, -20, -21, -21, -23, -26, -27, -28, -29, -32, -34, -35, -38, -44, -47, -52, -58, -59, -61, -61, -62, -64, -66, -66, -70, -71, -71, -72, -76, -80, -80, -84, -85, -90, -91, -91, -94, -94, -96, -98, -99, -99, -100]
Исходный массив: [64, -38, 94, 84, -90, 12, -14, -61, 75, -44, -8, -91, -32, 30, -71, 32, -5, -76, -61, -13, 54, 21, 100, 30, 100, -71, -58, -99, -35, -11, -66, 96, 100, 58, -6, 75, -12, -64, -21, -70, -27, 16, -20, -21, -6, 67, 53, 28, -52, -85, 66, -4, -66, -100, -91, -96, 28, -98, -72, 46, 40, 70, 73, 70, 15, -59, 48, -99, 78, 82, -94, -94, 6, -28, 34, -7, 34, -80, 71, 81, 41, 2, -34, -23, -29, 43, -47, 45, 62, -62, 47, -84, 48, 50, 95, 23, -80, 46, -26, 41]
Отсортированный массив: [100, 100, 100, 96, 95, 94, 84, 82, 81, 78, 75, 75, 73, 71, 70, 70, 67, 66, 64, 62, 58, 54, 53, 50, 48, 48, 47, 46, 46, 45, 43, 41, 41, 40, 34, 34, 32, 30, 30, 28, 28, 23, 21, 16, 15, 12, 6, 2, -4, -5, -6, -6, -7, -8, -11, -12, -13, -14, -20, -21, -21, -23, -26, -27, -28, -29, -32, -34, -35, -38, -44, -47, -52, -58, -59, -61, -61, -62, -64, -66, -66, -70, -71, -71, -72, -76, -80, -80, -84, -85, -90, -91, -91, -94, -94, -96, -98, -99, -99, -100]
Время в базовом варианте:
0.0358961
0.026388899999999993
3.4017957

Время в оптимизированном, видно улучшение при росте размера массива для сортировки:
0.005687700000000184
0.0008991999999996558
0.060493099999999966

"""
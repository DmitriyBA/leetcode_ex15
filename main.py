import random
array_digits = [random.randint(20, 10000) for item in range(random.randint(4, 15))]


def array_result_digits(array_digit: list) -> list:
    """
    Функция принимает на вход список чисел
    Функция возвращает список количества цифр в каждом числе
    """
    result_array_for_digit = []
    for number in array_digit:
        count = 0
        while number:
            digit = number % 10
            count += 1
            number = number // 10
        result_array_for_digit.append(count)
    return result_array_for_digit


list_digits = array_result_digits(array_digits)


def count_list_digit(lst_digits: list) -> int:
    """
    Функция принимает на вход список количества цифр в каждом числе
    Функция возвращает количество четных чисел изначально переданного списка
    """
    count = 0
    for count_digit in lst_digits:
        if count_digit % 2 == 0:
            count += 1
    return count


print(array_digits)
print(count_list_digit(list_digits))

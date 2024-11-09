'''Задача: "План перехват".'''


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for number in numbers:
            try:
                result += number
            except TypeError:
                print(f"Некорректный тип данных для подсчёта суммы: {number}")
                incorrect_data += 1
        _list = (result, incorrect_data)
        return _list
    except TypeError:
        print('В numbers записан некорректный тип данных')
        pass

# print(personal_sum([1,2,3,4,5]))
# print(personal_sum(range(1, 11)))
# print(personal_sum((1, 2, 'string')))
# print(personal_sum("1, 2"))
# print(f'Результат 2: {personal_sum([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
# print(f'Результат 1: {personal_sum("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
# print(personal_sum([]))

def calculate_average(numbers):
    var = personal_sum(numbers)
    count = 0
    try:
        for number in numbers:
            if number != str(number):
                count += 1
            else:
                continue
        try:
            average = var[0] / count
        except ZeroDivisionError:
            average = 0
        return average
    except TypeError:
        return None

# print(calculate_average([]))

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


def add_everything_up(a, b):
        try:
            print()
            return a+b
        except TypeError as exc:
            print(f"Выполнить сложение a = '{a}' и b = '{b}' не удалось, \n"
                  f"действие вызвало ошибку: '{exc}'")
            return a, b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
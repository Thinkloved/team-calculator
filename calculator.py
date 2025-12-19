print("Калькулятор команды [твое имя] и [имя друга]")

def add(a, b):
    """Функция сложения двух чисел"""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

# Проверка работы
if __name__ == "__main__":
    print("Проверяем сложение:")
    add(5, 3)
    add(10, 20)
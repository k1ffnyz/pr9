numbers = []  # Список для хранения введённых чисел

while True:
    user_input = input("Введите число или 'end' для завершения ввода: ")
    
    if user_input == "end":
        break
        
    try:
        number = float(user_input)  # Попытка преобразовать строку в число
        numbers.append(number)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число или 'end'.")

# Фильтруем список, оставляя только нечетные числа
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Нечетные элементы списка:", odd_numbers)
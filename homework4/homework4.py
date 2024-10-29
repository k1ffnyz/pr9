even_count = 0  # счётчик четных чисел
odd_count = 0   # счетчик нечетных чисел
numbers = []    # список для хранения введенных чисел

while True:
    user_input = input("Введите число или 'end' для завершения ввода: ")
    
    if user_input.lower() == 'end':
        break
    
    try:
        number = float(user_input)  # Преобразуем ввод в число
        numbers.append(int(number)) # Добавляем целое число в список
        
        # Проверяем, является ли число четным или нечетным
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число или 'end'.")

# Вывод результатов
print(f"Введено четных чисел: {even_count}")
print(f"Введено нечетных чисел: {odd_count}")
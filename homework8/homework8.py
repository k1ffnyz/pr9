import random

# Лотерейный билет
ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

# Функция для выбора чисел пользователем
def get_user_choices(ticket):
    choices = []
    for row in ticket:
        choice = int(input(f"Сделайте выбор из {row}: "))
        while choice not in row:
            choice = int(input(f"Попробуйте ещё раз: "))
        choices.append(choice)
    return choices

# Функция для случайного выбора компьютером
def get_computer_choices(ticket):
    return [random.choice(row) for row in ticket]

# Основная функция лотереи
def lottery(ticket):
    user_choices = get_user_choices(ticket)
    computer_choices = get_computer_choices(ticket)
    
    matches = sum(u == c for u, c in zip(user_choices, computer_choices))
    
    print("\nВаш выбор:", user_choices)
    print("Выбор компьютера:", computer_choices)
    print(f"Количество совпадений: {matches}\n")

# Запуск лотереи
lottery(ticket)
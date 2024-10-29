import re  # Импортируем модуль регулярных выражений

def parse_email(email):
    pattern = r'([^@]+)@([a-zA-Z0-9.-]+)'  # Шаблон для поиска имени пользователя и доменного имени
    match = re.match(pattern, email)  # Применяем шаблон к строке email

    if match:
        username = match.group(1)  # Извлекаем имя пользователя
        domain = match.group(2)  # Извлекаем доменное имя
        return username, domain  # Возвращаем кортеж с результатами
    else:
        return None, None  # Если не удалось разобрать email, возвращаем None

while True:
    email_input = input("Введите ваш email (или введите 'exit' для выхода): ")  # Запрашиваем email у пользователя
    if email_input.lower() == 'exit':  # Проверяем, хочет ли пользователь выйти
        print("Выход из программы.")  # Сообщаем о выходе
        break  # Завершаем цикл

    username, domain = parse_email(email_input)  # Разбираем email

    if username and domain:  # Если разбор прошел успешно
        print(f"Имя пользователя: {username}")  # Выводим имя пользователя
        print(f"Доменное имя: {domain}")  # Выводим доменное имя
    else:
        print("Некорректный email. Попробуйте еще раз.")  # Сообщаем о неправильном формате email
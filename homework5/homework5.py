# Исходный список
numbers = [1, 3, 2, 8, 5, 7, 4, 9]

# Результат будем хранить в этом списке
result = []

# Начинаем с первого индекса, равного 1
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        result.append(numbers[i])

# Выводим результат
print(result)
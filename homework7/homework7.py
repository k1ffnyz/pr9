def cyclic_shift_right(lst):
    # Сохраняем последний элемент списка
    last_element = lst[-1]
    
    # Сдвигаем все элементы на одну позицию вправо
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    
    # Вставляем последний элемент в начало списка
    lst[0] = last_element
    
    return lst

# Пример использования
my_list = [1, 2, 3, 4, 5]
shifted_list = cyclic_shift_right(my_list)
print(shifted_list)
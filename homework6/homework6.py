def swap_min_max(lst):
    # Проверяет, является ли список пустым или содержит только один элемент.
    if not lst:
        return lst
    
    # Находит индекс минимального элемента в списке.
    min_idx = lst.index(min(lst))
    
    # Находит индекс максимального элемента в списке.
    max_idx = lst.index(max(lst))
    
    # Меняет местами элементы на указанных индексах.
    lst[min_idx], lst[max_idx] = lst[max_idx], lst[min_idx]
    
    # Возвращает изменённый список.
    return lst

# Пример использования функции.
my_list = [3, 8, 1, 6, 5, 4, 7, 2]
swapped_list = swap_min_max(my_list)
print(swapped_list)
def alg_for_min():
    input_list = input("Введите список чисел через пробел: ").strip()

    if not input_list:
        print("Вы ничего не ввели!")
        return

    input_list = input_list.split()

    # Преобразуем каждый элемент в целое число с использованием цикла
    converted_list = []
    for num in input_list:
        try:
            converted_list.append(int(num))
        except ValueError:
            print(f"Элемент '{num}' не является числом!")

    # Найти минимальное значение
    if converted_list:  # Проверка на случай, если список окажется пустым после фильтрации
        min_value = min(converted_list)
        print("Минимальное значение в списке:", min_value)
    else:
        print("В списке нет допустимых чисел!")


if __name__ == "__main__":
    alg_for_min()
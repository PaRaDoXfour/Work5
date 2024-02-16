def sum_even_index_elements(arr):
    sum_even = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            sum_even += arr[i]
    return sum_even

def main():
    # Запитуємо користувача про розмір масиву
    N = int(input("Введіть розмір масиву: "))

    # Ініціалізуємо масив
    arr = []

    # Заповнюємо масив елементами, введеними користувачем
    print("Введіть елементи масиву:")
    for _ in range(N):
        while True:  # Повторюємо введення, поки не буде введено ціле число
            try:
                element = int(input())
                arr.append(element)
                break  # Виходимо з циклу, якщо введене значення успішно конвертується у ціле число
            except ValueError:
                print("Будь ласка, введіть ціле число.")

    # Знаходимо суму елементів масиву з парними індексами
    result = sum_even_index_elements(arr)

    # Виводимо результат
    print("Сума елементів масиву з парними індексами:", result)
if __name__ == "__main__":
    main()
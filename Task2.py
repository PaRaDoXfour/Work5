def create_chessboard(N):
    chessboard = []

    for i in range(N):
        row = []
        for j in range(N):
            # Додаємо 1, якщо сума індексів парна, і 0, якщо сума індексів непарна
            if (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        chessboard.append(row)

    return chessboard

def print_chessboard(chessboard):
    for row in chessboard:
        print(" ".join(map(str, row)))

def main():
    # Запитуємо розмір шахової дошки від користувача
    N = int(input("Введіть розмір квадратної матриці: "))

    chessboard = create_chessboard(N)

    print("Шахматне поле:")
    print_chessboard(chessboard)

if __name__ == "__main__":
    main()

n = int(input("Введіть розмір квадратної матриці: "))

chessboard = [[(i + j) % 2 for j in range(n)] for i in range(n)]

print("Шахматне поле:")
for n in chessboard:
    print(" ".join(map(str, n)))

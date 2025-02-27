import numpy as np


#чтение матрицы с файла
def read_matrix_from_file(filename):

    with open(filename, 'r') as file:
        n = int(file.readline())
        A = []
        for _ in range(n):
            row = list(map(float, file.readline().split()))
            A.append(row)
        b = list(map(float, file.readline().split()))
    return np.array(A), np.array(b)

#ручной ввод
def input_matrix_manually():

    n = int(input("Введите размерность матрицы n: "))
    print("Введите матрицу A:")
    A = []
    for i in range(n):
        while True:
            row_input = input(f"Строка {i + 1}: ")
            try:
                row = list(map(float, row_input.split()))
                if len(row) != n:
                    print(f"Ошибка: в строке должно быть {n} элементов.")
                else:
                    A.append(row)
                    break
            except ValueError:
                print("Ошибка: введите числа, разделённые пробелами.")

    print("Введите вектор b:")
    while True:
        b_input = input("b: ")
        try:
            b = list(map(float, b_input.split()))
            if len(b) != n:
                print(f"Ошибка: в векторе должно быть {n} элементов.")
            else:
                break
        except ValueError:
            print("Ошибка: введите числа, разделённые пробелами.")

    return np.array(A), np.array(b)

def lu_decomposition(A):
    """
    Выполняет LU-разложение матрицы A.
    Возвращает матрицы L и U.
    """
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Верхняя треугольная матрица U
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_

        # Нижняя треугольная матрица L
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Диагональные элементы L равны 1
            else:
                sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_) / U[i][i]
    return L, U

def solve_lu(L, U, b):
    """
    Решает систему линейных уравнений LUx = b.
    Возвращает вектор x.
    """
    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)

    # Решение Ly = b (прямая подстановка)
    for i in range(n):
        sum_ = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b[i] - sum_

    # Решение Ux = y (обратная подстановка)
    for i in range(n - 1, -1, -1):
        sum_ = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_) / U[i][i]
    return x

def check_solution(A, x, b):
    """
    Проверяет корректность решения системы Ax = b.
    Возвращает True, если решение верное, иначе False.
    """
    return np.allclose(np.dot(A, x), b)

def main():
    print("Выберите способ ввода данных:")
    print("1. Загрузить из файла")
    print("2. Ввести вручную")
    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        filename = input("Введите имя файла: ")
        try:
            A, b = read_matrix_from_file(filename)
        except FileNotFoundError:
            print("Ошибка: файл не найден.")
            return
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return
    elif choice == '2':
        A, b = input_matrix_manually()
    else:
        print("Ошибка: неверный выбор.")
        return

    # Вывод исходных данных
    print("\nИсходная матрица A:")
    print(A)
    print("\nВектор правых частей b:")
    print(b)

    # LU-разложение
    L, U = lu_decomposition(A)
    print("\nМатрица L:")
    print(L)
    print("\nМатрица U:")
    print(U)

    # Решение системы
    x = solve_lu(L, U, b)
    print("\nРешение системы x:")
    print(x)

    # Проверка решения
    if check_solution(A, x, b):
        print("\nПроверка: Решение верное!")
    else:
        print("\nПроверка: Решение неверное!")

if __name__ == "__main__":
    main()
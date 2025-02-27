import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -x**3 + 4*x + np.cos(x)

# Ввод данных пользователем
def get_input():
    try:
        start = float(input("Введите начальное значение x: "))
        end = float(input("Введите конечное значение x: "))
        step = float(input("Введите шаг для x: "))
        return start, end, step
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")
        return get_input()

# Получение данных от пользователя
start, end, step = get_input()

# Генерация значений x с заданным шагом
x_values = np.arange(start, end, step)

# Вычисление значений функции f(x)
y_values = f(x_values)

# Построение графика
fig, ax = plt.subplots()
ax.plot(x_values, y_values, label='f(x) = -x^3 + 4x + cos(x)')
ax.set_title('График функции f(x)')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.grid(True)
ax.legend()

# Включение инструментов масштабирования и панорамирования
plt.tight_layout()
plt.show()
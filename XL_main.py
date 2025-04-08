import time
import numpy as np
from sympy import symbols, GF, Matrix

def generate_monomials(variables, degree):
    """Генерує всі можливі мономи до заданого степеня."""
    if degree == 0:
        return [1]
    else:
        monomials = [1]
        for d in range(1, degree + 1):
            monomials += [np.prod(m) for m in np.array(np.meshgrid(*([variables] * d))).T.reshape(-1, d)]
        return list(set(monomials))

def linearize_system(equations, variables, degree, field_order=2):
    """Лінеаризує систему рівнянь шляхом розширення та вилучення коефіцієнтів."""
    # Генерація мономів до заданого степеня
    monomials = generate_monomials(variables, degree)
    num_monomials = len(monomials)

    # Створення матриці коефіцієнтів
    matrix = []
    for eq in equations:
        row = []
        for m in monomials:
            # Обчислення коефіцієнтів над полем GF(field_order)
            coeff = eq.expand().coeff(m) if m != 1 else eq.expand().as_coeff_add()[0]
            row.append(int(coeff.evalf() % field_order) if coeff.is_number else 0)
  # Залишок за модулем
        matrix.append(row)

    # Переведення у матрицю SageMath (або SymPy)
    return Matrix(matrix), monomials

def solve_xl(equations, variables, degree=2, field_order=2):
    """Основна функція алгоритму XL."""
    start_time = time.time()

    # Лінеаризуємо систему
    matrix, monomials = linearize_system(equations, variables, degree, field_order)
    print("Матриця коефіцієнтів:")
    print(matrix)

    # Розв'язуємо лінійну систему методом Гаусса
    reduced_matrix, pivots = matrix.rref()
    print("\nЗведена матриця (Рядкова канонічна форма):")
    print(reduced_matrix)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nЧас обчислення: {elapsed_time:.6f} секунд")
    return reduced_matrix, elapsed_time

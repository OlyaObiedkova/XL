# Означення змінних
x, y, z = symbols('x y z')

# Система рівнянь у GF(2)
equations = [
    x*y + y*z + z*x + 1,  # Приклад нелінійного рівняння
    x + y + z + 1,
    x*y*z + x + z
]

# Запускаємо алгоритм
solve_xl(equations, [x, y, z], degree=2, field_order=2)

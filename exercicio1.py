import random

x1 = float(input("Digite o parametro de x1:"))
x2 = float(input("Digite o parametro de x2:"))

w1 = round(random.uniform(-1, 1), 2)
w2 = round(random.uniform(-1, 1), 2)
b = round(random.uniform(-1, 1), 2)

# w1 = float(input("Digite o parametro de w1:"))
# w2 = float(input("Digite o parametro de w2:"))
# b = float(input("Digite o parametro de bias:"))

resultado = (x1 * w1) + (x2 * w2) + (b)

print(f"({x1} * {w1}) + ({x2} * {w2}) + {b} = {round(resultado, 2)}")

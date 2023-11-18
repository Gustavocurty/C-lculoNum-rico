from sympy import symbols, ln
from sympy.plotting import plot

x = symbols('x')

# Plota o gráfico da função
f_x = (x**3) - 10
p1 = plot(f_x, show=True)

# Define a função f(x)
def f(x): 
    fx = (x**3) -10
    return fx

# Define a função para calcular a derivada numericamente
def fLx(x):
    h = 0.0000001
    derivada = ((f(x + h) - f(x)) / h)
    return derivada

# Implementação do Método de Newton-Raphson
def newtonRaphson(fx, fLx, x, iter_max, tol):
    i = 0
    while i <= iter_max:
        x = x - fx(x) / fLx(x)
        i += 1
        
        if abs(fx(x)) < tol:
            print("O numero de iteraçoes foi:",i)
            return 'A raiz aproximada é', x
    return 'O método falhou após', i, 'iterações'

# Chamar a função Newton-Raphson
resultado = newtonRaphson(f, fLx, 1, 100, 1e-8)
print(resultado)

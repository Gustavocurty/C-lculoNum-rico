import sympy as sp
from math import e

def trapezoidal_rule(func, a, b, n):
    x = sp.symbols('x')
    h = (b - a) / n
    xi = a
    integral_value = 0

    for _ in range(n + 1):
        integral_value += func.subs(x, xi)
        xi += h

    integral_value *= h / 2
    return integral_value

def simpsons_rule(func, a, b, n):
    x = sp.symbols('x')
    h = (b - a) / n
    xi = a
    integral_value = func.subs(x, a) + func.subs(x, b)

    for i in range(1, n):
        if i % 2 == 0:
            integral_value += 2 * func.subs(x, xi)
        else:
            integral_value += 4 * func.subs(x, xi)
        xi += h

    integral_value *= h / 3
    return integral_value

def calculate_reference(func, a, b):
    x = sp.symbols('x')
    reference = sp.integrate(func, (x, a, b))
    return reference.evalf()

def calculate_approximation_error(approximation, reference):
    return abs(approximation - reference)

def calculate_relative_percent_error(approximation, reference):
    return (abs(approximation - reference) / abs(reference)) * 100

def main():
    x = sp.symbols('x')
    expression = sp.sympify(input("Digite a expressão da função em termos de x: "))
    a = float(input("Digite o valor de a (limite inferior): "))
    b = float(input("Digite o valor de b (limite superior): "))
    n = int(input("Digite o número de subintervalos (n): "))

    trapezoidal_result = trapezoidal_rule(expression, a, b, n)
    simpsons_result = simpsons_rule(expression, a, b, n)

    reference = calculate_reference(expression, a, b)

    trapezoidal_error = calculate_approximation_error(trapezoidal_result, reference)
    trapezoidal_relative_error = calculate_relative_percent_error(trapezoidal_result, reference)

    simpsons_error = calculate_approximation_error(simpsons_result, reference)
    simpsons_relative_error = calculate_relative_percent_error(simpsons_result, reference)

    print("\nResultados:")
    print(f"Resultado usando a regra do trapézio: {trapezoidal_result}")
    print(f"Resultado usando a regra de Simpson: {simpsons_result}")
    print(f"Valor de referência (integral exata): {reference}")
    print("\nErros:")
    print(f"Erro absoluto para a regra do trapézio: {trapezoidal_error}")
    print(f"Erro relativo percentual para a regra do trapézio: {trapezoidal_relative_error:.2f}%")
    print(f"Erro absoluto para a regra de Simpson: {simpsons_error}")
    print(f"Erro relativo percentual para a regra de Simpson: {simpsons_relative_error:.2f}%")

if __name__ == "__main__":
    main()

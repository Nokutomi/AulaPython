class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b
    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b
    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b
    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calc = Calculadora()
# print(calc.valor_b)
print(calc.soma(10,2))
print(calc.subtracao(2, 2))
print(calc.multiplicacao(8,1))
print(calc.divisao(9,2))


# print(soma(1,3))
# print(subtracao(1,3))
# print(multiplicacao(1,3))
# print(divisao(1,3))



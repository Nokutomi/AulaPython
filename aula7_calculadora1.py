class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b
    def subtracao(self):
        return self.valor_a - self.valor_b
    def multiplicacao(self):
        return self.valor_a * self.valor_b
    def divisao(self):
        return self.valor_a / self.valor_b

calc = Calculadora(10,2)
print(calc.valor_b)
print(calc.soma())
print(calc.subtracao())
print(calc.multiplicacao())
print(calc.divisao())


# print(soma(1,3))
# print(subtracao(1,3))
# print(multiplicacao(1,3))
# print(divisao(1,3))



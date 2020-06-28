a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {sum}.'
      '\nSubtracao: {sub}.'
      '\nMultiplicacao: {mult}.'
      '\nDivisao: {div}.'
      '\nResto: {res}.'
      .format(sum=soma, sub=subtracao, mult=multiplicacao, div=divisao, res=resto))

print(resultado)


# # print(type(soma))
# # soma = str(soma)
# # print(type(soma))
# print("soma: " + str(soma))
# print('subtracao: ' + str(subtracao))
# print(multiplicacao)
# # print(type(divisao))
# print(int(divisao))
# print(resto)
# # x = '1'
# # soma2 = int(x) + 1
# # print(soma2)
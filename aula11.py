
lista = [1,10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 0
    # numero = lista[3]
    # x = a
    # print('Fechando arquivo')
    # arquivo.close()
except ZeroDivisionError:
    print('Nao e possivel realizar uma divisao por zero')
except ArithmeticError:
    print('Houve um erro ao realizar uma operacao aritmetica')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando nao ocorre excecao')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()



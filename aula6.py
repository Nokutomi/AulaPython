conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}

conjunto_uniao = conjunto.union(conjunto2)
print('Uniao: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2)
print('Interseccao: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto.difference(conjunto2)
print('Diferenca entre 1 e 2: {}'.format(conjunto_diferenca1))

conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferenca entre 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferenca simetrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animal = set(lista)
print(conjunto_animal)
lista_animal = list(conjunto_animal)
print(lista_animal)





# conjunto = {1,2,3,4,4,2,2,2,2,2,2}
# conjunto.add(5)
# conjunto.discard(2)
# print(type(conjunto))
# print(conjunto)

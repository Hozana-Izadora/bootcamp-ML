# Escreva uma função que receba duas listas e retorne outra lista com os
# elementos que estão presentes em apenas uma das listas.

import random
def filtrar_unicos(lista1, lista2):
    lista_unicos = []
    for i in lista1:
        if i not in lista2:
            lista_unicos.append(i)
    for j in lista2:
        if j not in lista1:
            lista_unicos.append(j)
    return lista_unicos

lista1 = random.sample(range(1, 50), 10)
lista2 = random.sample(range(1, 50), 10)    
lista_unicos = filtrar_unicos(lista1, lista2)
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista de elementos unicos:")
print(sorted(lista_unicos))
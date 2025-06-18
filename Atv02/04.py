# Dada uma lista de números inteiros, escreva uma função para encontrar o
# segundo maior valor na lista.

import random
def segundo_maior(lista):
    if len(lista) < 2:
        return None 
    lista_ordenada = sorted(set(lista), reverse=True)
    if len(lista_ordenada) > 1:
        return lista_ordenada[1]
    else:
        return None
    
lista = random.sample(range(1, 50), 10)
segundo_maior_valor = segundo_maior(lista)
print("Lista:", lista)
print("Segundo maior valor:", segundo_maior_valor)
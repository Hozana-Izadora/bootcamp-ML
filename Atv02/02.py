#Escreva uma função que receba uma lista de números e retorne outra lista
#com os números primos presentes

import random
def filtrar_primos(lista):
    lista_primos = []
    for num in lista:
        if num > 1:  
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                lista_primos.append(num)
    return lista_primos

lista = random.sample(range(1, 50), 10)
lista_primos = filtrar_primos(lista)
print(lista)
print("Lista de numeros primos:")
print(lista_primos)
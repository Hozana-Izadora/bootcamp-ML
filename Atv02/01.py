#Escreva uma função que receba uma lista de números e retorne outra lista
#com os números ímpares.
import random

def filtrar_impares(lista):
    lista_impares = []
    for i in lista:
        if i % 2 != 0:
            lista_impares.append(i)
    return lista_impares

lista = random.sample(range(1, 50), 10) 
lista_impares = filtrar_impares(lista)
print(lista)
print("Lista de numeros ímpares:")
print(lista_impares) 
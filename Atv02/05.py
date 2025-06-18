# Crie uma função que receba uma lista de tuplas, cada uma contendo o
# nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das
# pessoas em ordem alfabética.

def ordenar_por_nome(lista_tuplas):
    return sorted(lista_tuplas, key=lambda pessoa: pessoa[0])

lista_pessoas = [
    ("Cinderela", 22),
    ("Fiona", 30),
    ("Branca de Neve", 25),
    ("Bela", 28),
    ("Aurora", 18),
    ("Ariel", 20),
    ("Rapunzel", 24),
    ("Jasmine", 26),
    ("Mulan", 27),
    ("Elsa", 29),
    ("Anna", 21),
    ("Moana", 23),
    ("Tiana", 31),
    ("Pocahontas", 19),
    ("Merida", 32)
]

lista_ordenada = ordenar_por_nome(lista_pessoas)
print("Lista de pessoas ordenada por nome:")

for pessoa in lista_ordenada:
    print(f"{pessoa[0]} - {pessoa[1]} anos")

# pregunta 01

import random

def numero_aleatorio():
    li=[]
    for i in range(0,10):
      li.append(random.randint(1, 20))
    return li

def lista_no_repetida(x):
    Lista_no_Repetida = []
    for i in x:
        if i not in Lista_no_Repetida:
            Lista_no_Repetida.append(i)

    return Lista_no_Repetida

def lista_ordenada(x):
    x.sort()
    print('Lista mayor a menor ------> ', x)
    x.reverse()
    print('Lista de menor a mayor----> ', x)
    return x

def maximo_valor(x):
    return x[0]

x = numero_aleatorio()
print('Lista Generada --------->  ', x)
x = lista_no_repetida(x)
print('Lista Sin repetidos ---->  ', x)
x = lista_ordenada(x)

print('El maximo valor de la lista es ----> ', maximo_valor(x))



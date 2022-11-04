# pregunta 03
import random
import time


def Medir_Tiempo(funcion):
    inicio = time.time()
    def funcion_numero(*dato, **ndato):
        resultado = funcion(*dato, **ndato)
        time.sleep(random.randint(1,2))
        print(resultado)
        print('Tiempo de Ejecución ---->: ', time.time())
        return resultado
    return funcion_numero

# ------
@Medir_Tiempo
def Division(a, b):
    return a/b
# prueba
Division(300, 10)
Division(20, 2)
Division(40, 8)

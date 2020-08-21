import threading
import time
import logging

from tiempo import Contador

# Para que logging imprima más info sobre los threads
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
# lo pone a dormir la cantidad de segundos "secs"
def dormir(secs):
    time.sleep(secs)


cont = Contador()

cont.iniciar()

lista = [] #crea una lista vacía

#un for con 10 iteraciones
for i in range(10):
    #crear un thead
    #se crea el hilo que llama a la funcion dormir por 1.5 segundos
    t = threading.Thread(target=dormir, args=[1.5])
    #lanzarlo
    t.start()
    # lo a grega a la lista
    lista.append(t)


#por cada hilo en la lista
for thread in lista:
    # lo finaliza con el join
    thread.join()

cont.finalizar()
cont.imprimir()
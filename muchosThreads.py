import threading
import time
import logging

from tiempo import Contador

# Para que logging imprima más info sobre los threads
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir(secs):
    time.sleep(secs)

cont = Contador()

cont.iniciar()

lista = [] #crea una lista vacía

for i in range(10):
    #crear un thead
    t = threading.Thread(target=dormir, args=[1.5])
    #lanzarlo
    t.start()
    lista.append(t)

for thread in lista:
    thread.join()

cont.finalizar()
cont.imprimir()
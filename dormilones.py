import time
import threading #hilos para concurrencia
import logging

from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


def dormir():
  time.sleep(1) #duerme por 1 seg


contador = Contador()


# ejemplo clásico secuencial
contador.iniciar()

dormir()
dormir()

contador.finalizar()
contador.imprimir()


# ejemplo con threads
contador.iniciar()

t1 = threading.Thread(target=dormir)
t2 = threading.Thread(target=dormir)

t1.start()
t2.start()

contador.finalizar()
contador.imprimir()


# ejemplo con threads, pero esperando que terminen
contador.iniciar()

t1 = threading.Thread(target=dormir)
t2 = threading.Thread(target=dormir)

t1.start()
t2.start()


t1.join() #esperá a que termine el lanzamiento del hilo t1
t2.join()

contador.finalizar()
contador.imprimir()

# Respuestas:
# 1) 
#  .En el caso secuencial da 2 seg., porque con el metodo dormir lo duerme 1 seg y se ejecuta dos veces.
#   Y por mas que se instancio el metodo dormir, el tiempo siguio pasando.
# .En el caso Thread da 0 seg., porque el metodo start indica que siga ejecutandose, y este no espera a que el 
#  metodo threading se ejecute y llega al metodo finalizar. Por ende el programa termina y los threads nunca se ejecutan.
# .En el caso de Trhead con join da 1 seg. porque el metodo join espera a que el hilo se ejecute y
#  luego finaliza, pero como los dos hilos correrieron al mismo tiempo se ejecuta uno solo.

# 2)
# . En el caso secuencial no hay hilos.
# . En el caso con Thread y de Thread con join hay 2 hilos.
# 
# 3) 
# La diferencia es el metodo join que obliga esperar a que los hilos se ejecuten.
# 
# 4)
# La desventaja es que el problema da solucion a un solo Thread y si tengo mas acciones que se pisan, 
# tendria que instanciar varios join. Y no es una solucion correcta porque habria ocupacion de memoria innecesaria
# y el codigo no seria legible a la hora de interpretarlo.   
  


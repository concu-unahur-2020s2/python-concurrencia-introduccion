import threading

THREADS = 2
MAX_COUNT = 1000000

counter = 0


def cuenta():
    global counter

    for i in range(int(MAX_COUNT/THREADS)):
        counter += 1



threads = []

for i in range(THREADS):
    t = threading.Thread(target=cuenta)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Valor del contador: {counter}")

# Respuestas:
# 1) El for se ejecuta 500000 . El primer for incrementa a counter en 1. el segundo for llama al metodo cuenta,
#   lo agrega en una lista de threads a cada thread y llama a la funcion star para que se ejecute. 
#   Y el ultimo for agrega un join a cada thread para que el metodo start no pise al metodo cuenta y los trheads
#   puedan finalizar.
# 
# 2) Si
# 
# 3) Si, eso lo hace el metodo join
# 
# 4) 500000
# 
# 5) Lo que observo es que cada vez que lo corro aumenta el counter cada vez mas.
#   Porque cada vez mas threads se van ejecutando. 


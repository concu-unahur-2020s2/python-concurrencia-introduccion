import threading

THREADS = 2
MAX_COUNT = 1000000

counter = 0


def cuenta():
    global counter

#contador +1 tantas veces como MAX_COUNT divido THREADS (500000) en este caso.
    for i in range(int(MAX_COUNT/THREADS)):
        counter += 1



threads = []

# crea un hilo definido por el valor THREADS (2), en cada hilo llama a la funcion cuenta()
for i in range(THREADS):
    t = threading.Thread(target=cuenta)
    threads.append(t)
    t.start()

# como el contador es compartido el valor final es indefinido.
# al ser otro for el del join no espera a que uno finalice para lanzar el siguiente.
for t in threads:
    t.join()
print(threads)
print(f"Valor del contador: {counter}")


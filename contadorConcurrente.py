import threading

THREADS = 2
MAX_COUNT = 1e6

counter = 0


def cuenta():
    global counter

    for i in range(int(MAX_COUNT/THREADS)):
        counter += 1 # seccion critica parte de codigo q quiere hacerder los theards



threads = []

for i in range(THREADS):
    t = threading.Thread(target=cuenta)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Valor del contador: {counter}")


from threading import Thread
import time

def say_hello(name):
    print (name, "Hola")

t = Thread(target=say_hello, args=("world",))
t.start()
t.join()
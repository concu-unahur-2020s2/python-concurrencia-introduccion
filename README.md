# To `join()` or not to `join()`...

En `dormilones.py` vimos tres ejemplos básicos de ejecución:

- Clásico secuencial,
- Con threads,
- Y con threads, pero esperando a que terminen usando `join()`.

Entonces responda:
- ¿Por qué los segundos que se imprimen que pasaron son 2, 0 y 1 (aprox.) respectivamente?
- ¿Cuántos hilos o threads hay en cada caso?
- Los últimos dos ejemplos tienen la misma cantidad de threads cada uno, ¿cuál sería la diferencia entonces?
- En el último ejemplo, ¿qué desventaja o desventajas le ve al uso del `join()`?


# Muchos threads

En `muchosThreads.py` hay algunas cosas básicas de Python:
- `from tiempo import Contador` importa desde `tiempo.py` la clase `Contador`.
- Cómo crear una lista vacía.
- Cómo hacer un loop con cantidad de iteraciones fija.
- Cómo agregar elementos (al final) a una lista.
- Cómo hacer un loop que itere sobre una lista.

## Parte 1
Mirá el código y fijate de entender la sintaxis. 

## Parte 2
Ahora corré el script: ¿por qué tarda lo que tarda? 


# Intercalación en concurrencia

**Dos reglas importantes** para `contadorConcurrente.py`:
- Mirá el código pero _no lo ejecutes_,
- Mirá el código pero _no lo ejecutes_.

(Referencia [The First Rule of Fight Club (1999)](https://www.youtubdC1yHLp9bWAe.com/watch?v=))

Mirando el código de `contadorConcurrente.py`, pero sin ejecutarlo:
- Al ejecutar la función `cuenta()`, ¿cuántas veces se ejecuta el `for` que tiene adentro, y qué hace cada iteración del `for`?
- ¿Es verdad que cada thread lanza una ejecución de la función `cuenta()`?
- ¿Es verdad que se está esperando a que termine cada thread?
- ¿Cúal te parece que es el valor que se imprime de `counter`?

Ahora corré `contadorConcurrente.py`:
- Correlo varias veces, ¿qué observás que pasa?
- ¿Por qué está pasando eso que observás?

RESPUESTAS

- El for se va a ejecutar la cantidad de THEADS pasados por parametros.
 en la primer iteracion crea un thead, lo agrega a la lista theads y luego lo incia
 -si cada thead lanza la ejcucion de ctas
 -si se espera que ternime cada ejecucion
 -el counter imprimer 1e6


-en cada ejecucion el valor del counter varia
-Esto esta pasando por que los theads esta hacediendo al mismo recuriso(variable "counter" si esperar que termine la ejecucion de cada theads)


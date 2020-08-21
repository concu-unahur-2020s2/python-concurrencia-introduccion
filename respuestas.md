# To `join()` or not to `join()`...

En `dormilones.py` vimos tres ejemplos básicos de ejecución:

- Clásico secuencial,
- Con threads,
- Y con threads, pero esperando a que terminen usando `join()`.

Entonces responda:
- ¿Por qué los segundos que se imprimen que pasaron son 2, 0 y 1 (aprox.) respectivamente?

Porque en el primer caso se ejecuta de forma secuencial, sin hilos extras solo el
proceso principal.
En el segundo caso de forma concurrente, y en el tercer caso
se espera con un join a que el primer hilo finalice para
lanzar el segundo.

- ¿Cuántos hilos o threads hay en cada caso?

En el primer caso 1, en los otros dos, 2.

- Los últimos dos ejemplos tienen la misma cantidad de threads cada uno, ¿cuál sería la diferencia entonces?

La diferencia es que en uno se lanzan de forma simultanea y en el otro caso se espera a
que un hilo termine para lanzar el proximo.

- En el último ejemplo, ¿qué desventaja o desventajas le ve al uso del `join()`?

Se tiene mas control de que se esta ejecutando en cada momento pero no se
aprovecha la concurrencia.

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

Mas alla de que en algun punto todos los hilos se ejecutan
de forma recurrente debido a las diez iteraciones del for,
van lanzando de a una. Se genera el hilo y mediante
la funcion dormir los pone en sleep 1.5 segundos.
La ejecucion de los 10 hilos tarda 1.516 segundos




# Intercalación en concurrencia

**Dos reglas importantes** para `contadorConcurrente.py`:
- Mirá el código pero _no lo ejecutes_,
- Mirá el código pero _no lo ejecutes_.

(Referencia [The First Rule of Fight Club (1999)](https://www.youtube.com/watch?v=dC1yHLp9bWA))

`The first rule of fight club is you do not talk about fight club`

Mirando el código de `contadorConcurrente.py`, pero sin ejecutarlo:
- Al ejecutar la función `cuenta()`, ¿cuántas veces se ejecuta el `for` que tiene adentro, y qué hace cada iteración del `for`?
- ¿Es verdad que cada thread lanza una ejecución de la función `cuenta()`?
- ¿Es verdad que se está esperando a que termine cada thread?
- ¿Cúal te parece que es el valor que se imprime de `counter`?

Ahora corré `contadorConcurrente.py`:
- Correlo varias veces, ¿qué observás que pasa?
- ¿Por qué está pasando eso que observás?

Al usar el mismo contador el valor final es indefinido.

# ¿Secuencial clásico, concurrente o paralelo?

Para cada una de las siguiente situaciones, decidí si es secuencial clásico, concurrente o paralelo. Intentá justificar señalando las ideas esenciales de cada caso.

- Cuál persona de un total de 50 corre más rápido una maratón.
    - opción 1) Cada persona corre secuencialmente en la pista, y medimos cada tiempo.

    Secuencial, lo dice la misma oracion, es mas exacto pero tarda mucho para obtener un resultado final.

    - opción 2) Todas las personas corren en la misma pista, y la que llega primero listo.
    Concurrente,

		- Preguntas: ¿hay algún recurso compartido? ¿genera problemas?

		La pista es compartida, puede haber colisiones y embotellamiento.

    - opción 3) Cada persona corre en una pista distinta, todas al mismo tiempo.
    Paralelo.

		- Pregunta: ¿hay un aumento de recursos respecto al anterior?
		si, se requiere una pista por persona.

        - Pregunta: ¿pros y contras de cada opción?
        Se requieren mas recursos para comprar las pistas y una persona que controle el tiempo.

- Competencia de triples en basquet: quién mete más en 10 intentos.
    - opción 1) Cada persona secuencialmente realiza 10 intentos, y anotamos la cantidad de triples.
    Secuencial.
    - opción 2) Todas las personas tiran los 10 intentos al mismo tiempo.
	Concurrente.
        - Preguntas: ¿hay algún recurso compartido? ¿genera problemas?

        Si, el aro y no sabemos si la pelota tambien. Si ha pelotas suficientes algunos
        tiros chocaran con otros.

    - opción 3) Cada persona tira en un aro distinto, todas al mismo tiempo.
    Paralelo.

    - Pregunta: ¿pros y contras de cada opción?

    Muy buena opcion si tenes platas para comprar todo lo necesario.
    Te aseguras los resultados correctos en menos tiempo que de forma secuencial.
    Muchos recursos desaprovechados.

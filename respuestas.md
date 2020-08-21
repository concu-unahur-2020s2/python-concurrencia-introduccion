# Dormilones

En `dormilones.py` vimos tres ejemplos básicos de ejecución:

- Clásico secuencial,
- Con threads,
- Y con threads, pero esperando a que terminen usando `join()`.

Entonces responda:
- ¿Por qué los segundos que se imprimen que pasaron son 2, 0 y 1 (aprox.) respectivamente?

*Porque en el primer caso ejecuta todo de manera secuencial, osea, inicia, duerme 1 segundo, termina, vuelve a dormir 1 segundo y recién al final ese segundo sleep pasa a finalizar. En el segundo caso se ejecutan los dos sleep a la vez pero no espera a que terminen, cosa que si pasa en el tercero por medio de un .join().*

- ¿Cuántos hilos o threads hay en cada caso?

*En el primer caso hay un solo hizo, el principal.*
*En el segundo caso y tercer caso hay tres hilos, el principal y los dos creados (t1 y t2).*

- Los últimos dos ejemplos tienen la misma cantidad de threads cada uno, ¿cuál sería la diferencia entonces?

*La diferencia está en que al usar join el t2 espera que finalice el t1 primero.*

- En el último ejemplo, ¿qué desventaja o desventajas le ve al uso del `join()`?

*Se desaprovecha el paralelismo (esto casi seguro de que en este caso es paralelismo y no concurrencia), podrían ejecutarse las cosas a la vez y listo. La ventaja es que con el join() al menos tenemos un mejor control de cuando está ejecutandose cada cosa.*

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

*Al crear el thread se está pasando por parametro que el sleep dure 1.5 segundos.*


# Intercalación en concurrencia

**Dos reglas importantes** para `contadorConcurrente.py`:
- Mirá el código pero _no lo ejecutes_,
- Mirá el código pero _no lo ejecutes_.

<!-- (Referencia [The First Rule of Fight Club (1999)](https://www.youtube.com/watch?v=dC1yHLp9bWA)) --> 
*Comenté una linea, no se habla de eso profe.*

Mirando el código de `contadorConcurrente.py`, pero sin ejecutarlo:
- Al ejecutar la función `cuenta()`, ¿cuántas veces se ejecuta el `for` que tiene adentro, y qué hace cada iteración del `for`?

*Se ejecuta MAX_COUNT/THREADS de veces, en este caso serían 500mil veces. En cada iteración aumenta 1 al contador.*

- ¿Es verdad que cada thread lanza una ejecución de la función `cuenta()`?

*Sí, si no es pregunta capciosa y no estamos teniendo en cuenta el thread principal del programa.*

- ¿Es verdad que se está esperando a que termine cada thread?

*No, se están ejecutando todos los threads dentro de un for, el join está por fuera de este.*

- ¿Cúal te parece que es el valor que se imprime de `counter`?

*Pensaría que el valor planeado sería 500000, pero el hecho de que el join() esté por fuera del loop que los ejecuta me genera dudas.*

Ahora corré `contadorConcurrente.py`:
- Correlo varias veces, ¿qué observás que pasa?
- ¿Por qué está pasando eso que observás?

*En todas las ejecuciones me da un resultado distinto en el contador, de nuevo, mi razonamiento es que es debido a que el join no está en el for loop de las ejecuciones y eso está generando problemas. Mi teoría es que hay momentos en donde varios threads acceden al contador a la vez y se pierde un control sobre este.*

# ¿Secuencial clásico, concurrente o paralelo?

Para cada una de las siguiente situaciones, decidí si es secuencial clásico, concurrente o paralelo. Intentá justificar señalando las ideas esenciales de cada caso.

- Cuál persona de un total de 50 corre más rápido una maratón.
    - opción 1) Cada persona corre secuencialmente en la pista, y medimos cada tiempo.

        *Esta opción es secuencial clásica, todos están corriendo en distintos momentos.*

    - opción 2) Todas las personas corren en la misma pista, y la que llega primero listo.
		- Preguntas: ¿hay algún recurso compartido? ¿genera problemas?

        *Esta opción sería concurrente. Se comparte la pista lo cual podría entorpecer o generar problemas dependiendo del tamaño que esta posea.*

    - opción 3) Cada persona corre en una pista distinta, todas al mismo tiempo.
		- Pregunta: ¿hay un aumento de recursos respecto al anterior?
    
        *Sí, aumenta la cantidad de pistas utilizadas*

    - Pregunta: ¿pros y contras de cada opción?

        *En el primer caso se utiliza demasiado tiempo, no necesitamos muchos recursos en el sentido de que solo utilizamos una pista, pero tardaría demasiado en terminar su ejecución.*

        *En el segundo caso se intenta optimizar el tiempo y los recursos, usando una sola pista, pero perdemos información valiosa como la posición en que terminarian los demás, se tiene un menor control sobre los otros procesos que siguen corriendo, básicamente.*

        *El tercer caso es efectivo en el tiempo utilizado pero necesita muchos recursos, necesitariamos tener 50 pistas disponibles y es algo bastante imposible de conseguir.*

- Competencia de triples en basquet: quién mete más en 10 intentos.
    - opción 1) Cada persona secuencialmente realiza 10 intentos, y anotamos la cantidad de triples.

        *Es un caso secuencial clásico, cada persona está turnandose para cumplir sus intentos.*

    - opción 2) Todas las personas tiran los 10 intentos al mismo tiempo.
		- Preguntas: ¿hay algún recurso compartido? ¿genera problemas?

        *Es un caso concurrente. Se comparte el aro o los aros si se están usando los de ambos equipos al mismo tiempo, generaría problemas en los momentos que varios jugadores quieran encestar al mismo tiempo.*
    - opción 3) Cada persona tira en un aro distinto, todas al mismo tiempo.

        *Es un caso paralelo, están todos haciendo sus tiros a la vez pero en distintos aros.*

    - Pregunta: ¿pros y contras de cada opción?

        *El primer caso puede ser cumplido solo teniendo un aro y una pelota por lo que es más económico, pero tarda demasiado tiempo.*

        *El segundo caso ocupa menos tiempo que el primero pero necesita estar compartiendo aros o hasta incluso pelotas, se entorpece mucho.*

        *El tercer caso es el más cómodo para los jugadores y más efectivo en tiempo, pero requiere tener una X cantidad de aros y pelotas donde X es la cantidad de jugadores totales que están participando.*

# Heuristica
-Modoficaciones en run.py: 
El programa pide al usuario que introduzca el nivel de dificultad. En donde f es fácil, 
m es medio y d es díficil. Los niveles varian el nivel de profundidad de la busqueda, 3
para el nivel fácil, 4 para medio y 5 para díficil. En caso de introducir un caracter 
incorrecto se comienza la partida con el valor medio por defecto.

Luego pedirá que se indique quien va a comenzar, llamandose a la función auxiliar
empiezauser si es el usuario el que comienza. Del mismo modo en caso de dar una respuesta 
no valida se asignará el valor por defecto comenzando la maquina.

Finalmente se indica quien ha ganado la partida.

-Heuristica.py:
Existe una variable global juser que indica si el usuario(humano) es O ó X, por defecto
se inicia a O y solo puede ser modificado por la función empiezauser(solo se llama si 
el usuario elige empezar).

La heurística se calcula mediante la función h4 y la auxiliar adyacente3. En h4 se 
recorren todas las posiciones ocupadas en en tablero y se examinan para cada posión sus 
ocho casillas adyacentes utilizando la función auxiliar. Devolviendo la suma de todos los 
valores del tablero.

Adyacente3 devuelve la suma de las 3 casillas en la dirrección dada, con respecto a la 
dirrección dada (x,y) y el jugador dado que ocupa dicha casilla. En donde las casillas en blanco
suman 2, las del mismo jugador 4 y diferente jugador -4. Si dicha suma es superior a 12 
se suma 100 al valor que se devolverá. Finalmente si el jugador dado coincide con el 
valor de juser el valor devuelto será con signo opuesto. 

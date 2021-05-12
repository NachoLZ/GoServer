Integrantes:
Ignacio Lizana - ROL: 201673542-9
Nicolás Miranda - ROL: 201673583-6


Instrucciones de ejecución:

1.- Abrir un terminal en la carpeta, luego ejecutar el comando: "python servidor_intermediario.py"
2.- Abrir un segundo terminal en la carpeta, luego ejecutar el comando: "go run cachipun.go"
3.- Abrir un tercer terminal en la carpeta, luego ejecutar el comando: "python cliente.py"
4.- Para comenzar a jugar, escribir "ready?" y presionar ENTER en el tercer terminal, el cual está ejecutando cliente.py
5.- Hay un 20% de probabilidad de que el servidor cachipun retorne un "NO" por lo que hay que ejecutar todo denuevo, pero
si es que este está listo y retorna "OK", el juego comenzará y se le preguntará su jugada.
6.- La jugada se debe ingresar como una de estas opciones: "piedra", "papel", "tijera" y presionar ENTER
7.- Gana la partida el que obtenga primero los 3 puntos.
8.- Si se desea terminar el juego en cualquier momento, se debe escribir "terminar" y presionar ENTER 
9.- Cuando hay un ganador, se le avisa al cliente y este cierra automáticamente los servidores.


Cliente: cliente.py
Servidor Intermediario: servidor_intermediario.py
Servidor Cachipún: cachipun.go
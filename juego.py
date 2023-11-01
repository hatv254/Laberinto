"""
posiciones inicial y final son atributos de esta clase, reescribe todas tus funciones 
anteriores de forma que sean métodos de la clase y todo esté encapsulado.

"""
from pynput import keyboard as bk
import os

class Juego:
    global inicial 
    global final

    def __init__(self) -> None:
        listener = bk.Listener(on_release=self.on_key_release)
        listener.start()
        self.mostrarLaberinto()
        listener.join()

    posicion_personaje = [0, 0]

    def mostrarLaberinto():
        global laberinto
        # Limpia la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(fila):
            for x in range(columna):
                if posicion_personaje == [i, x]:
                    print("P", end="")
                else:
                    print(laberinto[i][x], end="")
            print("")


    def moverPersonaje(self, key):
        global posicion_personaje
        nueva_posicion = list(posicion_personaje)
        if key == bk.Key.up:
            nueva_posicion[0] -= 1
        elif key == bk.Key.down:
            nueva_posicion[0] += 1
        elif key == bk.Key.left:
            nueva_posicion[1] -= 1
        elif key == bk.Key.right:
            nueva_posicion[1] += 1
        # Verificar si la nueva posición es válida
        if (0 <= nueva_posicion[0] < fila
            and 0 <= nueva_posicion[1] < columna
            and laberinto[nueva_posicion[0]][nueva_posicion[1]] == "."):
            posicion_personaje = nueva_posicion
            self.mostrarLaberinto()
            self.verificar_final()

    def verificar_final():
        global fila, columna, posicion_personaje
        if posicion_personaje == [fila - 1, columna - 1]:
            exit()  # Finaliza el programa

    def on_key_release(self, key):
        if key in [bk.Key.up, bk.Key.down, bk.Key.left, bk.Key.right]:
            self.moverPersonaje(key)

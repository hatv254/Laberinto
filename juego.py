from pynput import keyboard as bk
import os, random, re

class Juego:
    def __init__(self, posicion_inicial:[], posicion_final:[], laberinto:list) -> None:
        self.posicion_final = posicion_final
        self.laberinto = laberinto
        self.posicion_personaje = posicion_inicial  # Iniciar en la fila 1
        listener = bk.Listener(on_release=self.on_key_release)
        listener.start()
        self.mostrarLaberinto()
        listener.join()

    def mostrarLaberinto(self):
        # Limpia la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(len(self.laberinto)):
            for x in range(len(self.laberinto[0])):
                if self.posicion_personaje == [i, x]:
                    print("P", end="")
                else:
                    print(self.laberinto[i][x], end="")
            print("")

    def moverPersonaje(self, key):
        nueva_posicion = self.posicion_personaje
        if key == bk.Key.up:
            nueva_posicion[0] -= 1
        elif key == bk.Key.down:
            nueva_posicion[0] += 1
        elif key == bk.Key.left:
            nueva_posicion[1] -= 1
        elif key == bk.Key.right:
            nueva_posicion[1] += 1
        # Verificar si la nueva posición es válida
        if (
            0 <= nueva_posicion[0] < len(self.laberinto)
            and 0 <= nueva_posicion[1] < len(self.laberinto[0])
            and self.laberinto[nueva_posicion[0]][nueva_posicion[1]] == "."
        ):
            self.posicion_personaje = nueva_posicion
            self.mostrarLaberinto()
            self.verificar_final()

    def verificar_final(self):
        if self.posicion_personaje == self.posicion_final:
            exit()  # Finaliza el programa

    def on_key_release(self, key):
        if key in [bk.Key.up, bk.Key.down, bk.Key.left, bk.Key.right]:
            self.moverPersonaje(key)


class JuegoArchivo(Juego):
    def __init__(self) -> None:
        laberinto = self.randomLaberinto()
        posicion_inicial = self.coordeneadasIniciales(laberinto)
        posicion_final = self.final(laberinto)
        laberinto = self.quitarPrimeraFila(laberinto)
        super().__init__(posicion_inicial=posicion_inicial, posicion_final=posicion_final, laberinto=laberinto)

    def quitarPrimeraFila(self, laberinto):
        return laberinto[1:]


    def coordeneadasIniciales(self, laberinto):
        coordenadasInicio = [int(laberinto[0][0]), int(laberinto[0][2])]  # Convertir a int
        return coordenadasInicio

    def final(self, laberinto):
        coordenadasFinal = [int(laberinto[0][4:6]), int(laberinto[0][7:9])]  # Convertir a int
        return coordenadasFinal

    def randomLaberinto(self):
        lista_Laberinto = os.listdir("Laberintos")
        laberinto = random.sample(lista_Laberinto, 1)
        # Leemos el archivo
        with open(f"Laberintos/{laberinto[0]}", 'r') as laberirnto:
            laberinto = list(laberirnto)
        # Limpiamos el mapa
        laberinto_limpio = [re.sub(r'[\n\[\],]', '', elemento) for elemento in laberinto]
        return laberinto_limpio

juego = JuegoArchivo()

from partida import Partida
from repository import Repository
from repository import GuardarPartida
import random


class ServicesPartidas:
    def __init__(self):
        self.repo_palabras = Repository.repositorioPalabras
        self.guardar = GuardarPartida

    def iniciar_partida(self, nombre_jugador, dificultad, palabra='',
                        tipo_palabra=''):
        if dificultad < 1 or dificultad > 10:
            raise ValueError("La dificultad debe comprender entre 1 y 10")
        if (len(palabra) == 0 or palabra is None and len(tipo_palabra) == 0 or
           tipo_palabra is None):
            randomKey = random.choice(list(self.repo_palabras.keys()))
            palabra = self.repo_palabras[randomKey]['palabra']
            tipo_palabra = self.repo_palabras[randomKey]['tipo_palabra']
        intentos = dificultad * len(palabra)
        partidaUno = Partida(palabra, intentos, tipo_palabra, nombre_jugador)
        key = partidaUno._nombre_jugador
        self.guardar.saves[key] = partidaUno.__dict__
        return partidaUno

    def get_random_palabra(self):
        randomKey = random.choice(list(self.repo_palabras.keys()))
        return self.repo_palabras[randomKey]

    def intentar_letra(self, partida, letra):
        partida._intentos = partida._intentos - 1
        if partida._intentos < 0:
            raise ValueError("No tienes mas intentos")
        for i in range(len(partida._palabra)):
            if letra == partida._palabra[i]:
                partida._palabra_aciertos[i] = letra
        if None in partida._palabra_aciertos:
            if partida._intentos == 0:
                return 'Perdio'
            else:
                return 'Continua'
        else:
            return 'Gano'

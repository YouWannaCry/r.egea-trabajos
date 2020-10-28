from repository import GuardarPartida
from servicesPartidas import ServicesPartidas


class Ahorcado:
    def menu_ahorcado(self):
        print('Seleccione 1 para Un Jugador, 2 para Dos Jugadores o cualquier otro numero para salir')
        return int(input('Elija una opción: '))

    def un_jugador(self):
        try:
            services = ServicesPartidas()
            _nombre = input('Ingrese su nombre: ')
            _dificultad = int(input('Ingrese la dificultad: '))
            partidaUno = services.iniciar_partida(_nombre, _dificultad)
            res = 'Continua'
            while res == 'Continua':
                letra = input('Ingrese una letra: ')
                if letra == 'salir':
                    return True
                res = services.intentar_letra(partidaUno, letra.upper())
                print(partidaUno._palabra_aciertos)
            if res == 'Gano':
                print('Muy bien {}'.format(_nombre))
                return True
            elif res == 'Perdio':
                print('Fallaste {} :('.format(_nombre))
                return True
        except StopIteration:
            return True
        except SystemExit:
            pass
        return True

    def dos_jugadores(self):
        services = ServicesPartidas()
        for i in range(0, 2):
            _nombre = input('Ingreme nombre PLAYER ONE {}: '
                            .format(i+1))
            _dificultad = int(input('Ingrese dificultad {}: '
                                    .format(_nombre)))
            _palabra = input('Ingrese palabra {}: '.format(_nombre))
            _tipo_palabra = input('Ingrese dificultad: ')
            i = services.iniciar_partida(_nombre, _dificultad, _palabra,
                                         _tipo_palabra)
            res = 'Continua'
            while res == 'Continua':
                letra = input('Ingrese una letra: ')
                if letra == 'salir':
                    return True
                res = services.intentar_letra(i, letra.upper())
                print(i._palabra_aciertos)
            if res == 'Gano':
                print('Muy bien {}'.format(_nombre))
            elif res == 'Perdio':
                print('Fallaste {} :('.format(_nombre))
        print(GuardarPartida.saves, "")
        return True

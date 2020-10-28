from ahorcado import Ahorcado

if __name__ == '__main__':
    juego = Ahorcado()
    opcion_menu = juego.menu_ahorcado()
    if opcion_menu == 1:
        print('SOLO-PLAYER')
        juego.un_jugador()
    if opcion_menu == 2:
        print('MULTI-PLAYER')
        juego.dos_jugadores()
    if opcion_menu < 1 or opcion_menu > 2:
        print('GG WP, cya later pal')

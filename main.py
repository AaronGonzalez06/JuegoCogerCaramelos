import pygame
import random
import math
from pygame import mixer
#from modelo import Iten
from modelo.Iten import Iten

pygame.init()
pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("halloween 2.0")
fondo = pygame.image.load("img/fondo.jpg")

icono = pygame.image.load("icono/veneno.png")
pygame.display.set_icon(icono)

#musica
mixer.music.load('audio/audio.mp3')
mixer.music.play(-1)

# jugador 1
Jugador = Iten(368, 460, 'img/dulcedehalloween.png', 0, 0,True,"jugador")
# ojo
enemigos = 9
objetos = []
Ojo = Iten(random.randint(0,710), -70, 'img/globocular.png', -1, 0.3,True,"ojo")
Ojo2 = Iten(random.randint(0,710), -100, 'img/globocular.png', -1, 0.2,True,"ojo")
Pocion = Iten(random.randint(0,710), -150, 'img/pocion.png', -5, 0.08,True,"pocion")
Pocion2 = Iten(random.randint(0,710), -600, 'img/pocion.png', -5, 0.08,True,"pocion")
Caramelo = Iten(random.randint(0,710), -500, 'img/caramelo.png', +3, 0.4,True,"caramelo")
Caramelo2 = Iten(random.randint(0,710), -1000, 'img/caramelo.png', +3, 0.4,True,"caramelo")
Pastel = Iten(random.randint(0,710), -500, 'img/pastel.png', +2, 0.25,True,"pastel")
Calabaza = Iten(random.randint(0,710), -1000, 'img/calabaza2.png', -10, 0.3,True,"calabaza")
Calabaza2 = Iten(random.randint(0,710), -2500, 'img/calabaza2.png', -10, 0.3,True,"calabaza")
objetos.append(Ojo)
objetos.append(Ojo2)
objetos.append(Pocion)
objetos.append(Pocion2)
objetos.append(Caramelo)
objetos.append(Caramelo2)
objetos.append(Pastel)
objetos.append(Calabaza)
objetos.append(Calabaza2)

img_jugador = pygame.image.load(Jugador.img)
img_iten = pygame.image.load(Ojo.img)
img_iten2 = pygame.image.load(Ojo2.img)
img_pocion = pygame.image.load(Pocion.img)
img_caramelo = pygame.image.load(Caramelo.img)
img_pastel = pygame.image.load(Pastel.img)
img_calabaza = pygame.image.load(Calabaza.img)



#puntuacion
puntuacion= 10
fuentePuntuacion = pygame.font.Font('fuente/CFHalloween-Regular.ttf',32)
Fuente = fuentePuntuacion.render(f"PUNTUACION {puntuacion}",True,(255,255,255))


def mostrar_puntuacion (x, y):
    Fuente = fuentePuntuacion.render(f"PUNTUACION {puntuacion}",True,(127,5,42))
    pantalla.blit(Fuente, (x,y))


def jugador(x,y):
    pantalla.blit(img_jugador, (x, y))

def punto():
    sonidoPuntos = mixer.Sound('audio/punto.mp3')
    sonidoPuntos.play()

def incorrecto():
    sonidoPuntos = mixer.Sound('audio/incorrecto.mp3')
    sonidoPuntos.play()

iniciando = True
while iniciando:
    #prueba iten
    #volver aqui si no funciona
    for e in range(enemigos):
        #objetos[e].velocidad = objetos[e].velocidad
        objetos[e].coordenaday += objetos[e].velocidad
        if objetos[e].coordenaday >0:
            objetos[e].visible = True
        if objetos[e].coordenaday > 600:
            objetos[e].visible = False
            if objetos[e].tipo == "calabaza":
                sonidoRisa = mixer.Sound('audio/risa.mp3')
                sonidoRisa.play()
                puntuacion -=10
            else:
                puntuacion -=1
            if not objetos[e].visible:
                objetos[e].coordenadax = random.randint(0,710)
                if objetos[e].tipo == "calabaza":
                    objetos[e].coordenaday = -3000
                else:
                    objetos[e].coordenaday = -70


    # fin pruebas
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(img_iten, (Ojo.coordenadax, Ojo.coordenaday))
    pantalla.blit(img_iten2, (Ojo2.coordenadax, Ojo2.coordenaday))
    pantalla.blit(img_pocion, (Pocion.coordenadax, Pocion.coordenaday))
    pantalla.blit(img_caramelo, (Caramelo.coordenadax, Caramelo.coordenaday))
    pantalla.blit(img_pastel, (Pastel.coordenadax, Pastel.coordenaday))
    pantalla.blit(img_calabaza, (Calabaza.coordenadax, Calabaza.coordenaday))
    pantalla.blit(img_calabaza, (Calabaza2.coordenadax, Calabaza2.coordenaday))
    pantalla.blit(img_pocion, (Pocion2.coordenadax, Pocion2.coordenaday))

    if Jugador.coordenadax < -1:
        Jugador.velocidad = 0
    if Jugador.coordenadax > 680:
        Jugador.velocidad = 0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            iniciando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key  == pygame.K_a:
                #print("A")
                Jugador.velocidad = -0.4
            if evento.key  == pygame.K_d:
                #print("D")
                Jugador.velocidad = 0.4

    Jugador.coordenadax += Jugador.velocidad
    jugador(Jugador.coordenadax, Jugador.coordenaday)

    for e in range(enemigos):
        distancia = math.sqrt(math.pow(Jugador.coordenadax - objetos[e].coordenadax, 2) + math.pow(Jugador.coordenaday - objetos[e].coordenaday, 2))
        if distancia <= 50:
            objetos[e].visible = False
            if not objetos[e].visible and objetos[e].tipo == "ojo":
                objetos[e].coordenadax = random.randint(0, 710)
                objetos[e].coordenaday = -70
                punto()
                puntuacion +=1
            elif not objetos[e].visible and objetos[e].tipo == "pocion":
                objetos[e].coordenadax = random.randint(0, 710)
                objetos[e].coordenaday = -70
                incorrecto()
                puntuacion +=objetos[e].puntos
            elif not objetos[e].visible and objetos[e].tipo == "caramelo":
                objetos[e].coordenadax = random.randint(0, 710)
                objetos[e].coordenaday = -70
                punto()
                puntuacion +=objetos[e].puntos
            elif not objetos[e].visible and objetos[e].tipo == "pastel":
                objetos[e].coordenadax = random.randint(0, 710)
                objetos[e].coordenaday = -70
                punto()
                puntuacion +=objetos[e].puntos
            elif not objetos[e].visible and objetos[e].tipo == "calabaza":
                objetos[e].coordenadax = random.randint(0, 710)
                objetos[e].coordenaday = -3000
                #punto()
                #puntuacion +=objetos[e].puntos

    if puntuacion <= 0:
        for e in range(enemigos):
            objetos[e].velocidad = 0
            objetos[e].coordenadax = 100
            objetos[e]. coordenaday = -100
        Jugador.velocidad = 0
        fuenteFinJuego = pygame.font.Font('fuente/CFHalloween-Regular.ttf', 32)
        Fuente = fuenteFinJuego.render(f"FIN DEL JUEGO", True, (127,5,42))
        pantalla.blit(Fuente, (250, 280))
        mixer.music.pause()
        sonidoPuntos = mixer.Sound('audio/grito.mp3')
        sonidoPuntos.play()
    mostrar_puntuacion(10,10)
    if puntuacion >= 30:
        objetos[0].velocidad = 0.4
        objetos[1].velocidad = 0.4
        objetos[2].velocidad = 0.05
        objetos[3].velocidad = 0.05
        objetos[4].velocidad = 0.5
        objetos[5].velocidad = 0.5
        objetos[6].velocidad = 0.4
        objetos[7].velocidad = 0.6
        objetos[8].velocidad = 0.6
    if puntuacion < 30:
        objetos[0].velocidad = 0.3
        objetos[1].velocidad = 0.2
        objetos[2].velocidad = 0.08
        objetos[3].velocidad = 0.08
        objetos[4].velocidad = 0.4
        objetos[5].velocidad = 0.4
        objetos[6].velocidad = 0.25
        objetos[7].velocidad = 0.3
        objetos[8].velocidad = 0.3
    pygame.display.update()
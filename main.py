# Para el funcionamiento correcto, hay que instlar todas laslibrerías, pygame, matplotliib, numpy.
# pip install numpy / Para numpy
# pip install pygame / Para pygame
# pip install matplotlib / Para matplotlib
from functions import * # Importa funciones personalizadas
from winotify import Notification # Importa la notificación de Windows

# Solicita al usuario ingresar una velocidad
velocidad = float(input("Ingrese una velocidad: "))

# Variables de control
entrar = True # Controla el bucle inicial

# Importa librerías
import pygame, random
import math
import random

# Configuración inicial de Pygame
pygame.init()
window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

# Evento para generar bolas de fuego
fire_ball_event = pygame.USEREVENT
pygame.time.set_timer(fire_ball_event, 200)

# Creación de la bola de fuego y configuración de dimensiones
fireball = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(fireball, "yellow", (10, 10), 10)
pygame.draw.circle(fireball, "orange", (10, 13), 7)
pygame.draw.circle(fireball, "red", (10, 16), 4)

fireball_rect = None  # Variable para controlar la única bola que cae
event_active = True  # Variable para controlar si el evento está activo

# Bucle principal del juego de las bolas de fuego
run = True
while run:
    clock.tick(100) # Limita la velocidad de actualización
    
    # Manejo de eventos de Pygame
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # Si se cierra la ventana, termina el juego
            run = False 
            # Si se activa el evento de bola de fuego y está activo y no hay bola cayendo
        if event.type == fire_ball_event and event_active and fireball_rect is None:
            # Genera una posición aleatoria para la bola de fuego
            x = random.randrange(10, window.get_width()-10)
            fireball_rect = pygame.Rect(x, -20, 20, 20)
            event_active = False  # Desactivar el evento después de lanzar la bola
    
    # Mueve la bola de fuego si existe y controla si sale de la pantalla    
    if fireball_rect is not None:
        fireball_rect.y += 1
        if fireball_rect.top > window.get_height():
            fireball_rect = None
    # Actualiza la ventana del juego
    window.fill(0)
    if fireball_rect is not None:
        window.blit(fireball, fireball_rect)
    pygame.display.flip()

pygame.quit()  # Cierra Pygame

# Inicia un bucle nuevo para controlar el lanzamiento del proyectil
while  entrar:
    # Verifica si la velocidad ingresada es mayor a 90 y solicita otra velocidad
    if  velocidad > 90:
        velocidad = float(input("Ingrese una velocidad: "))
        
    # Verifica si la velocidad está en el rango válido y sale del bucle
    if 1 <= velocidad <= 90:    
        entrar = False  
        
    pygame.init()
    # Notificación de datos válidos
    toast = Notification(app_id="Tiro parabólico",
    title="Velocidad  válida",
    msg="Tiro parabólico",
    icon=r"C:\Users\NICO-PC\Desktop\cohete.png")
    toast.show() 
    # Configuración de la ventana y pantalla del juego del proyectil
    # (configuración de resolución, colores, fuentes, etc.) 
SCREEN = WIDTH, HEIGHT = 1200, 600

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 60
# Define constantes y colores
BLACK = (18, 18, 18)
WHITE = (217, 217, 217)
RED = (252, 91, 122)
GREEN = (29, 161, 16)
BLUE = (78, 193, 246)
ORANGE = (252,76,2)
YELLOW = (254,221,0)
PURPLE = (155,38,182)
AQUA = (0,249,182)

COLORS = [RED, GREEN, BLUE, ORANGE, YELLOW, PURPLE]

font = pygame.font.SysFont('verdana', 12)

origin = (30, 340)
radius = 13



g = 9.8

# Crea una clase para el proyectil que calcula y dibuja la trayectoria

class Projectile(pygame.sprite.Sprite):
            def __init__(self, velocidad, theta):
                super(Projectile, self).__init__()

                self.velocidad = velocidad
                self.theta = toRadian(abs(theta))
                self.x, self.y = origin
                
                self.color = random.choice(COLORS)

                self.ch = 0
                self.dx = 2
                
                self.f = self.getTrajectory()
                self.range = self.x + abs(self.getRange())

                self.path = []

            def timeOfFlight(self):
                return round((2 * self.velocidad * math.sin(self.theta)) / g, 2)

            def getRange(self):
                range_ = ((self.velocidad ** 2) * 2 * math.sin(self.theta) * math.cos(self.theta)) / g
                return round(range_, 2)

            def getMaxHeight(self):
                h = ((self.velocidad ** 2) * (math.sin(self.theta)) ** 2) / (2 * g)
                return round(h, 2)

            def getTrajectory(self):
                return round(g /  (2 * (self.velocidad ** 2) * (math.cos(self.theta) ** 2)), 4)

            def getProjectilePos(self, x):
                return x * math.tan(self.theta) - self.f * x ** 2

            def update(self):
                if self.x >= self.range:
                    self.dx = 0
                self.x += self.dx
                self.ch = self.getProjectilePos(self.x - origin[0])

                self.path.append((self.x, self.y-abs(self.ch)))
                self.path = self.path[-50:]

                pygame.draw.circle(win, self.color, self.path[-1], 5)
                pygame.draw.circle(win, WHITE, self.path[-1], 5, 1)
                for pos in self.path[:-1:5]:
                    pygame.draw.circle(win, WHITE, pos, 1)
# Grupo de sprites para los proyectiles
projectile_group = pygame.sprite.Group()

clicked = False
currentp = None

# Variables para el control del ángulo y la posición del proyectil
# (control de clics del mouse, ángulos, etc.)
theta = -30
end = getPosOnCircumeference(theta, origin)
arct = toRadian(theta)
arcrect = pygame.Rect(origin[0]-30, origin[1]-30, 60, 60)


running = True
# Bucle principal del juego del proyectil
while running:
        win.fill(BLACK)
        # Lógica para manejar eventos de Pygame
        # (incluye acciones al presionar teclas, clics del mouse, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False

                if event.key == pygame.K_r:
                    projectile_group.empty()
                    currentp = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False

                pos = event.pos
                theta = getAngle(pos, origin)
                if -90 < theta <= 0:
                    projectile = Projectile(velocidad, theta)
                    projectile_group.add(projectile)
                    currentp = projectile

            if event.type == pygame.MOUSEMOTION:
                if clicked:
                    pos = event.pos
                    theta = getAngle(pos, origin)
                    if -90 < theta <= 0:
                        end = getPosOnCircumeference(theta, origin)
                        arct = toRadian(theta)
        # Dibuja la interfaz gráfica del juego del proyectil
        # (trayectoria, ángulos, información en pantalla, etc.)
        pygame.draw.line(win, WHITE, origin, (origin[0] + 1160, origin[1]), 2)
        pygame.draw.line(win, WHITE, origin, (origin[0], origin[1] - 270), 2)
        pygame.draw.line(win, WHITE, origin, end, 1)
        pygame.draw.circle(win, WHITE, origin, 6)
        pygame.draw.arc(win, AQUA, arcrect, 0, -arct, 1)

        projectile_group.update() # Actualiza y muestra la información sobre la trayectoria y proyectiles en pantalla

        # Info *******************************************************************
        title = font.render("Movimiento Parabólico", True, WHITE)
        fpstext = font.render(f"FPS : {int(clock.get_fps())}", True, WHITE)
        thetatext = font.render(f"Ángulo : {int(abs(theta))}", True, WHITE)
        degreetext = font.render(f"{int(abs(theta))}°", True, YELLOW)
        win.blit(title, (80, 30))
        win.blit(fpstext, (20, 400))
        win.blit(thetatext, (20, 420))
        win.blit(degreetext, (origin[0]+38, origin[1]-20))

        if currentp:
            veltext = font.render(f"Velocidad : {currentp.velocidad}m/s", True, WHITE)
            timetext = font.render(f"Tiempo : {currentp.timeOfFlight()}s", True, WHITE)
            rangetext = font.render(f"Alcance horizontal : {currentp.getRange()}m", True, WHITE)
            heighttext = font.render(f"Alcance vertical : {currentp.getMaxHeight()}m", True, WHITE)
            win.blit(veltext, (WIDTH-240, 400))
            win.blit(timetext, (WIDTH-240, 420))
            win.blit(rangetext, (WIDTH-240, 440))
            win.blit(heighttext, (WIDTH-240, 460))

        pygame.draw.rect(win, (0,0,0), (0, 0, WIDTH, HEIGHT), 5)
        clock.tick(FPS)
        pygame.display.update()
pygame.quit() # Cierra Pygame al salir del bucle del juego del proyectil



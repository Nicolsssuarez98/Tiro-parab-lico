import pygame, random

# Inicializar Pygame
pygame.init()

# Crear la ventana del juego
window = pygame.display.set_mode((600, 600))

# Inicializar el reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Crear un evento personalizado para lanzar bolas de fuego
fire_ball_event = pygame.USEREVENT
pygame.time.set_timer(fire_ball_event, 200)

# Crear la superficie de la bola de fuego y definir sus círculos y colores
fireball = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(fireball, "yellow", (10, 10), 10)
pygame.draw.circle(fireball, "blue", (10, 13), 7)
pygame.draw.circle(fireball, "red", (10, 16), 4)

fireball_rect = None  # Variable para controlar la única bola que cae
event_active = True  # Variable para controlar si el evento está activo

run = True
while run:
    clock.tick(100)  # Limitar la velocidad del juego a 100 FPS

    # Manejar los eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si se cierra la ventana
            run = False 
        if event.type == fire_ball_event and event_active and fireball_rect is None:
            # Generar una posición aleatoria para la bola de fuego
            x = random.randrange(10, window.get_width()-10)
            fireball_rect = pygame.Rect(x, -20, 20, 20)
            event_active = False  # Desactivar el evento después de lanzar la bola

    if fireball_rect is not None:
        # Mover la bola de fuego hacia abajo
        fireball_rect.y += 1
        if fireball_rect.top > window.get_height():
            # Si la bola de fuego sale de la ventana, restablecerla a None
            fireball_rect = None

    window.fill(0)  # Limpiar la pantalla con un color negro

    if fireball_rect is not None:
        # Mostrar la bola de fuego en la ventana si existe
        window.blit(fireball, fireball_rect)

    pygame.display.flip()  # Actualizar la pantalla

pygame.quit()
exit()

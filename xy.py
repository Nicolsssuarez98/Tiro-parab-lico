import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Función para calcular la posición en x e y en función del tiempo
def posicion(t, v0, theta):
    g = 9.81  # Aceleración debido a la gravedad en m/s^2
    # Cálculo de las posiciones en x e y
    x = v0 * np.cos(np.radians(theta)) * t
    y = v0 * np.sin(np.radians(theta)) * t - 0.5 * g * t**2
    return x, y

# Parámetros iniciales
velocidad_inicial = 20  # en m/s
angulo = 45  # en grados

# Tiempo de simulación
tiempo_total = 2 * velocidad_inicial * np.sin(np.radians(angulo)) / 9.81
tiempo = np.linspace(0, tiempo_total, 100)  # 100 puntos de tiempo

# Calcula las posiciones x e y en función del tiempo
posicion_x, posicion_y = posicion(tiempo, velocidad_inicial, angulo)

# Configuración inicial del gráfico
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 6))
ax1.set_xlim(0, tiempo_total * velocidad_inicial * np.cos(np.radians(angulo)) * 0.09)
ax1.set_ylim(0, max(posicion_x) * 1.2)
ax2.set_xlim(0, tiempo_total * velocidad_inicial * np.cos(np.radians(angulo)) * 0.09)
ax2.set_ylim(0, max(posicion_y) * 1.2)
ax3.set_xlim(0, max(posicion_x) * 1.2)
ax3.set_ylim(0, max(posicion_y) * 1.2)
ax4.set_xlim(0, max(posicion_x) * 1.2)
ax4.set_ylim(0, max(posicion_y) * 1.2)

line1, = ax1.plot([], [], lw=3)
line2, = ax2.plot([], [], lw=3)
line3, = ax3.plot([], [], lw=3)
line4, = ax4.plot([], [], lw=3)

lines = [line1, line2, line3, line4]

# Función de inicialización para la animación
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Función de animación que actualiza los datos en cada cuadro
def animate(i):
    # Posición en x vs Tiempo
    lines[0].set_data(tiempo[:i], posicion_x[:i])
    # Posición en y vs Tiempo
    lines[1].set_data(tiempo[:i], posicion_y[:i])
    # Posición en y vs Posición en x
    lines[2].set_data(posicion_x[:i], posicion_y[:i])
    # Trayectoria
    lines[3].set_data(posicion_x[:i], posicion_y[:i])
    return lines

# Crea la animación
anim = FuncAnimation(fig, animate, init_func=init, frames=len(posicion_x), interval=50, blit=True)

ax1.set_title('Posición en x vs Tiempo')
ax1.set_xlabel('Tiempo (s)')
ax1.set_ylabel('Posición en x (m)')
ax2.set_title('Posición en y vs Tiempo')
ax2.set_xlabel('Tiempo (s)')
ax2.set_ylabel('Posición en y (m)')
ax3.set_title('Posición en y vs Posición en x')
ax3.set_xlabel('Posición en x (m)')
ax3.set_ylabel('Posición en y (m)')
ax4.set_title('Trayectoria del tiro parabólico')
ax4.set_xlabel('Posición en x (m)')
ax4.set_ylabel('Posición en y (m)')

plt.tight_layout()
plt.show()

import matplotlib 
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Trazar una caminata

rw = RandomWalk(50_000)
rw.fill_walk()

while True:

    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Trazar los puntos
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))

    # Aniadir estilos al princio de los puntos
    point_number = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, 
               c=point_number, cmap=plt.cm.Blues, 
               edgecolors='none', s=20)

    ax.set_aspect('equal')

    # Marcar el primer punto y el ultimo
    # Primeros puntos [y=0, x=0]
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # Ultimops puntos [y=4999, x=4999]
    ax.scatter(rw.x_values[-1], rw.y_values[-1], 
               c='red', edgecolors='none',
               s=60)

    # Eliminar los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk (y/n)? ")
    if keep_running == 'n':
        break

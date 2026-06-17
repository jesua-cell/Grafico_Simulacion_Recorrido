from random import choice

class RandomWalk:

    def __init__(self, num_points=5000):

        # Puntos de la caminata
        self.num_points = num_points
        # Caminas (x, y)
        self.x_values = [0]
        self.y_values = [0]

    # Calcular los puntos del paseo
    def fill_walk(self):

        # Ejecutar hasta que llega a la longitud indicada
        while len(self.x_values) < self.num_points:

            # 1 
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 4])
            x_step = x_direction * x_distance

            # 2 
            y_direction = choice([1, -1]);
            y_distance = choice([0, 1, 2, 4])
            y_step = y_direction * y_distance

            # 3 
            if x_step == 0 and y_step == 0:
                continue

            # 4
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # 5
            self.x_values.append(x)
            self.y_values.append(y)



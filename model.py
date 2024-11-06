from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from agente_vehiculo import Vehicle
from agente_avenida import Road
import random
from mesa.time import SimultaneousActivation


class TrafficModel(Model):
    def __init__(self, width, height, num_vehicles):
        super().__init__()
        self.grid = MultiGrid(width, height, True)
        self.schedule = SimultaneousActivation(self)

        # Crear calles y avenidas alrededor de cada cuadra con sentido único
        for x in range(width):
            for y in range(height):
                # Define las avenidas alrededor de las cuadras de 4x4 con sentido único
                if x % 6 == 0:  # Avenida vertical derecha de la cuadra (Norte)
                    road = Road(f"road_{x}_{y}", self, direction='N')
                    self.grid.place_agent(road, (x, y))
                # Avenida vertical izquierda de la cuadra (Sur)
                elif x % 6 == 1:
                    road = Road(f"road_{x}_{y}", self, direction='S')
                    self.grid.place_agent(road, (x, y))
                # Avenida horizontal arriba de la cuadra (Este)
                elif y % 6 == 0:
                    road = Road(f"road_{x}_{y}", self, direction='E')
                    self.grid.place_agent(road, (x, y))
                # Avenida horizontal abajo de la cuadra (Oeste)
                elif y % 6 == 1:
                    road = Road(f"road_{x}_{y}", self, direction='W')
                    self.grid.place_agent(road, (x, y))

        # Añadir vehículos solo en las avenidas
        for i in range(num_vehicles):
            # Seleccionar solo celdas en avenidas para colocar los vehículos
            possible_positions = [(x, y) for x in range(width) for y in range(
                height) if (x % 6 in [0, 1] or y % 6 in [0, 1])]
            x, y = self.random.choice(possible_positions)
            # Colocar los vehículos de acuerdo con el sentido de la avenida en esa celda
            if x % 6 == 0:
                initial_direction = 'N'
            elif x % 6 == 1:
                initial_direction = 'S'
            elif y % 6 == 0:
                initial_direction = 'E'
            elif y % 6 == 1:
                initial_direction = 'W'
            vehicle = Vehicle(i, self, initial_direction)
            self.grid.place_agent(vehicle, (x, y))
            self.schedule.add(vehicle)

    def step(self):
        self.schedule.step()

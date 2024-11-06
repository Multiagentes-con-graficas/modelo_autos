from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from agente_avenida import Road
import random


class Vehicle(Agent):
    def __init__(self, unique_id, model, direction):
        super().__init__(unique_id, model)
        self.direction = direction

    def step(self):
        self.move()

    def move(self):
        x, y = self.pos

        if x == 0 and self.direction == 'W':
            self.direction = 'S' if random.choice([True, False]) else 'E'
        elif x == self.model.grid.width - 1 and self.direction == 'E':
            self.direction = 'N' if random.choice([True, False]) else 'W'
        elif y == 0 and self.direction == 'S':
            self.direction = 'E' if random.choice([True, False]) else 'N'
        elif y == self.model.grid.height - 1 and self.direction == 'N':
            self.direction = 'W' if random.choice([True, False]) else 'S'

        elif self.is_corner(x, y):
            if random.choice([True, False]):
                self.turn_corner(x, y)

        if self.direction == 'N':
            new_position = (x, y + 1)
        elif self.direction == 'S':
            new_position = (x, y - 1)
        elif self.direction == 'E':
            new_position = (x + 1, y)
        elif self.direction == 'W':
            new_position = (x - 1, y)

        if not self.model.grid.out_of_bounds(new_position):
            self.model.grid.move_agent(self, new_position)

    def is_corner(self, x, y):
        """Verifica si el vehículo está en una esquina de la cuadra."""
        return (x % 6 == 0 and y % 6 == 0) or (x % 6 == 1 and y % 6 == 1) or \
               (x % 6 == 0 and y % 6 == 1) or (x % 6 == 1 and y % 6 == 0)

    def turn_corner(self, x, y):
        """Gira automáticamente en la esquina para seguir el flujo alrededor de la cuadra."""
        if self.direction == 'N' and x % 6 == 0 and y % 6 == 0:
            self.direction = 'E'
        elif self.direction == 'S' and x % 6 == 1 and y % 6 == 1:
            self.direction = 'W'
        elif self.direction == 'E' and x % 6 == 0 and y % 6 == 1:
            self.direction = 'S'
        elif self.direction == 'W' and x % 6 == 1 and y % 6 == 0:
            self.direction = 'N'

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random


class Semaforo(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "red"
        self.count = 0

    def step(self):
        ...

    def count_vehicles(self):
        ...

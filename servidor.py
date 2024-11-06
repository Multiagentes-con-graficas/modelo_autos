from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import SimultaneousActivation
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from agente_vehiculo import Vehicle
from agente_avenida import Road
from model import TrafficModel
import random


def agent_portrayal(agent):
    if isinstance(agent, Vehicle):
        portrayal = {
            "Shape": "circle",
            "Color": "yellow",
            "Filled": "true",
            "r": 0.5,
            "Layer": 1
        }
    elif isinstance(agent, Road):
        color_map = {'N': "lightblue", 'S': "lightcoral",
                     'E': "lightgreen", 'W': "lightgoldenrodyellow"}
        portrayal = {
            "Shape": "rect",
            "Color": color_map.get(agent.direction, "grey"),
            "Filled": "true",
            "w": 1,
            "h": 1,
            "Layer": 0
        }
    return portrayal


grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)
server = ModularServer(
    TrafficModel,
    [grid],
    "Autos en la ciudad",
    {"width": 20, "height": 20, "num_vehicles": 30}
)

server.port = 8001
server.launch()

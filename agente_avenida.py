from mesa import Agent


class Road(Agent):
    def __init__(self, unique_id, model, direction=None):
        super().__init__(unique_id, model)
        self.direction = direction

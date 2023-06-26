# Definition of a flower
import mesa

class Flower(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
# Definition of Bee Agent
import mesa

class Bee(mesa.Agent):
    """Bzzzzzzz"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    
    def step(self):
        self.move()

    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=False,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
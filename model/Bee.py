# Definition of Bee Agent
import mesa

class Bee(mesa.Agent):
    """Bzzzzzzz"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.previous_pos = (0, 0)
        self.previous_previous_pos = (0, 0)

    
    def step(self):
        self.move()

    
    def move(self):
        # go to a neighboring cell but not the previous position
        # TODO: this does accurately prevent going to the previous position
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=False,
            include_center=False)
        new_position = self.random.choice(list(set(possible_steps) - set(self.previous_previous_pos)))
        self.previous_previous_pos = self.previous_pos
        self.previous_pos = self.pos
        self.model.grid.move_agent(self, new_position)
        
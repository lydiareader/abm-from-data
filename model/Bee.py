# Definition of Bee Agent
import mesa

class Bee(mesa.Agent):
    """Bzzzzzzz"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.previous_pos = (0, 0)

    
    def step(self):
        self.move()
        self.check_flower()

    
    def move(self):
        # go to a neighboring cell but not the previous position
        # TODO: this does accurately prevent going to the previous position
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=False,
            include_center=False)
        self.previous_pos = self.pos
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    
    def check_flower(self):
        '''Check if there is a flower on the current cell'''
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        self.on_flower = (len(cellmates) > 1)
        
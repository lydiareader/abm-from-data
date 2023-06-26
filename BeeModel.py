# Main model definition
import mesa
from Bee import Bee

class BeeModel(mesa.Model):
    """A model with a bee. Bzzz"""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width=width, height=height, torus=True)
        self.schedule = mesa.time.RandomActivation(self)

        for i in range(N):
            b = Bee(i, self)
            self.schedule.add(b)

            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (x, y))
    

    def step(self):
        self.schedule.step()
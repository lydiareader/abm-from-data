# Main model definition
import mesa
from Bee import Bee
from Flower import Flower
from itertools import product

class BeeModel(mesa.Model):
    """A model with a bee. Bzzz"""
    def __init__(self, num_bees, num_flowers, width, height):
        self.num_agents = num_bees
        self.num_flowers = num_flowers
        self.grid = mesa.space.MultiGrid(width=width, height=height, torus=True)
        self.schedule = mesa.time.RandomActivation(self)

        for i in range(num_bees):
            # create the bees
            b = Bee(i, self)
            self.schedule.add(b)

            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (x, y))

        # place the flowers randomly
        flower_pos_options = list(product(range(width), range(height)))
        flower_pos_list = self.random.sample(flower_pos_options, num_flowers)
        for j in range(num_flowers):
            f = Flower(j + self.num_agents, self)
            self.grid.place_agent(f, flower_pos_list[j])


        self.bees = self.schedule.agents    # alias for convenience
    

    def step(self):
        self.schedule.step()
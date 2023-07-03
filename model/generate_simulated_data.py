from BeeModel import BeeModel
import numpy as np
import json

replicates = 10
eat_probabilities = np.linspace(0,1,11)

width = 2
height = 2
time = 1000
beecount = 1

for p_eat in eat_probabilities:
    for rep in range(replicates):
        model = BeeModel(beecount, flower_density=0.5, width=width, height=height, p_eat=p_eat)
        states = []
        for _ in range(time):
            model.step()
            states.append(model.get_grid_state())
        
        filename = f"{int(p_eat*10):02d}.{rep:03d}.json"
        print(filename)
        with open(filename, "w") as f:
            json.dump(states, f)

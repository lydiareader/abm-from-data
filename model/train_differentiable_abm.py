import json
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from DifferentiableBeeModel import DifferentiableBeeModel
import pandas as pd

replicates = 10
eat_probabilities = np.linspace(0,1,11)
epochs = 10000
width = 10
height = 10
beecount = 1
time = 10

real_p_eats = []
predicted_p_eats = []

for p_eat in eat_probabilities:
    for rep in range(replicates):
        filename = f"{int(p_eat*10):02d}.{rep:03d}.json"
        with open(filename, "r") as f:
            states = json.load(f)

        
        bee_positions = np.zeros((width, height, beecount, time))
        flower_positions = np.zeros((width, height, time))

        for t in range(time):
            for beeindex, (x,y) in enumerate(states[t]["bees"]):
                bee_positions[x,y,beeindex,t] = 1
            for flowerindex, position in enumerate(states[t]["flowers"]):
                if position:
                    x,y = position
                    flower_positions[x,y,t] = 1

        bee_positions_tensor = torch.Tensor(bee_positions)
        flower_positions_tensor = torch.Tensor(flower_positions)

        model = DifferentiableBeeModel()

        optimizer = optim.Adam(model.parameters(), lr=0.0001)
        criterion = torch.nn.BCELoss()

        for epoch in range(epochs):
            optimizer.zero_grad()

            random_values = torch.rand(flower_positions_tensor[:,:,:-1].shape)
            next_flower_positions_prediction = model(bee_positions_tensor[:,:,0,:-1], flower_positions_tensor[:,:,:-1], random_values)
            loss = criterion(next_flower_positions_prediction, flower_positions_tensor[:,:,1:])
            loss.backward()
            optimizer.step()

        print(model.p_eat, p_eat)
        real_p_eats.append(float(p_eat))
        predicted_p_eats.append(float(model.p_eat))

df = pd.DataFrame({"real":real_p_eats, "prediction": predicted_p_eats})
df.to_csv("predictions.csv")


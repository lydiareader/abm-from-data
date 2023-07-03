import torch
import torch.nn as nn

class DifferentiableBeeModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.p_eat = nn.Parameter(torch.tensor(0.5))
        
    def forward(self, bee_position, flower_position, input_rand):
        return bee_position * flower_position * torch.sigmoid((input_rand-self.p_eat)*10) + (1-bee_position) * flower_position

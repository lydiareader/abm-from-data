"""
Project "abm-from-data" at the Complex Systems Summer School 2023 (Santa Fe Institute)
"""

import numpy as np
from scipy.stats import qmc
import matplotlib.pyplot as plt

""" class definitions """

class Sampling():
    """
    collection of different methods of parameter space sampling 
    """
    def __init__(self, param_names, min_values, max_values):
        self.param_names = param_names
        self.min_values = min_values
        self.max_values = max_values
        self.nr_params = len(param_names)
    
    def latin_hypercubes(self, nr_values, orthogonal=False):
        """
        computes evenly spaced samples from a parameter space, 
        using the orthogonal latin hypercubes sampling algorithm from scipy
        
        Parameters
        ----------
        nr_values : int
            number of sampling values along each parameter dimension
            
        orthogonal : bool
            option to use orthogonal sampling. In this case, the number of
            sampling values needs to be equal to the square of a prime number
            
        Returns
        -------
        samples : numpy array
            two dimensional numpy array containing the sample points
        """
        if orthogonal:
            sampler = qmc.LatinHypercube(d=self.nr_params, strength=2)
        else:
            sampler = qmc.LatinHypercube(d=self.nr_params)
        sample_unit_cube = sampler.random(n=nr_values)
        sample = qmc.scale(sample_unit_cube, self.min_values, self.max_values)
        return sample
    
    def grid_sampling(self, nr_values):
        """
        grid sampling
        
        Parameters
        ----------
        nr_values : int
            number of sampling values along each parameter dimension
        
        Returns
        -------
        samples_array : numpy array
            numpy array containing all sample points
        """
        pass
    
    
""" main entry point """
if __name__ == "__main__":
    """ Illustration """
    nr_dimensions = 3
    param_names = ["A", "B", "C"]
    min_values = [0,0,0]
    max_values = [1,1,1]
    nr_values = 25 #needs to be the square of a prime number for the orthogonal case
    S = Sampling(param_names=param_names,
                 min_values=min_values,
                 max_values=max_values) 
    sample = S.latin_hypercubes(nr_values=nr_values, orthogonal=True)
    x_values = [sample[i][0] for i in range(len(sample))]
    y_values = [sample[i][1] for i in range(len(sample))]
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(x_values, y_values, "o", markersize=10)
    ax.set_xlabel("parameter " + param_names[0])
    ax.set_ylabel("parameter " + param_names[1])
    ax.set_title("Two-dimensional projection of sample points")

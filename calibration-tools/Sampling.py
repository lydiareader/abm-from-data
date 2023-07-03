"""
Project "abm-from-data" at the Complex Systems Summer School 2023 (Santa Fe Institute)
"""

import numpy as np
from scipy.stats import qmc
import matplotlib.pyplot as plt
import pandas as pd

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
        sample_df : pandas data frame
            Data frame containing the sample coordinates for each parameter.
        """
        if orthogonal:
            sampler = qmc.LatinHypercube(d=self.nr_params, strength=2)
        else:
            sampler = qmc.LatinHypercube(d=self.nr_params)
        sample_unit_cube = sampler.random(n=nr_values)
        sample = qmc.scale(sample_unit_cube, self.min_values, self.max_values)
        sample_dict = {self.param_names[k]: \
                       [sample[i][k] for i in range(len(sample))] \
                                        for k in range(self.nr_params)}
        sample_df = pd.DataFrame(sample_dict)
        #print(sample_df.corr())
        return sample_df
    
    def grid_sampling(self, nr_values):
        """
        grid sampling
        
        Parameters
        ----------
        nr_values : int
            number of sampling values along each parameter dimension
        
        Returns
        -------
        coordinates_array: numpy array
            numpy array containing the coordinates of the sampling points
        """
        min_and_max_values = zip(self.min_values,self.max_values)
        coordinates_array = np.meshgrid(*[np.linspace(i,j,nr_values) for i,j in min_and_max_values])
        return coordinates_array
    
    
""" main entry point """
if __name__ == "__main__":
    """ Illustration for two dimensions"""
    param_names = ["A", "B"]
    min_values = [0,0]
    max_values = [1,1]
    nr_values = 9 #needs to be the square of a prime number for the orthogonal case
    
    """ Latin hypercubes """
    S = Sampling(param_names=param_names,
                 min_values=min_values,
                 max_values=max_values) 
    LH_sample = S.latin_hypercubes(nr_values=nr_values, orthogonal=True)

    """Grid sampling """
    G_sample = S.grid_sampling(nr_values=nr_values)
    fig, ax = plt.subplots(nrows=2, ncols=1, squeeze=False, figsize=(8,12))
    ax[0][0].plot(LH_sample["A"], LH_sample["B"], "o", markersize=10)
    ax[0][0].set_xlabel("parameter " + param_names[0])
    ax[0][0].set_ylabel("parameter " + param_names[1])
    ax[0][0].set_title("Sample points using latin hypercubes")
    ax[1][0].plot(G_sample[0], G_sample[1], "o", markersize=10)
    ax[1][0].set_xlabel("parameter " + param_names[0])
    ax[1][0].set_ylabel("parameter " + param_names[1])
    ax[1][0].set_title("Sample points using grid sampling")
    plt.tight_layout()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 19:29:50 2023

@author: Anja Janischewski

Code is partly taken from the lecture material of the course "Computational Economics II"
at Chemnitz University of Technology tought by Prof. Torsten Heinrich
"""

""" module imports """
import numpy as np
import pandas as pd

""" class definitions """
class Sampling():
    """
    class defining different methods for sampling the parameter space
    """
    def __init__(self, param_names, min_values, max_values):
        self.param_names = param_names
        self.min_values = min_values
        self.max_values = max_values
        self.nr_params = len(param_names)
        self.parameter_samples = {}
    
    def NOHL_sampling(self, nr_values):
        """
        computes samples according to an nearly orthogonal hypercubes 
        algorithm
        
        Parameters
        ----------
        nr_values : int
            number of sampling values along each parameter dimension
            
        Returns
        -------
        samples_df : pandas data frame
            data frame containing the sample points
        """
        """ prepare parameter values for sampling """
        parameters_for_sampling = {}
        for k in range(self.nr_params):
            min_value = self.min_values[k]
            max_value = self.max_values[k]
            step_size = (max_value - min_value) / (nr_values -1)
            param_values = np.arange(min_value, max_value + step_size, step_size)
            parameters_for_sampling[self.param_names[k]] = param_values
            
        """ create nearly orthogonal samples """
        samples_ok = False
        while not samples_ok:
            """ create candidate samples"""
            for param in self.param_names:
                sample = np.random.choice(a=parameters_for_sampling[param],
                                              size=nr_values, 
                                              replace=False)
                self.parameter_samples[param] = sample

            """ check if samples are correlated"""
            samples_df = pd.DataFrame(self.parameter_samples)
            correlation_matrix = samples_df.corr() - \
                                np.identity(self.nr_params)
            if (np.abs(correlation_matrix) < 0.05).all(axis=None):
                """ When samples are not correlated any more, we can
                    stop the while loop."""
                samples_ok = True
        return samples_df
    
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
    S = Sampling(param_names=["A", "B"],
                 min_values=[0,0],
                 max_values=[1,1])
    sampling_df = S.NOHL_sampling(nr_values=11)
    print(sampling_df)

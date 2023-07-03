# abm-from-data

## Abstract
Group members: Shabaz, Lydia, Anja, Carla, Pablo, Bernise, Jana 

Corresponding group member: Jana Lasser jana.lasser@tugraz.at  

Resources:  
* Zotero library with relevant literature: [https://www.zotero.org/groups/5097156/abm_from_data](https://www.zotero.org/groups/5097156/abm_from_data)
* GitHub repository with growing collection of learning resources: [https://github.com/lydiareader/abm-from-data](https://github.com/lydiareader/abm-from-data) 

The project "Agent-based models from data" is an endeavour focused on learning about methods to calibrate or discover agent-based models given (fine-grained) observations from the system of interest. Sophisticated agent-based models are increasingly used to model complex dynamical systems. However, the existing learning resources regarding the implementation and calibration of these models remain limited to rather basic models and approaches. This project aims to contribute to filling this gap by providing an overview of approaches and collection of learning materials.

Agent-based models are a powerful tool to model complex systems. However, many models have a large number of free parameters that need to be chosen or calibrated. In addition, the choice of which mechanisms to model and which to ignore can be somewhat arbitrary. These challenges threaten the external validity and predictive power of agent-based models. The use of micro-level observations to "learn" the agent-based model from data can contribute to improving model validity and is increasingly employed in modern agent-based modelling.

A standard approach to calibrate parameters of agent-based models is to compare the moments of distributions for some outcome of interest as simulated by the model to the moments of the distribution observed in the real world. For example, considering an agent-based model of the spread of a disease in a population, we might be interested in the average outbreak size and its variance. Given data about outbreaks of the disease in the real world, we can tune parameters of the model such as the infection risk by minimizing the difference between the observed and simulated average outbreak size. While this approach enables us to reproduce the **macro** behaviour of a system of interest, it does not guarantee that on the **micro**-level the simulation behaves in the same way as the real world, as a number of micro behaviours might result in the same macro outcome. This is reflected by the observation that the functions that are optimized to calibrate the parameters are ofentimes rugged – they have many local minima – and tend to have rather flat "valleys", making it difficult to find a clear optimum for parameter values. In addition, there might be mechanisms that are important for the phenomenon of interest but are ignored in the simulation to reduce complexity. For the example of disease spread, this could be transmissions via different paths, such as aerosols or surfaces. Here, we briefly summarise a number of approaches to address these challenges.

**Probabilistic modelling approach**:

**Multi-agent inverse reinforcement learning**:


## model
V0 of the model is incredibly simple for educational purposes. The model space is a lattice with torroidal edges, defined by a width and a height. Flowers are placed on random cells. There is a single agent: a bee that moves randomly from cell to cell. When a bee is on the same cell as a flower, the bee will eat from the flower with some probability. The primary goal of the model was to see if the probability of eating from the flower could be derived using advanced ABM calibration methods.

## calibration-tools

### Sampling.py

Class containing different methods for parameter space sampling.  
A two dimensional plot is provided as illustration.

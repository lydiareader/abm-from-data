# abm-from-data

## Abstract
Group members: Shabaz, Lydia, Anja, Carla, Pablo, Bernise, Jana (jana.lasser@tugraz.at)

Sophisticated agent-based models (ABMs) are increasingly used to model complex dynamical systems and have been praised for their ability to replicate empirically-observed stylized facts on the macro level which other approaches struggle to replicate. Despite those successes, ABMs face strong criticism regarding their inadequacy of validation and calibration practices concerning a) free micro parameters as well as b) behavioral rules of emergent dynamics. In other words, the stylized-fact centric methodology of most ABMs creates the impossibility of robust model comparison because a potential large number of different micro parameters and/or their behavioral rules could lead to the same stylized facts.   

**Learning micro-parameters from data:** Many ABMs have a large number of free parameters that need to be chosen or calibrated. A standard approach to calibrate parameters of agent-based models is to compare the moments of distributions for some outcome of interest as simulated by the model to the moments of the distribution observed in the real world. While this approach enables the reproduction of macro behavior of a system of interest, it does not guarantee that on the micro-level the simulation behaves in the same way as the real world, as a number of micro behaviors might result in the same macro outcome. This is reflected by the observation that the functions that are optimized to calibrate the parameters are oftentimes rugged – they have many local minima – and tend to have rather flat "valleys", making it difficult to find a clear optimum for parameter values. A way to improve on this situation is the use of micro-level observations to calibrate the micro-parameters of the system, such as individual agent attributes. A recent approach proposed in this direction relies on the translation of the ABM into a differentiable form [1] and subsequent gradient descent or maximum-likelihood estimation of the micro parameters given data.  

**Learning mechanisms from data:** Next to free model parameters, there might be mechanisms that are important for the phenomenon of interest but are ignored in the simulation to reduce complexity. The choice of which mechanisms to model and which to ignore can be somewhat arbitrary – again threatening the external validity and reliability of predictions from the model. Multi-agent inverse reinforcement learning [2] can provide a principled way to select mechanisms for a model from a pool of probable mechanisms given data. In this approach, agents are generated to pursue a certain goal and interact with other agents to explore possible strategies.  

In our project we set out to learn about these methods to calibrate or discover agent-based models given fine-grained observations from a system of interest. Along the way we discovered that there is a substantial gap between the approaches that are used in contemporary ABM modeling in research applications and the available learning resources.  Therefore, next to learning about these approaches ourselves, the main aim of the project is to compile learning resources on modern ABM approaches for teaching students and learning teachers. We provide a growing collection of literature on recent attempts to address challenges with ABMs [3]. We created a simple model (“A Bee Model”) with one free parameter that can be used as a benchmark model to test different approaches [4]. We provide translation of the model into a differentiable form and a mechanism to “learn” the model’s parameter from data [4]. Finally, we started to compile a list of learning and teaching materials for learning ABMs from data [4]. The long-term goal of the project is to transform this loose collection of knowledge into a more organized learning resource for ABMs.

**References**  
[1] Monti et al., On learning agent-based models from data, Scientific Reports (2023).   
[2] Bergerson et al., Multi-Agent Inverse Reinforcement Learning: Suboptimal Demonstrations and Alternative Solution Concepts, arXiv (2021).  
[3] Zotero library „ABM from data“, [https://www.zotero.org/groups/5097156/abm_from_data](https://www.zotero.org/groups/5097156/abm_from_data](https://www.zotero.org/groups/5097156/abm_from_data](https://www.zotero.org/groups/5097156/abm_from_data).  
[4] GitHub repository with growing collection of learning resources: [https://github.com/lydiareader/abm-from-data](https://github.com/lydiareader/abm-from-data)


## model
V0 of the model is incredibly simple for educational purposes. The model space is a lattice with torroidal edges, defined by a width and a height. Flowers are placed on random cells. There is a single agent: a bee that moves randomly from cell to cell. When a bee is on the same cell as a flower, the bee will eat from the flower with some probability. The primary goal of the model was to see if the probability of eating from the flower could be derived using advanced ABM calibration methods.

## calibration-tools

### Sampling.py

Class containing different methods for parameter space sampling.  
A two dimensional plot is provided as illustration.

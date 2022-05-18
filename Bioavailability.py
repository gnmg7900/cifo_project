from charles.charles import Population, Individual
from data.data import inputs,target
from copy import deepcopy
from charles.selection import fps, tournament
from charles.mutation import swap_mutation, inversion_mutation
from charles.crossover import single_point_co,cycle_co, pmx_co

import random as rand
import numpy as np
import math
from sklearn.metrics import mean_squared_error



# inputs is the matrix moleculars (X1,X2,.... X241)

def get_fitness(self):
    """A simple objective function to calculate RMSE

    Returns:
        int: the total RMSE
    """
    predict_values=[]      # Create an empty list
    for i in range(len(inputs)):
        # Em cada iteração multiplicar de Beta1 até BetaN element wise com a primeira row de inputs
        # e posteriormente adicionar o beta0

        temp = np.sum(np.multiply(self.representation[1:], inputs[i])) + self.representation[0]
        predict_values.append(temp)  # Adicionar à lista de predicted values
    predict_values
    print(predict_values)
    # RMSE usando Sklearn dos valores predicted vs actual (target), e round it para 2 casas decimais
    rmse = round(math.sqrt(mean_squared_error(target,predict_values)),2)

    return rmse


# Monkey patching
Individual.get_fitness = get_fitness



pop = Population(
    size=100,
    sol_size=(len(inputs[0])+1),
    valid_set=[0,1],
    replacement=True,
    optim="min",
)


pop.evolve(
    gens=1,
    select=fps,
    crossover=single_point_co,
    mutate=swap_mutation,
    co_p=0.8,
    mu_p=0.2,
    elitism=True
)


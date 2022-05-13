from charles.charles import Population, Individual
from data.data import distance_matrix
from copy import deepcopy
from charles.selection import tournament
from charles.mutation import inversion_mutation
from charles.crossover import pmx_co


def get_fitness(self):
    """A simple objective function to calculate RMSE

    Returns:
        int: the total RMSE
    """



def get_neighbours(self):
    """A neighbourhood function for the Bioavailability problem.

    Returns:
        a definir pelo Tomás
    """



# Monkey patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours


pop = Population(
    size=100,
    sol_size=len(distance_matrix[0]),
    valid_set=[i for i in range(len(distance_matrix[0]))],
    replacement=False,
    optim="min",
)

pop.evolve(
    gens=100,
    select=tournament,
    crossover=pmx_co,
    mutate=inversion_mutation,
    co_p=0.8,
    mu_p=0.2,
    elitism=True
)
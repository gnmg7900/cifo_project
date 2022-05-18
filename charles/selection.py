from random import uniform, sample
from operator import attrgetter


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "min":
        # Sum total fitness
        total_fitness = sum([(1/i.fitness) for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += (1/individual.fitness)
            if position > spin:
                return individual

    elif population.optim == "max":
        raise NotImplementedError

    else:
        raise Exception("No optimization specified (min).")



def tournament(population, size=20):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """

    # Select individuals based on tournament size
    tournament = sample(population.individuals, size)
    # Check if the problem is max or min
    if population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))

    elif population.optim == "max":
        raise NotImplementedError

    else:
        raise Exception("No optimization specified (min).")

# Falta escrever o ranking
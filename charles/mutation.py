from random import randint, sample


def swap_mutation(individual):
    """Swap mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points
    mut_points = sample(range(len(individual)), 2)
    # Swap them
    individual[mut_points[0]], individual[mut_points[1]] = individual[mut_points[1]], individual[mut_points[0]]

    return individual


def inversion_mutation(individual):
    """Inversion mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Position of the start and end of substring
    mut_points = sample(range(len(individual)), 2)
    # This method assumes that the second point is after (on the right of) the first one, that's the reason why the list is sorted
    mut_points.sort()
    # Invert for the mutation
    individual[mut_points[0]:mut_points[1]] = individual[mut_points[0]:mut_points[1]][::-1]

    return individual

# Insertion Mutation selects a Beta at random and inserts it at random position

def insertion_mutation(individual):
    mut_insert_point = sample(range(len(individual)), 2)
    mut_insert_point.sort()
    print(f"the index mutation point is {mut_insert_point[0]} and the index insert point is {mut_insert_point[1]}")

    aux1 = individual[mut_insert_point[0]]
    aux2 = individual[mut_insert_point[1] + 1:len(individual)]
    individual = individual[0:mut_insert_point[0]]+individual[mut_insert_point[0]+1:mut_insert_point[1]+1]
    individual.append(aux1)
    individual = individual + aux2

    return individual

# Abaixo serve para testar se o código definido acima está bem implementado.

if __name__ == '__main__':
    test = [6, 1, 3, 5, 2, 4, 7]
    #test = inversion_mutation(test)
    test = insertion_mutation(test)
    print(test)




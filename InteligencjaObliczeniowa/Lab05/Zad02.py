import math
import pygad
import numpy as np


def endurance(x, y, z, u, v, w):
    return math.exp(-2 * (y - math.sin(x))**2) + math.sin(z * u) + math.cos(v * w)

def fitness_func(model, solution, solution_idx):
    x, y, z, u, v, w = solution
    endurance_value = endurance(x, y, z, u, v, w)
    return endurance_value


gene_space={"low": 0.0, "high": 1.0}

ga_instance = pygad.GA(
    num_generations=50,
    sol_per_pop=10,
    num_genes=6,
    num_parents_mating=4,
    fitness_func=fitness_func,
    parent_selection_type="sss",
    crossover_type="single_point",
    mutation_percent_genes=15,
    gene_space=gene_space
)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("best solution: ", solution)
print("best endurance: ", solution_fitness)

ga_instance.plot_fitness().savefig("Zad02results.png")
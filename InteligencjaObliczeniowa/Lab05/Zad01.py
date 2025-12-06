import time

import numpy as np
from pygad import GA


def fitness_func(ga_instance, solution, solution_idx):
    selected_weights = np.sum(solution * weights)
    selected_values = np.sum(solution * values)

    if selected_weights > 25:
        fitness = 0
    else:
        fitness = selected_values

    return fitness


Items = {"zegar": (100, 7),
"obraz-pejzaż":	(300, 7),
"obraz-portret": (200, 6),
"radio": (40, 2),
"laptop": (500, 5),
"lampka nocna":	(70, 6),
"srebrne sztućce": (100, 1),
"porcelana": (250, 3),
"figura z brązu": (300, 10),
"skórzana torebka": (280, 3),
"odkurzacz": (300, 15)}

Ikeys = list(Items.keys())

values_tuples, weight_tuples = zip(*Items.values())

values = list(values_tuples)
weights = list(weight_tuples)

ga_instance = GA(
    num_generations=50,
    num_parents_mating=4,
    fitness_func=fitness_func,
    sol_per_pop=10,
    num_genes=len(Ikeys),
    gene_space=[0, 1],
    gene_type=int,
    parent_selection_type="rank",
    crossover_type="uniform",
    mutation_type="random",
    mutation_percent_genes=10
)


def run_experiment():
    start_time = time.time()
    ga_instance.run()
    end_time = time.time()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    best_selection_indices = np.where(solution == 1)[0]
    best_items = [Ikeys[i] for i in best_selection_indices]
    total_weight = np.sum(solution * weights)
    return best_items, solution_fitness, total_weight, end_time - start_time


result = [run_experiment() for _ in range(10)]
average_time = sum(res[3] for res in result)/len(result)


filename = "Zad01results.txt"
with open(filename, "w") as f:
    f.write("Results:\n")
    for i, (best_items, solution_fitness, total_weight, exec_time) in enumerate(result):
        f.write(f"{i+1}:\n")
        f.write(f"Items Selected: {best_items}\n")
        f.write(f"Total Value: {solution_fitness}\n")
        f.write(f"Total Weight: {total_weight} / {25} (Capacity)\n")
        f.write(f"Execution Time: {exec_time:.2f}s\n\n")
    f.write(f"Average Time: {average_time:.2f}s\n")
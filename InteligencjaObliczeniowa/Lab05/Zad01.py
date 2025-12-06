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
    parent_selection_type="rws",
    crossover_type="uniform",
    mutation_type="random",
    mutation_percent_genes=10
)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
best_selection_indices = np.where(solution ==1)[0]
best_items= [Ikeys[i] for i in best_selection_indices]

total_weight = np.sum(solution * weights)

print("\n--- Genetic Algorithm Results ---")
print(f"✅ Items Selected: {best_items}")
print(f"💰 Total Value: {solution_fitness}")
print(f"⚖️ Total Weight: {total_weight} / {25} (Capacity)")
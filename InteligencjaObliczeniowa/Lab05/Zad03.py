import pygad
import time

grid = [
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 2]
]

start_pos = (0,0)
goal_pos = (9, 9)

def fitness_func(ga_instance, solution, solution_idx):
    x, y = start_pos
    score = 0
    for step in solution:
        if step == 0:
            x -= 1
        elif step == 1:
            x += 1
        elif step == 2:
            y -= 1
        elif step == 3:
            y += 1
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
            break
        score += 1
        if (x, y) == goal_pos:
            score += 100
            break
    goal_x, goal_y = goal_pos
    distance = abs(goal_x - x) + abs(goal_y - y)
    score -= distance
    return score


gene_space = [0, 1, 2, 3]

def on_generation(ga_instance):
    best_solution, best_fitness, _ = ga_instance.best_solution()
    if best_fitness >= 100:
        print(f"Solution found: {ga_instance.generations_completed}")
        ga_instance.terminate_generation = True


ga_instance = pygad.GA(
    num_generations=500,
    sol_per_pop=200,
    num_parents_mating=10,
    fitness_func=fitness_func,
    gene_space=gene_space,
    num_genes=40,
    mutation_percent_genes=10,
    crossover_type="single_point",
    mutation_type="random",
    on_generation=on_generation
)


def run_experiment():
    start_time = time.time()
    ga_instance.run()
    end_time = time.time()
    best_solution, best_fitness, _ = ga_instance.best_solution()
    return best_solution, best_fitness, end_time - start_time

result = [run_experiment() for _ in range(10)]
average_time = sum(res[2] for res in result)/len(result)

filename = "Zad03results.txt"

with open(filename, "w") as f:
    f.write("Best times: ")
    for i, (solution, fitness, exec_time) in enumerate(result):
        f.write(f"\n{i+1}: {fitness} {exec_time:.2f}s")

    f.write(f"\nAverage time: {average_time:.2f}s")
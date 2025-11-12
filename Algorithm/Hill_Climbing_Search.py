import random

def fitness(x):
    return  -x**2+ 10
def hill_climbing(start, step_size=1, max_iteration =100):
    current = start
    for i in range(max_iteration):
       neighbors = [current+ step_size, current - step_size]
       neighbor_fitness = [fitness(n) for n in neighbors]

       best_neighbor = neighbors[neighbor_fitness.index(max(neighbor_fitness))]
       
       if fitness(best_neighbor)<= fitness(current):
          break
       current = best_neighbor
    return current, fitness(current)

start_point = random.randint(-10, 10)
soluation, value = hill_climbing(start_point)
print(f"start :{start_point:.2f} -> soluation: {soluation:.2f}, Valua:{value}")
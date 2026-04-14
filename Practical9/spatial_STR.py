# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import random

# the input data
population = np.zeros((100, 100))
x = random.randint(0, 99)
y = random.randint(0, 99)
print(f"Initial infected individual at: ({x}, {y})")
population[x, y] = 1

# plot the original population
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest', origin='lower')
plt.title('Initial Population with Infected Individual at ('+str(x)+','+str(y)+')')
plt.colorbar(label='Infection Status')
plt.show()

# set the model parameters
beta = 0.3
gamma = 0.05

# define the SIR model function
def SIR(population, beta, gamma, n_steps):
    infection_results = []
    for step in range(n_steps):
        population_results = []
        infected_individuals = np.argwhere(population == 1) # this will return the indices of infected individuals
        population_copy = population.copy()
        for infected in infected_individuals:
            x, y = infected
            # attempt to infect neighbors
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx != 0 or dy != 0) and (0 <= x + dx < population.shape[0]) and (0 <= y + dy < population.shape[1]):
                        if population[x + dx, y + dy] == 0: # if the neighbor is susceptible
                            if random.randint(0,1) < beta: # infection occurs with probability beta
                                population_copy[x + dx, y + dy] = 1 # neighbor becomes infected]
            # attempt to recover
            if random.randint(0,1) < gamma: # recovery occurs with probability gamma
                population_copy[x, y] = 2 # infected individual recovers
        population = population_copy
        infection_results.append(population)
    return infection_results

# run the SIR model
results = SIR(population, beta, gamma, 100)

# plot the results
for i in range(0, 100, 10):
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(results[i], cmap='viridis', interpolation='nearest', origin='lower')
    plt.title(f'Population at Time Step {i}'+' with Infected Individual at ('+str(x)+','+str(y)+')')
    plt.colorbar(label='Infection Status')
    plt.savefig(f'population_step_{i}.png')
    plt.show()
    plt.close()
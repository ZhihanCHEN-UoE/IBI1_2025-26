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

# Vaccinate a certain number of susceptible individuals at the start
num_vaccinated = 1000  # certain number of vaccinated individuals
susceptible_positions = [(i, j) for i in range(100) for j in range(100) if population[i, j] == 0 and (i, j) != (x, y)]
random.shuffle(susceptible_positions)
for pos in susceptible_positions[:num_vaccinated]:
    population[pos] = 3

# plot the original population
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest', origin='lower')
plt.title('Initial Population with Infected Individual at ('+str(x)+','+str(y)+')')
cbar = plt.colorbar(label='Infection Status')
cbar.set_ticks([0, 1, 2, 3])
cbar.set_ticklabels(['Susceptible', 'Infected', 'Recovered', 'Vaccinated'])
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
                            if random.random() < beta: # infection occurs with probability beta
                                population_copy[x + dx, y + dy] = 1 # neighbor becomes infected
            # attempt to recover
            if random.random() < gamma: # recovery occurs with probability gamma
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
    cbar = plt.colorbar(label='Infection Status')
    cbar.set_ticks([0, 1, 2, 3])
    cbar.set_ticklabels(['Susceptible', 'Infected', 'Recovered', 'Vaccinated'])
    plt.show()
    plt.close()
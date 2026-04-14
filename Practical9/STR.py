# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

beta = 0.3
gamma = 0.05
populations = {'infected':1, 'susceptible':9999, 'recovered':0}

# define the SIR model function
def SIR(populations, beta, gamma, n_steps):
    n = sum(populations.values())
    infection_results = []
    susceptible_results = []
    recovered_results = []
    for step in range(n_steps):
        p_infected = beta * populations['infected'] / n
        for infected_individual in range(populations['infected']):
            if np.random.choice([0, 1], p=[1-gamma, gamma]) == 1:
                populations['infected'] -= 1
                populations['recovered'] += 1    
        for susceptible_individual in range(populations['susceptible']):
            if np.random.choice([0, 1], p=[1-p_infected, p_infected]) == 1:
                populations['susceptible'] -= 1
                populations['infected'] += 1
        infection_results.append(populations['infected'])
        susceptible_results.append(populations['susceptible'])
        recovered_results.append(populations['recovered'])
    return infection_results, susceptible_results, recovered_results

# run the SIR model for 1000 time steps
infection_results, susceptible_results, recovered_results = SIR(populations, beta, gamma, 1000)

# plot the results
plt.plot(infection_results, label='Infected')
plt.plot(susceptible_results, label='Susceptible')
plt.plot(recovered_results, label='Recovered')
plt.xlabel('Time Steps')
plt.ylabel('Number of Individuals')
plt.title('SIR Model Simulation')
plt.legend()
plt.show()
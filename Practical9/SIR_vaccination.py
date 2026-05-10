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

# run the SIR model with vaccination rate
def SIR_with_vaccine(rate):
    populations_with_vaccinaion = populations.copy()
    populations_with_vaccinaion['susceptible'] -= int(populations['susceptible'] * rate)
    populations_with_vaccinaion['vaccinated'] = int(populations['susceptible'] * rate)
    return SIR(populations_with_vaccinaion, beta, gamma, 1000)


# run the SIR model for different vaccine rates
vaccine_rates = [i/10 for i in range(11)]
results = []

for i in range(len(vaccine_rates)):
    result = SIR_with_vaccine(vaccine_rates[i])
    results.append(result[0])

# plot the results with different vaccine rates
plt.figure(figsize=(10, 6))
for i in range(len(vaccine_rates)):
    plt.plot(results[i], label=f'Vaccine Rate: {vaccine_rates[i]}')
plt.title('SIR Model with Different Vaccine Rates')
plt.xlabel('Time Steps')
plt.ylabel('Number of Infected Individuals')
plt.legend()
plt.show()
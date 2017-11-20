import math
import random
import numpy as np

from text_utils import read_data, process_input, read_data_np
from standrad_utils import standardize, destandardize_value

data = read_data_np()
x, y = data[..., 0:3], data[..., 3]
n = len(x)
population = np.array(np.random.rand(3))
population_start_size = 20
mutate_probability = 0.1
mutation = 0.5
delta_stop_lim = 0.00000001


# def f(x1, x2):
# return theta[0] + theta[1] * x1 + theta[2] * x2


def init_population():
    global population
    for i in range(population_start_size - 1):
        population = np.vstack([population, np.random.rand(3) * 10])
        # population.append([random.randint(1000)/1000, random.randint(10000)/1000, random.randint(2000)/1000])
    pass


def crossover(father_index, mother_index):
    father = population[father_index]
    mother = population[mother_index]
    separator_index = random.getrandbits(1) + 1
    new_guy = father[:separator_index]
    new_guy = np.append(new_guy, mother[separator_index:])
    return new_guy


def mutate(new_solution):
    is_mutating = np.random.choice([True, False], 1, p=[mutate_probability, 1 - mutate_probability])
    if is_mutating:
        index = random.randint(1, 3) - 1
        new_solution[index] = random.randint(1, 20000) / 1000 - 10
    return new_solution


def should_continue():
    global population, new_population
    try:
        new_population
    except NameError:
        return True
    else:
        delta = new_population - population
        delta = np.abs(delta)
        dsum = np.sum(delta)
        # print(dsum)
        population = new_population
        return dsum > delta_stop_lim


# data = standardize(data)
init_population()
while should_continue():
    fitness = np.array([])
    for solution in population:
        y_calculated = np.dot(x, solution)
        delta = y - y_calculated
        delta *= delta
        deviation = np.sqrt(np.sum(delta) / n)
        fitness = np.append(fitness, deviation)
    print(np.average(fitness))
    reverse_fitness = 1 / fitness
    coeff_sum = np.sum(reverse_fitness)
    survival_chance = reverse_fitness / coeff_sum
    new_population = np.array([])
    for i in range(population_start_size):
        choice = np.random.choice(np.arange(len(survival_chance)), 2, p=survival_chance)
        new_solution = crossover(choice[0], choice[1])
        new_solution = mutate(new_solution)
        if len(new_population) == 0:
            new_population = new_solution
        else:
            new_population = np.vstack([new_population, new_solution])
    # print(new_solution)
print(population)

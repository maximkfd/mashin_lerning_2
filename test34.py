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
mutate_probability = 0.2
mutation = 0.5
delta_stop_lim = 0.001


# def f(x1, x2):
# return theta[0] + theta[1] * x1 + theta[2] * x2


def init_population():
    global population
    for i in range(population_start_size - 1):
        population = np.vstack([population, np.random.rand(3)])
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
        signed_mutation = np.random.choice([-mutation, mutation], 1, p=[0.5, 0.5])
        new_solution[index] += signed_mutation
    return new_solution


def should_continue():
    try:
        new_population
    except NameError:
        return True
    else:
        delta = new_population - population
        delta = np.abs(delta)
        dsum = np.sum(delta)
        return dsum < delta_stop_lim


# data = standardize(data)
init_population()
fitness = np.array([])
while should_continue():
    for solution in population:
        y_calculated = np.dot(x, solution)
        delta = y - y_calculated
        delta *= delta
        deviation = np.sqrt(np.sum(delta) / n)
        fitness = np.append(fitness, deviation)
    reverse_fitness = 1 / fitness
    coeff_sum = np.sum(reverse_fitness)
    survival_chance = reverse_fitness / coeff_sum
    new_population = np.array([])
    for i in range(population_start_size):
        choice = np.random.choice(np.arange(len(survival_chance)), 2, p=survival_chance)
        new_solution = crossover(choice[0], choice[1])
        new_solution = mutate(new_solution)
        new_population = np.append(new_population, new_solution)

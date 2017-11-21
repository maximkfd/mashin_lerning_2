import math
import random
import numpy as np

from text_utils import read_data, process_input, read_data_np
from standrad_utils import standardize, destandardize_value

RAND_CONST = 5000


def random_arr():
    return np.random.rand(3) * RAND_CONST


data = read_data_np()
x, y = data[..., 0:3], data[..., 3]
n = len(x)
population = np.array(random_arr())
population_start_size = 20
mutate_probability = 0.5
mutation = 0.05
delta_stop_lim = 0.00000001


# def f(x1, x2):
# return theta[0] + theta[1] * x1 + theta[2] * x2
def random_num():
    return np.random.rand() * RAND_CONST


def random_arr():
    return np.random.rand(3) * RAND_CONST


def init_population():
    global population
    for i in range(population_start_size - 1):
        population = np.vstack([population, random_arr()])
        # population.append([random.randint(1000)/1000, random.randint(10000)/1000, random.randint(2000)/1000])


def crossover(father_index, mother_index):
    if bool(random.getrandbits(1)):
        father = population[father_index]
        mother = population[mother_index]
    else:
        father = population[mother_index]
        mother = population[father_index]
    separator_index = random.getrandbits(1) + 1
    new_guy = father[:separator_index]
    new_guy = np.append(new_guy, mother[separator_index:])
    return new_guy


def mutate(new_solution):
    is_mutating = np.random.choice([True, False], 1, p=[mutate_probability, 1 - mutate_probability])
    if is_mutating:
        index = random.randint(1, 3) - 1
        new_solution[index] = random_num()
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
        # population = new_population
        return dsum > delta_stop_lim


def define_parents(i):
    global cur_m, cur_f
    cur_m -= 1
    if cur_m < 13:
        cur_f -= 1
        cur_m = cur_f - 1
    return [cur_f, cur_m]


# data = standardize(data)
init_population()
print(population)
contin = True
while contin:
    fitness = np.array([])
    for solution in population:
        y_calculated = np.dot(x, solution)
        delta = y - y_calculated
        delta *= delta
        deviation = np.sqrt(np.sum(delta) / n)
        fitness = np.append(fitness, deviation)
    average = np.average(fitness)
    if average < 69000:
        print(np.min(fitness))
        break
    # print(np.min(fitness))
    # print(np.max(fitness))
    # print()
    reverse_fitness = 1 / fitness
    coeff_sum = np.sum(reverse_fitness)
    survival_chance = reverse_fitness / coeff_sum
    new_population = np.array([])
    cur_f = population_start_size - 1
    cur_m = cur_f
    for i in range(population_start_size):
        # fit_inds = fitness.argsort()
        # fitness = fitness[fit_inds[::-1]]
        # population = population[fit_inds[::-1]]
        # choice = define_parents(i)
        choice = [9, 9]
        while choice[0] == choice[1]:
            choice = np.random.choice(np.arange(len(survival_chance)), 2, p=survival_chance)
        new_solution = crossover(choice[0], choice[1])
        new_solution = mutate(new_solution)
        if len(new_population) == 0:
            new_population = new_solution
        else:
            new_population = np.vstack([new_population, new_solution])
            # print(new_solution)
    contin = should_continue()
    population = new_population
print(population)

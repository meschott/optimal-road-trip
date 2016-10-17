import pandas as pd
import numpy as np

waypoint_distances = {}
waypoint_durations = {}
all_waypoints = set()
#old_start_point = ['4919 Cave Run Drive, Houston, TX']
start_point = ['4919 Cave Run Drive, Houston, TX']
end_point = '113 Mill Creek Road, South Chatham, MA'

waypoint_data = pd.read_csv("my-waypoints-dist-dur.tsv", sep="\t")

for i, row in waypoint_data.iterrows():
    waypoint_distances[frozenset([row.waypoint1, row.waypoint2])] = row.distance_m
    waypoint_durations[frozenset([row.waypoint1, row.waypoint2])] = row.duration_s
    all_waypoints.update([row.waypoint1, row.waypoint2])

import random

def compute_fitness(solution):
    """
        This function returns the total distance traveled on the current road trip.

        The genetic algorithm will favor road trips that have shorter
        total distances traveled.
    """

    solution_fitness = 0.0
    #print len(solution)

    for index in range(len(solution) - 1):
        waypoint1 = solution[index]
        waypoint2 = solution[index + 1]
    #    print waypoint1, waypoint2
    #    print waypoint_distances[frozenset([waypoint1, waypoint2])]
        solution_fitness += waypoint_distances[frozenset([waypoint1, waypoint2])]


    return solution_fitness

def generate_random_agent():
    """
        Creates a random road trip from the waypoints.
    """

    new_random_agent = list(all_waypoints)
    start_point = ['4919 Cave Run Drive, Houston, TX']
    new_random_agent.remove(start_point[0])
    new_random_agent.remove(end_point)
    random.shuffle(new_random_agent)
    start_point.extend(new_random_agent)
    new_random_agent = start_point
    new_random_agent.append(end_point)
    return tuple(new_random_agent)

def mutate_agent(agent_genome, max_mutations=3):
    """
        Applies 1 - `max_mutations` point mutations to the given road trip.

        A point mutation swaps the order of two waypoints in the road trip.
    """

    agent_genome = list(agent_genome)
    num_mutations = random.randint(1, max_mutations)

    for mutation in range(num_mutations):
        swap_index1 = random.randint(1, len(agent_genome) - 2)
        swap_index2 = swap_index1

        while swap_index1 == swap_index2:
            swap_index2 = random.randint(1, len(agent_genome) - 2)

        agent_genome[swap_index1], agent_genome[swap_index2] = agent_genome[swap_index2], agent_genome[swap_index1]

    return tuple(agent_genome)

def shuffle_mutation(agent_genome):
    """
        Applies a single shuffle mutation to the given road trip.

        A shuffle mutation takes a random sub-section of the road trip
        and moves it to another location in the road trip.
    """
    agent_genome = list(agent_genome)
    start_point = ['4919 Cave Run Drive, Houston, TX']

    agent_genome.remove(start_point[0])
    agent_genome.remove(end_point)

    start_index = random.randint(0, len(agent_genome) - 1)
    length = random.randint(2, 20)

    genome_subset = agent_genome[start_index:start_index + length]
    agent_genome = agent_genome[:start_index] + agent_genome[start_index + length:]

    insert_index = random.randint(0, len(agent_genome) + len(genome_subset) - 1)
    agent_genome = agent_genome[:insert_index] + genome_subset + agent_genome[insert_index:]

    start_point.extend(agent_genome)
    agent_genome = start_point
    agent_genome.append(end_point)

    return tuple(agent_genome)

def generate_random_population(pop_size):
    """
        Generates a list with `pop_size` number of random road trips.
    """

    random_population = []
    for agent in range(pop_size):
        random_population.append(generate_random_agent())
        #start_point=old_start_point
    return random_population

def run_genetic_algorithm(generations=5000, population_size=100):
    """
        The core of the Genetic Algorithm.
    """

    # Create a random population of `population_size` number of solutions.
    population = generate_random_population(population_size)

    # For `generations` number of repetitions...
    for generation in range(generations):

        # Compute the fitness of the entire current population
        population_fitness = {}

        for agent_genome in population:
            if agent_genome in population_fitness:
                continue

            #print len(agent_genome)

            population_fitness[agent_genome] = compute_fitness(agent_genome)

        # Take the 10 shortest road trips and produce 10 offspring each from them
        new_population = []
        for rank, agent_genome in enumerate(sorted(population_fitness, key=population_fitness.get)[:10]):
            if (generation % 1000 == 0 or generation == generations - 1) and rank == 0:
                print("Generation %d best: %d | Unique genomes: %d" % (generation,
                                                                       population_fitness[agent_genome],
                                                                       len(population_fitness)))
                print(agent_genome)
                print("")

            # Create 1 exact copy of each of the top 10 road trips
            new_population.append(agent_genome)

            # Create 2 offspring with 1-3 point mutations
            for offspring in range(2):
                new_population.append(mutate_agent(agent_genome, 3))

            # Create 7 offspring with a single shuffle mutation
            for offspring in range(7):
                new_population.append(shuffle_mutation(agent_genome))
            #print agent_genome

        # Replace the old population with the new population of offspring
        for i in range(len(population))[::-1]:
            del population[i]

        population = new_population

run_genetic_algorithm(5000,100)

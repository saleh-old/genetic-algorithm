from abc import ABC, abstractmethod
from random import randint, choices, random, choice


class Genetic(ABC):
    def __init__(self, iterations, population_size, solution_len, charset='0123456789', fitness_goal=1):
        self.population = []
        self.iterations = iterations
        self.population_size = population_size
        self.solution_len = solution_len
        self.charset = charset
        self.fitness_goal = fitness_goal

        if fitness_goal > 1 or fitness_goal < 0:
            raise ValueError('fitness scores must be between 0 and 1')

    @abstractmethod
    def fitness(self, dna) -> float:
        """
        calculates and returns the fitness score the the DNA

        :param dna: str
        :return: float (must be between 0 and 1)
        """
        pass

    def generate_initial_population(self):
        """
        generates the initial population
        """
        for i in range(self.population_size):
            dna = ''.join(choices(self.charset, k=self.solution_len))
            fitness = self.fitness(dna)
            person = {
                'dna': dna,
                'fitness': fitness
            }

            self.population.append(person)

        # sort the population
        self.population = list(sorted(self.population, key=lambda x: x['fitness'], reverse=True))

    def mutate(self, baby):
        replace_at = randint(0, self.solution_len - 1)
        replace_with = choice(self.charset)
        dna = '{}{}{}'.format(baby['dna'][:replace_at], replace_with, baby['dna'][replace_at + 1:])
        fitness = self.fitness(dna)

        return {
            'dna': dna,
            'fitness': fitness
        }

    def make_love(self):
        father = self.select_person()
        mother = self.select_person()

        dna = ''

        for i in range(self.solution_len):
            if i % 2 == 0:
                dna += father['dna'][i]
            else:
                dna += mother['dna'][i]

        return {
            'dna': dna,
            'fitness': self.fitness(dna)
        }

    def select_person(self):
        index = 0
        r = random()

        while r >= 0:
            r -= self.population[index]['fitness']
            index += 1

        index -= 1
        return self.population[index]

    def evolve(self):
        """
        the main method, that runs the evolutionary algorithm
        """
        self.generate_initial_population()

        for i in range(self.iterations):
            # let's make a baby together LOL
            baby = self.make_love()

            # let's mutate baby's genes, who knows, maybe we create a x-man or something
            baby = self.mutate(baby)

            # one person has to die and be replaced with the newborn baby
            random_index = randint(0, self.population_size - 1)
            self.population[random_index] = baby
            self.population = list(sorted(self.population, key=lambda x: x['fitness'], reverse=True))

            # reaching the fitness goal could also end the process
            if baby['fitness'] >= self.fitness_goal:
                print('fitness goal reached after iteration {}'.format(i))
                return baby

        print('Finished {} iterations.'.format(self.iterations))

        return self.population

    def run(self):
        """an alias for evolve() because it's easier to remember!"""
        return self.evolve()

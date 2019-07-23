from Genetic import Genetic


class ClassToEvolve(Genetic):
    def __init__(self):
        self.answer = '5264264772289112422891124757556398556398'
        self.iterations = 10_000
        self.population = 1000
        super().__init__(self.iterations, self.population, len(self.answer), fitness_goal=1)

    def fitness(self, dna) -> float:
        score = 0

        for i in range(len(self.answer)):
            if self.answer[i] == dna[i]:
                score += 1

        return score / len(self.answer)


to_optimize = ClassToEvolve()
result = to_optimize.run()

# do whatever you want with the result, in this case we simply return it
print(result)

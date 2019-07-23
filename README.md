# Genetic Algorithm
This implementation is simple yet advanced:

- it's fast and optimized.
- Supports both fitness_goal and iterations for ending the evolution process.
- It's been tailored to be used at your custom use cases.
- No dependencies are required.
 
## Usage Example

All you need to do is to copy the `Genetic` class into your project and use like below example.


Let's say we're looking to find a 20 characters string containing only numbers in it. We'll create a class 
and name it `ClassToEvolve` while extending the Genetic class, implement the `fitness()` method:

```python
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
```

## Test
Clone the repository and run the `main.py`:

```
git clone https://github.com/sullyfischer/genetic-algorithm.git
cd genetic-algorithm
python3 main.py
```

Output:
```bash
➜  genetic-algorithm git:(master) ✗ py main.py
fitness goal reached after iteration 1520
{'dna': '5264264772289112422891124757556398556398', 'fitness': 1.0}
```
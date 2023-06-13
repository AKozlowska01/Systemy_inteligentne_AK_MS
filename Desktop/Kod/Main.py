from SimulatedAnneling import SimulatedAnneling
from SavageCriterion import SavageCriterion
import random
import numpy as np


def WeightGenerator(N):
    weights = []
    for i in range(N):
        weight1 = random.randrange(1, 7)
        weight2 = random.randrange(weight1 + 1, 12)
        weights.append([weight1, weight2])
    return weights


def ValueGenerator(N):
    values = []
    for i in range(N):
        value = random.randrange(1, 11)
        values.append(value)
    return values


N = 5  
max_weight = 10
weights = WeightGenerator(N)
values = ValueGenerator(N)
print(" Przedmiot |  Waga  | Ocena")
for i in range(N):
    if i == 9:
        print('  ', i + 1, '   \t', weights[i], '   ', values[i])
    else:
        print('  ', i + 1, '   \t', weights[i], '  ', values[i])
print("=" * 100)
print("=" * 100)
print("Savage Criterion")
SC = SavageCriterion(values, weights, max_weight)
SC.main()
print("\n", "=" * 100)
print("=" * 100)
print("Simulated Anneling")
SA = SimulatedAnneling(values, weights, max_weight)
a, b, c = SA.Simulation()
print("=" * 100)
print(f'Wartość plecaka: {a}\nWybrane przedmioty: {b}\nWagi wybranych przedmiotów: {c}')
print("=" * 100)


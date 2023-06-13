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


class SavageCriterion:

    def __init__(self, values, weights, max_weight):
        self.values = values
        self.weights = weights
        self.max_weight = max_weight

    def VectorsGenerator(self):
        vectors = [[]]
        values2 = [0, 1]
        for item in range(len(self.values)):
            new_vector = []
            for val in values2:
                for vector in vectors:
                    new_vector.append(vector + [val])
            vectors = new_vector
        vectors.remove([0 for _ in range(len(self.values))])
        return vectors

    def ScenarioGenerator(self):
        scenarios = [[]]
        for item in self.weights:
            new_scenario = []
            for weight in item:
                for scenario in scenarios:
                    new_scenario.append(scenario + [weight])
            scenarios = new_scenario
        return scenarios

    def Knapsack(self, weights):
        tab = np.zeros((len(self.values) + 1, self.max_weight + 1))
        for i in range(1, len(self.values) + 1):
            for j in range(self.max_weight + 1):
                if weights[i - 1] > j:
                    tab[i, j] = tab[i - 1, j]
                else:
                    tab[i, j] = max(tab[i - 1, j], tab[i - 1, j - weights[i - 1]] + self.values[i - 1])

        selected_items = []
        i, w = len(self.values), self.max_weight
        while i > 0 and w > 0:
            if tab[i][w] != tab[i - 1][w]:
                selected_items.append(i - 1)
                w -= weights[i - 1]
            i -= 1

        return tab[len(self.values), self.max_weight], len(selected_items)

    def CountingSavageCriterion(self, vectors, scenarios, max_weight_scenarios, num_of_items_selected):
        macierz = []
        print("Macierz minmax:")
        for i in range(len(vectors)):
            m2 = []
            value3 = 0
            for v in range(len(vectors[i])):
                value3 += vectors[i][v] * self.values[v]
            print("Wartość wektora ", i+1, ": ", value3)
            for j in range(len(scenarios)):
                if sum(vectors[i]) == num_of_items_selected[j]:
                    m2.append(round(value3 - max_weight_scenarios[j], 2))
            macierz.append(m2)
            print(m2)

        max_macierz = []
        max_macierz2 = []
        for i in range(len(macierz)):
            if bool(macierz[i]):
                max_macierz.append(max(macierz[i]))
                max_macierz2.append(max(macierz[i]))
            else:
                max_macierz2.append(100)
        print("Macierz minmax po  maksie: \n", max_macierz)
        print("Min z macierzy: ", min(max_macierz))
        index = max_macierz.index(min(max_macierz2))
        return min(max_macierz), index

    def main(self):
        scenarios = self.ScenarioGenerator()
        print("\t\tScenariusze: ")
        for i in range(len(scenarios)):
            print("Scenariusz nr ", i + 1, ": ", scenarios[i])
        print("\nLiczba możliwych scenariuszy: ", len(scenarios))
        print("=" * 100)

        vectors = self.VectorsGenerator()
        print("\t\tWektory branych kotów: ")
        for i in range(len(vectors)):
            print("Wektor nr ", i + 1, ": ", vectors[i])
        print("\nLiczba możliwych kombinacji wektora wziętych przedmiotów: ", len(vectors))
        print("=" * 100)

        max_weight_scenarios = []
        num_of_items_selected = []
        for i in range(len(scenarios)):
            mw, nc = self.Knapsack(scenarios[i])
            max_weight_scenarios.append(mw)
            num_of_items_selected.append(nc)
        print("Wartości decyzji: ")
        print(max_weight_scenarios)
        print("Liczba wybranych przedmiotów w kazdym wypadku:")
        print(num_of_items_selected)
        print("=" * 100)

        criterion_value, index = self.CountingSavageCriterion(vectors, scenarios, max_weight_scenarios, num_of_items_selected)
        print("Wartość kryterium żalu: ", criterion_value, "\n")
        print("Najlepszy wektor to wektor nr ", index+1, ": ", vectors[index])
        knapsack_value = 0
        for i in range(len(vectors[index])):
            knapsack_value += vectors[index][i] * self.values[i]
        print("Wartość plecaka wynosi: ", knapsack_value)


# N = 3  # liczba przedmiotów
# max_weight = 10
# weights = WeightGenerator(N)
# values = ValueGenerator(N)
# print(" Przedmiot |  Waga  | Ocena")
# for i in range(N):
#     if i == 9:
#         print(' ', i + 1, ' ', weights[i], '\t ', values[i])
#     else:
#         print(' ', i + 1, '  ', weights[i], '\t ', values[i])
# print("=" * 100)
# SC = SavageCriterion(values, weights, max_weight)
# SC.main()

import matplotlib.pyplot as plt
import networkx as nx
import math
import random


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


class SimulatedAnneling:

    def __init__(self, values, weights, max_weight, Temp=1000):
        self.values = values
        self.weights = weights
        self.max_weight = max_weight
        self.Temp = Temp
        self.solution = 0
        self.chosen_items = [0 for _ in range(len(self.weights))]
        self.chosen_weights = [0 for _ in range(len(self.weights))]
        self.possible_chosen_weights = self.chosen_weights

    def FirstSolution(self):
        items_num = len(self.weights)
        weight = 0
        i = 0
        while weight < self.max_weight and i < items_num:
            j = random.randint(0, 1)
            if weight + self.weights[i][j] < self.max_weight:
                weight += self.weights[i][j]
                self.solution += self.values[i]
                self.chosen_items[i] = 1
                self.chosen_weights[i] = self.weights[i][j]
            i += 1
        print(f'Rozwiązanie początkowe: \n- wartość plecka: {self.solution} \n- wybrane przedmioty: {self.chosen_items}\n'
              f'- wagi wybranych przedmiotów: {self.chosen_weights}\n{"="*100}')
        return self.solution, self.chosen_items

    def KnapsackValue(self, chosen_items):
        value = 0
        for i in range(len(chosen_items)):
            if chosen_items[i] == 1:
                value += self.values[i]
        return value

    def KnapsackWeight(self, chosen_items):
        weight = 0
        self.possible_chosen_weights = self.chosen_weights
        for i in range(len(chosen_items)):
            if chosen_items[i] == 1 and self.chosen_items[i] == 1:
                weight += self.chosen_weights[i]
            elif chosen_items[i] == 1 and self.chosen_items[i] == 0:
                j = random.randint(0, 1)
                weight += self.weights[i][j]
                self.possible_chosen_weights[i] = self.weights[i][j]
        return weight

    def GenerateNewSolution(self):
        check = True
        while check:
            index = random.randint(0, len(self.chosen_items) - 1)
            if self.chosen_items[index] == 1:
                chosen_items = self.chosen_items.copy()
                chosen_items[index] = 0
                if self.KnapsackWeight(chosen_items) <= self.max_weight:
                    new_value = self.KnapsackValue(chosen_items)
                    new_chosen_weights = self.possible_chosen_weights
                    check = False
            else:
                chosen_items = self.chosen_items.copy()
                chosen_items[index] = 1
                if self.KnapsackWeight(chosen_items) <= self.max_weight:
                    new_value = self.KnapsackValue(chosen_items)
                    new_chosen_weights = self.possible_chosen_weights
                    check = False
        return chosen_items, new_value, new_chosen_weights

    def Probability(self, new_value):
        p = math.exp((new_value - self.solution) / self.Temp)
        return min(1, p)

    def Simulation(self):
        self.solution, self.chosen_items = self.FirstSolution()
        epoch = 1
        while self.Temp >= 0 and epoch <= 100:
            for i in range(1, 4):
                new_chosen_items, new_solution, new_chosen_weights = self.GenerateNewSolution()

                if self.solution <= new_solution:
                    self.solution = new_solution
                    self.chosen_cats = new_chosen_items
                    self.chosen_weights = new_chosen_weights
                    print(f'Epoka {epoch} proba {i} obecne rozwiazanie: {self.solution, self.chosen_items}')

                else:
                    p = self.Probability(new_solution)
                    num = random.random()
                    if num < p:
                        self.solution = new_solution
                        self.chosen_items = new_chosen_items
                        self.chosen_weights = new_chosen_weights
                        print(f'Epoka {epoch} proba {i} obecne rozwiazanie: {self.solution, self.chosen_items}')
                    else:
                        print(f'Epoka {epoch} proba {i} obecne rozwiazanie: {self.solution, self.chosen_items}')
            self.Temp = 0.9 * self.Temp
            epoch += 1
        return self.solution, self.chosen_items, self.chosen_weights

# sep = '='
# line = 100
# N = 3
# max_weight = 10
# weights = WeightGenerator(N)
# values = ValueGenerator(N)
# print(" Przedmiot |  Waga  | Ocena")
# for i in range(N):
#     if i == 9:
#         print(' ', i + 1, ' ', weights[i], '\t ', values[i])
#     else:
#         print(' ', i + 1, '  ', weights[i], '\t ', values[i])
# print(sep * line)
#
# SA = SimulatedAnneling(values, weights, max_weight)
# a, b, c = SA.Simulation()
# print(sep * line)
# print(f'Wartość plecaka: {a}\nWybrane przedmioty: {b}\nWagi wybranych przedmiotów: {c}')
# print(sep * line)
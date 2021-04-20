import numpy as np
import csv

cities = []

sol = []


def distance(x, y):
    dist = np.linalg.norm(np.array(x)-np.array(y))
    return dist


with open('TSP.csv', mode='r', newline='') as tsp:
    reader = csv.reader(tsp)

    i = 0

    for row in reader:
        cities.append(row)
        if i > 20:
            break
        i = i+1

print(cities[0])
print(cities[0][0])
print(cities[1])

city1 = [float(cities[0][0]), float(cities[0][1])]
city2 = [float(cities[1][0]), float(cities[1][1])]

print('distance 0~1 : '+str(distance(city1, city2)))

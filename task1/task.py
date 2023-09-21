import numpy as np
import json

matrix = np.random.randint(0, 10, (5, 5), int)
np.savetxt('matrix.csv', matrix, delimiter=',', fmt='%d')
print('Matrix saved successfully', '\n')

csv_data = np.genfromtxt('example.csv', delimiter=',')
print(csv_data, '\n')

with open('example.json') as file:
    json_data = json.load(file)
    print(json_data)

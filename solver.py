# -*- coding: utf-8 -*-
from operator import attrgetter
from collections import namedtuple
# from greedyalgo import greedyAlgorithm
# from DP import dynamic_programming, getknapsackItems


Item = namedtuple("Item", ['index', 'value', 'weight','value_density'])
    

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []


    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1]), int(parts[0])/int(parts[1])))

    # # Greedy Algorithm 
    # value = 0
    # weight = 0
    # taken = [0]*len(items)
    # for item in sorted(items, key = attrgetter('value_density')):
    #       if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight
    
    # Dynammic Programming| Time complexcity O(N * M) where N = number of columns (items) , M = number of rows (capacity)
            
    knapsackValues = [[0 for i in range(0, len(items) + 1)] for j in range(0, capacity+1)]
    
    for j in range(1, len(items) + 1):
        currentWeight = items[j - 1].weight
        currentValue = items[j - 1].value
        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[c][j] = knapsackValues[c][j-1]
            else:
                knapsackValues[c][j] = max(knapsackValues[c][j-1], knapsackValues[c - currentWeight][j-1] + currentValue)
    
    value = knapsackValues[-1][-1]
    
    # print(knapsackValues)
    
    taken = [0]*len(items)
    row = len(knapsackValues) - 1
    col = len(knapsackValues[0]) - 1
    while col > 0:
        if knapsackValues[row][col] == knapsackValues[row][col - 1]:
            col -= 1
        else:
            taken[col - 1] = 1
            row = row - items[col - 1].weight
            col -= 1
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == '__main__':
    # import sys
    # if len(sys.argv) > 1:
    file_location = "D:\Discrete Optimization\Knapsack\knapsack\data\ks_19_0"
    with open(file_location, 'r') as input_data_file:
        input_data = input_data_file.read()
    print(solve_it(input_data))
    # else:
        # print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')


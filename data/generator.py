import random

def increase_value(size=100, initial=100):
    data = [initial]
    for i in range(1, size):        
        data.append(round(data[i-1] ** (1.01)))
    return data

def population_data(size=20):
    year = list(range(1950, 1950 + size))
    population = increase_value(size)
    return [year, population]

def readcsv(filename, fields):
    file = open(filename, 'r', encoding='utf-8-sig')
    file_data = file.read()

    table = [[] for _ in range(len(fields))]

    rows = file_data.split('\n')
    columns = rows[0].split(',')
    indexes = [i for i in range(len(columns)) if columns[i] in fields]
    
    for column in rows[1:]:
        if not column:
            continue
        data = column.split(',')
        for i in range(len(fields)):
            table_data = data[indexes[i]]
            table[i].append(table_data)
          
    return table

def column_data(data, value):
    index = data[0].index(value)
    row = []
    for column in data[1:]:
        row.append(column[index])
    return row
import sys
sys.path.append("../data/")

import matplotlib.pyplot as plt
from generator import population_data, readcsv, column_data

years = [str(x) for x in range(1961, 2016, 5)]
fields = ['Country Code'] + [str(x) for x in range(1961, 2016, 5)]
data = readcsv('../data/world.csv', fields)

countries = ['IND', 'USA', 'PAK', 'CHN', 'PAK']

fig, axes = plt.subplots(figsize=(10, 6))

for country in countries:
    population = [round(int(x)/10**6) for x in column_data(data, country)]
    plt.scatter(years, population, label = country, s=population)

# plt.yticks([])
plt.xlabel('Year')
plt.ylabel('Population (in millions)')
plt.yticks(list(range(0, 1400, 100)))
plt.title('World Population Projection')

plt.show()
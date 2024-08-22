import sys
sys.path.append("../data/")

import matplotlib.pyplot as plt
from generator import readcsv

# x = readcsv('../data/worldcup.csv', ['position'])
# plt.hist(x)
# plt.show()

data = readcsv('../data/worldcup.csv', ['nationality'])
plt.hist(data, orientation= 'horizontal')
plt.show()
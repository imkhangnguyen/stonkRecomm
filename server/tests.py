from matplotlib import pyplot as plt
from random import sample
import lib_import as lib
import timeit
import main

symbols = []

with open("constituents.csv") as f:
    next(f)
    for row in f:
        symbols.append(row.split(',')[0])

x = [5, 10, 15, 30, 40, 60]
y = []

for i in range(len(x)):
  start = timeit.default_timer()
  main.main(sample(symbols, x[i]))
  end = timeit.default_timer()
  y.append(end-start)

plt.plot(x,y)
plt.xlabel('Number of Stocks')
plt.ylabel('Running time (s)')
plt.show()

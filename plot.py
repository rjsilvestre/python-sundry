# Simple plotting example taken from intro to computation and programming using
# python from Guttag. Pylab replace with matplotlib.pyplot as it's use is 
# currently discourage.


import matplotlib.pyplot as pl

principal = 1000
interest_rate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interest_rate
pl.plot(values, 'r--', linewidth = 2)
pl.title('5% Growth, Compounded Annually', fontsize = 'xx-large')
pl.xlabel('Years of Compounding', fontsize = 'medium')
pl.ylabel('Value of Principal ($)', fontsize = 'medium')
pl.show()

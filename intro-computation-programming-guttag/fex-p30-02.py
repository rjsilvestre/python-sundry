# A program that sums all the numbers contained in a string s that contains
# a sequence of decimal numbers separated by commas.

s = '1.23,4.5,6.78'
print(sum(float(num) for num in s.split(',')))

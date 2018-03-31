# A program that sums all the numbers contained in a string s that contains
# a sequence of decimal numbers separated by commas.

s = '1.23,4.5,6.78'
ans = 0
for num in s.split(','):
    ans += float(num)
print(ans)

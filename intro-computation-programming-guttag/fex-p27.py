# A program that asks the user for and int and prints two ints, root and pwr,
# such that 0 < pwr < 6 and root**pwr is equal to the int entered by the user.
# If no such pair of integers exists, it shoulf print a message to that effect

num = int(input('Enter a integer: '))
root = num
pwr = 5
while pwr > 0:
    while root > 0:
        ans = root ** pwr
        if ans == num:
            break
        root -= 1
    if root != 0:
        break
    else:
        root = num
    pwr -= 1
if root != 0:
    print(f'{num} is {root}^{pwr}')
else:
    print('Nothing found.')   # This will never happen since any num == num ** 1

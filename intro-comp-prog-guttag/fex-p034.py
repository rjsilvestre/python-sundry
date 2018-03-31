# A modified program that finds aproximation to the cube root based on a square
# root calculation program. Both negative and posite numbers work.

x = -27
epsilon = 0.01
num_guesses = 0
low = min(x, -1.0)
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('num_guesses =', num_guesses)
print(ans, 'is close to cube root of', x)

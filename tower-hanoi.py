# Towers of Hanoi solution program. Uses recursive calls
# to calculate the movements of each piece on the poles.
# Base on the solution presented on edx mitx 6.00.1x course.


def hanoi(n, init, temp, final):
    '''
    Prints the next movement to be executed 
    or calls itself recursively if needed.

    Args:
        n: int. Number of pieces.
        init: Initial pole name.
        temp: Temporary pole name.
        final: Final pole name.

    Returns:
        None.
    '''
    if n == 1:
        print('Move from:',init, 'to', final)
    else:
        hanoi(n - 1, init, final, temp)
        hanoi(1, init, temp, final)
        hanoi(n - 1, temp, init, final)

# Test case
blocks = int(input('Number of blocks: '))
hanoi(blocks, 'Pole 1', 'Pole 2', 'Pole 3')

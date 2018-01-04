# Closures test file. Creates a simple function that creates returns
# another function. The purpose is to store a string to be used as a
# greeting by the returned function. Example based on the programiz
# website.


def make_greeting(greeting):
    """A function that creates greeting functions."""

    def greet(name):
        """Returns the greeting from the parent function
        with the name taken as argument.
        """
        return(greeting + ', ' + name)
    
    return greet

# Creates the greet 'Hello'
hello = make_greeting('Hello')

# Prints the function object
print(hello)
# Prints the closure object inside the function
print(hello.__closure__)
# Prints the argument passed to the closure function
print(hello.__closure__[0].cell_contents)

# Prints the result of the function
# store in hello variable
print(hello('Isabel'))

# Calls the closure function directly without assignement
# to a variable
print(make_greeting('Holla')('Billy'))

# Creates the greet 'Hi'
hi = make_greeting('Hi')
# Deletes the make_greeting function
del make_greeting
# Both hello and hi still store their greeting
print(hello('Rafael'))
print(hi('Emmanuel'))

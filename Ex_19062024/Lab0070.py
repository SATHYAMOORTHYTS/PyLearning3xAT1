# Lists - list is a collection of items in a particular order
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# how to use list in user define function
numbers = [1, 2, 3, 4, 5]


def do_something(numbers):
    numbers.append(4) # number will be added at last
    numbers[0] = 100
    numbers[4] = 124
    return numbers

l = do_something(numbers) # l = 100
print(l)

from functools import partial

def division(x,y):
    return x/y

divide_by_two = partial(division,2) # this means that 2 is x for division function we already have division(2,y)

print(divide_by_two(6)) #we are passing y value here at the end it calculate division(2,6) = 2/6
print(divide_by_two(11))
print(divide_by_two(7))
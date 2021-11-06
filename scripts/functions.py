def function_new(name, language):
    print('Hello ' + name + ' it is your first ' + language + ' function')

function_new('Paul', 'Python')


def divide(divident, divisor):
    if(divisor == 0):
        return False
    else:
        return divident/divisor

print(divide(5,0))
print(divide(10,2))

def my_function(arg1, arg2 = 'Ford'):
    return f'{arg1} {arg2}'

print(my_function(arg1='car', arg2='Fiat'))
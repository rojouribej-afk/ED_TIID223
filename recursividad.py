

def factorial(n):
    """ Caso base: El factorial de 0 y de 1 es 1 """
    if n == 0:
        return 1
    """ Caso recursivo: n multiplicando por el factorial del numero anterior  """
    return n * factorial(n - 1)

print(factorial(5))
#Перепешите функцию для вычисления чисел фибоначи в рекурсивной форме


def rec_fib(n):
    '''inefficient recursive function as defined, returns Fibonacci number'''
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
print(rec_fib(9))
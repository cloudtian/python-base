# -*- coding: utf-8 -*-

def fact(n):
    '''
    fact doctest

    >>> fact(1)
    1
    >>> fact(3)
    6
    >>> fact('3')
    6
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact('ewr')
    Traceback (most recent call last):
        ...
    TypeError
    '''
    try:
        n = int(n)
    except Exception:
        raise TypeError()
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""

from nose.tools import assert_equal


def check_input(n):
    assert type(n) in [int, long], 'Input must be an integer.'
    assert n >= 0, 'Input must be a non-negative integer.'


def factorial_recursive(n):
    """Calculate factorial in a recursive way
    Args:
      n (int): a non-negative integer
    Returns:
      int: n factorial
    """
    check_input(n)
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)


def factorial_reduce(n):
    """Calculate factorial with python's reduce function
    Args:
      n (int): a non-negative integer
    Returns:
      int: n factorial
    """
    check_input(n)
    if n <= 1:
        return 1
    return reduce(lambda x, y: x*y,
                  xrange(1, n+1))


def factorial_loop(n):
    """Calculate factorial using a loop
    Args:
      n (int): a non-negative integer
    Returns:
      int: n factorial
    """
    check_input(n)
    ans = 1
    while n > 1:
        ans *= n
        n -= 1
    return ans


def test_factorial():
    for func in (factorial_recursive, factorial_reduce, factorial_loop):
        assert_equal(func(0), 1)
        assert_equal(func(1), 1)
        assert_equal(func(5), 120)
        assert_equal(func(6), 720)


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = input("Please enter number of conditions: ")
    norders = factorial_recursive(nconditions)
    print("Number of possible trial orders: " + str(norders))

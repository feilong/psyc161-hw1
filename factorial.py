#!/usr/bin/env python
"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""
from nose.tools import assert_equal, assert_raises


def check_input(n):
    """make sure input is valid for those factorial functions"""
    if type(n) not in [int, long]:
        raise TypeError('Input must be an integer.')
    if n < 0:
        raise ValueError('Input must be a non-negative integer.')


def factorial_recursive(n):
    """Calculate factorial in a recursive way.

    Parameters
    ----------
    n : int
        a non-negative integer

    Returns
    -------
    fact : int
        `n` factorial

    Raises
    ------
    TypeError
        If parameter `n` is not an integer
    ValueError
        If parameter `n` is negative

    """
    check_input(n)
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)


def factorial_reduce(n):
    """Calculate factorial with python's reduce function.

    Parameters
    ----------
    n : int
        a non-negative integer

    Returns
    -------
    fact : int
        `n` factorial

    Raises
    ------
    TypeError
        If parameter `n` is not an integer
    ValueError
        If parameter `n` is negative

    """
    check_input(n)
    if n <= 1:
        return 1
    return reduce(lambda x, y: x*y,
                  xrange(1, n+1))


def factorial_loop(n):
    """Calculate factorial using a loop.

    Parameters
    ----------
    n : int
        a non-negative integer

    Returns
    -------
    fact : int
        `n` factorial

    Raises
    ------
    TypeError
        If parameter `n` is not an integer
    ValueError
        If parameter `n` is negative

    """
    check_input(n)
    ans = 1
    while n > 1:
        ans *= n
        n -= 1
    return ans


def test_factorial():
    """Test those factorial functions."""
    for func in (factorial_recursive, factorial_reduce, factorial_loop):
        assert_raises(ValueError, func, -1)
        assert_raises(TypeError, func, '12')
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

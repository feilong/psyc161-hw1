import time

from factorial import factorial_recursive, factorial_reduce, factorial_loop


def time_elapsed(func, n, repeat=10000):
    t_start = time.clock()
    for j in xrange(repeat):
        func(n)
    t_end = time.clock()
    return t_end - t_start


# for large n's, non-recursive functions only take ~30% of the time
funcs = [('recursive', factorial_recursive),
         ('reduce', factorial_reduce),
         ('loop', factorial_loop)]
for n in [1, 3, 5, 10, 20, 50, 80, 100, 120]:
    times = {}
    for func_name, func in funcs:
        times[func_name] = time_elapsed(func, n)
    print '%3d, %.2f, %.2f' % (
        n,
        times['reduce'] / times['recursive'],
        times['loop'] / times['recursive'])

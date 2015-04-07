import time

from factorial import factorial_recursive, factorial_reduce, factorial_loop


def time_elapsed(func, n, repeat=1000):
    t_start = time.clock()
    for j in xrange(repeat):
        func(n)
    t_end = time.clock()
    return t_end - t_start


# for large n's, non-recursive functions only take ~30% of the time
func_names = ['factorial_recursive', 'factorial_reduce', 'factorial_loop']
for n in [1, 3, 5, 10, 20, 50, 80, 100, 120]:
    times = {}
    for func_name in func_names:
        func = eval(func_name)
        times[func_name] = time_elapsed(func, n)
    print '%3d, %.2f, %.2f' % (
        n,
        times['factorial_reduce'] / times['factorial_recursive'],
        times['factorial_loop'] / times['factorial_recursive'])

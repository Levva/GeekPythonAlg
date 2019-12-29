import cProfile
import functools

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} ok!')

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


cProfile.run('fib(200)')

# test_fib(fib)

# task_0.fib(10)
# 1000 loops, best of 3: 47.6 usec per loop

# task_0.fib(15)
# 1000 loops, best of 3: 951 usec per loop

# task_0.fib(20)
# 1000 loops, best of 3: 3.72 msec per loop

# task_0.fib(25)
# 1000 loops, best of 3: 45 msec per loop

# cProfile.run('fib(10)')
# 180 function calls (4 primitive calls) in 0.000 seconds
# 177/1    0.000    0.000    0.000    0.000 task_0.py:11(fib)

# cProfile.run('fib(15)')
# 1976 function calls(4 primitive calls) in 0.001 seconds
# 1973/1    0.001    0.000    0.001    0.001 task_0.py:11(fib)

# cProfile.run('fib(20)')
# 21894 function calls (4 primitive calls) in 0.006 seconds
# 21891/1    0.006    0.000    0.006    0.006 task_0.py:11(fib)
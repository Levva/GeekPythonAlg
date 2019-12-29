import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} ok!')

def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n-1) + _fib_list(n-2)
        return fib_l[n]
    return _fib_list(n)

# test_fib(fib_list)

# 1000 loops, best of 3: 15.4 usec per loop  -> 10
# 1000 loops, best of 3: 12.1 usec per loop  -> 20
# 1000 loops, best of 3: 57.8 usec per loop  -> 100
# 1000 loops, best of 3: 86.3 usec per loop  -> 200
# 1000 loops, best of 3: 482 usec per loop  -> 500


cProfile.run('fib_list(500)')


# 19/1    0.000    0.000    0.000    0.000 task_000.py:14(_fib_list)  10
# 39/1    0.000    0.000    0.000    0.000 task_000.py:14(_fib_list)  20
# 199/1    0.000    0.000    0.000    0.000 task_000.py:14(_fib_list)  100
# 999/1    0.001    0.000    0.001    0.001 task_000.py:14(_fib_list)  500
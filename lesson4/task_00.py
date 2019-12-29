import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} ok!')

def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n-1) + _fib_dict(n-2)
        return fib_d[n]
    return _fib_dict(n)

# test_fib(fib_dict)

# task_00.fib_dict(10)
# 1000 loops, best of 3: 3.69 usec per loop

# "task_00.fib_dict(15)"
# 1000 loops, best of 3: 6.81 usec per loop

# "task_00.fib_dict(20)"
# 1000 loops, best of 3: 9.74 usec per loop

# "task_00.fib_dict(100)"
# 1000 loops, best of 3: 38.3 usec per loop

#  "task_00.fib_dict(200)"
# 1000 loops, best of 3: 86.7 usec per loop

#  "task_00.fib_dict(500)"
# 1000 loops, best of 3: 542 usec per loop

cProfile.run('fib_dict(10)')
# 19/1    0.000    0.000    0.000    0.000 task_00.py:13(_fib_dict)

cProfile.run('fib_dict(20)')
# 39/1    0.000    0.000    0.000    0.000 task_00.py:13(_fib_dict)

cProfile.run('fib_dict(100)')
# 199/1    0.000    0.000    0.000    0.000 task_00.py:13(_fib_dict)

cProfile.run('fib_dict(500)')
# 999/1    0.001    0.000    0.001    0.001 task_00.py:13(_fib_dict)
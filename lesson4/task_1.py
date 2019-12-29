from collections import OrderedDict

a = {'cat':5, 'dog':2, 'mouse':4}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))

print(new_a)

b = {'cat':5, 'dog':4, 'mouse':2}
new_b = OrderedDict(sorted(b.items(), key=lambda x: x[1]))

print(new_b)
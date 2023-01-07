from itertools import accumulate
from itertools import groupby
from itertools import product
from itertools import permutations
from itertools import combinations
import operator

a = [1, 2, 3, 4]
b = [5, 6]
acc = accumulate(a)
print(list(acc))

prods = accumulate(a, func=operator.mul)
print(list(prods))

group = groupby(a, key=lambda x: x < 3)
for k, v in group:
    print(k, list(v))

prod = product(a, b)
print(list(prod))

perms = permutations(b)
print(list(perms))

combs = combinations(a, 3)
print(list(combs))

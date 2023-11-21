import random
import itertools
import operator
import functools

def get_var_name(variable):
    for name, value in globals().items():
        if value is variable:
            return name

def test(XX, XY):
    TT = list(itertools.combinations(XX, XY))
    for x in TT:
        TY = [get_var_name(el) for el in x]
        APA = [set(i) for i in x]
        intersection = functools.reduce(operator.and_, APA)
        if len(intersection) >= 1:
            print(f'{TY} : {intersection}')

######################################### TEST ####################################

A = [random.randint(1, 10) for _ in range(5)]
B = [random.randint(1, 10) for _ in range(7)]
C = [random.randint(1, 10) for _ in range(5)]
D = [random.randint(1, 10) for _ in range(10)]
E = [random.randint(1, 10) for _ in range(5)]


display(A,B,C,D,E)

letters = [A, B, C, D, E]

for x in range(2, len(letters) + 1):
    test(letters, x)

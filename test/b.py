import numpy as np
from pymoo.model.population import Population
from pymoo.model.individual import Individual
import autograd.numpy as anp



def interleaving_args(*args, kwargs=None):
    if len(args) % 2 != 0:
        raise Exception(f"Even number of arguments are required but {len(args)} arguments were provided.")

    if kwargs is None:
        kwargs = {}

    for i in range(int(len(args) / 2)):
        key, values = args[i * 2], args[i * 2 + 1]
        kwargs[key] = values
    return kwargs


def new( *args, **kwargs):
    if len(args) == 1:
        kk = 1
    else:

        kwargs = interleaving_args(*args, kwargs=kwargs)
        iterable = [v for _, v in kwargs.items() if hasattr(v, '__len__') and not isinstance(v, str)]

        if len(iterable) == 0:
            b=1
        else:
            n = np.unique(np.array([len(v) for v in iterable]))
        if len(n) == 1:
            n = n[0]
        a = 1
        pop = Population(5)
        pop.set(*args, **kwargs)
        return pop



X = np.full((5, 10), 0, dtype=np.int)
for i in range(5):
    X[i, :] = np.random.permutation(10)
pop = new("X", X)

f1 = X[:, 0]
g = 1 + 9.0 / (10 - 1) * anp.sum(X[:, 1:], axis=1)
f2 = g * (1 - anp.power((f1 / g), 0.5))


d=1

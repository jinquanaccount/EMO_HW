from pymoo.algorithms.moead import MOEAD
from pymoo.model.algorithm import Algorithm
from pymoo.optimize import minimize
from pymoo.factory import get_problem, get_visualization, get_reference_directions
from pymoo.model.problem import Problem
from pymoo.algorithms.so_genetic_algorithm import GA
from pymoo.optimize import minimize
from pymoo.factory import get_algorithm, get_crossover, get_mutation, get_sampling
from pymoo.problems.single.traveling_salesman import create_random_tsp_problem
from pymoo.util.termination.default import SingleObjectiveDefaultTermination
from pymoo.algorithms.so_genetic_algorithm import GA
from pymoo.optimize import minimize
from pymoo.factory import get_algorithm, get_crossover, get_mutation, get_sampling
from pymoo.problems.single.traveling_salesman import create_random_tsp_problem
import pymoo.problems.multi.zdt
import pymoo.problems.multi.bnh
from pymoo.factory import get_problem, get_visualization, get_reference_directions

problem = get_problem("dtlz2")

algorithm = MOEAD(
    get_reference_directions("das-dennis", 2, n_partitions=100),
    n_neighbors=15,
    decomposition="pbi",
    prob_neighbor_mating=0.7,
    seed=1
)

res = minimize(problem, algorithm, termination=('n_gen', 200))

get_visualization("scatter").add(res.F).show()

from pymoo.algorithms.moead import MOEAD
from pymoo.util.display import MultiObjectiveDisplay
from pymoo.operators.sampling.random_permutation_sampling import PermutationRandomSampling
from pymoo.operators.crossover.order_crossover import OrderCrossover
from pymoo.operators.mutation.inversion_mutation import InversionMutation


class Smy_Algorithm(MOEAD):
    def __init__(self,
                 ref_dirs,
                 n_neighbors=20,
                 decomposition='auto',
                 prob_neighbor_mating=0.9,
                 display=MultiObjectiveDisplay(),
                 **kwargs):
        """

        Smy_Algorithm Algorithm.

        Parameters
        ----------
        ref_dirs
        n_neighbors
        decomposition
        prob_neighbor_mating
        display
        kwargs
        """
        kwargs['sampling'] = PermutationRandomSampling()
        kwargs['crossover'] = OrderCrossover(prob=1.0)
        kwargs['mutation'] = InversionMutation(prob=1.0)

        super().__init__(ref_dirs,
                         n_neighbors,
                         decomposition,
                         prob_neighbor_mating,
                         display,
                         **kwargs)

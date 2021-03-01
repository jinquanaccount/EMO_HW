import numpy as np
from pymoo.model.problem import Problem
import copy
from search_method.seacrh_method_smy.my_pack import my_pack


class Smy_Problem(Problem):
    def __init__(self,
                 raw_num_heap_map,
                 raw_box_id_list,
                 raw_my_bin_list,
                 raw_date_string,
                 raw_platform_must_first_map,
                 raw_distance_map,
                 **kwargs):
        """

        Parameters
        ----------
        raw_num_heap_map : list
            number of total heaps

        """
        self.raw_num_heap_map = copy.deepcopy(raw_num_heap_map)
        self.raw_box_id_list = copy.deepcopy(raw_box_id_list)
        self.raw_my_bin_list = copy.deepcopy(raw_my_bin_list)
        self.raw_date_string = copy.deepcopy(raw_date_string)
        self.raw_platform_must_first_map = copy.deepcopy(raw_platform_must_first_map)
        self.raw_distance_map = copy.deepcopy(raw_distance_map)
        n_heaps = len(raw_num_heap_map)

        super(Smy_Problem, self).__init__(
            n_var=n_heaps,
            n_obj=2,
            xl=0,
            xu=n_heaps,
            type_var=np.int,
            elementwise_evaluation=False,
            **kwargs
        )

    def _evaluate(self, x, out, *args, **kwargs):
        temp_list = []
        for i in range(x.shape[0]):
            temp_list.append(my_pack(list(x[i]),
                                     self.raw_num_heap_map,
                                     self.raw_box_id_list,
                                     self.raw_my_bin_list,
                                     self.raw_date_string,
                                     self.raw_platform_must_first_map,
                                     self.raw_distance_map
                                     ))
        f = np.array(temp_list)
        out['F'] = f
        print(out)
        print(x.shape)

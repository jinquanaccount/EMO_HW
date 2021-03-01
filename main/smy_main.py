import numpy as np
from IO.Workspace import Workspace as wsp
from IO import IO
from factory.smy_factory import *
from my_entity.entity import *
from search_method.seacrh_method_smy.smy_algorithm import Smy_Algorithm
from search_method.seacrh_method_smy.smy_problem import Smy_Problem
from pymoo.optimize import minimize
from pymoo.factory import get_visualization, get_reference_directions
from search_method.seacrh_method_smy.my_pack import my_pack

directory = 'C:/Users/seusmy/Desktop/竞赛/dataset/dataset'
raw_file = "E1598428999777"
result_file = "E1598428999777.json"

# 初始化工作空间
ws = wsp(directory=directory, raw=raw_file, result=result_file)
raw_date_string = IO.read_json_file_to_string(ws.raw)
raw_date_dictionary = IO.read_json_file_to_dictionary(ws.raw)

# 同一站点相同规格的box定义为heap，并对heap集合建立索引
raw_my_bin_list = creat_my_bin_list_from_truck_dict_list(
    raw_date_dictionary["algorithmBaseParamDto"]["truckTypeDtoList"])
raw_my_bin_list.sort(key=lambda x: x.max_vol * x.max_Load, reverse=True)
raw_box_id_list = creat_box_id_list_from_box_dict_list(raw_date_dictionary["boxes"])
raw_ag_box_list = creat_box_list_from_box_dict_list(raw_date_dictionary["boxes"])
raw_heap_list = create_heap_list(raw_ag_box_list)
raw_num_heap_map = list_to_dict_by_index(raw_heap_list)
raw_distance_map = raw_date_dictionary["algorithmBaseParamDto"]["distanceMap"]
raw_platform_must_first_map = creat_raw_platform_must_first_map(
    raw_date_dictionary["algorithmBaseParamDto"]["platformDtoList"])

# 将解模式定义为heap序列，将解模式参数定义为序列顺序，一个解模式绑定一个方向向量，使用MOEAD算法搜索确定解模式参数
problem = Smy_Problem(raw_num_heap_map,
                      raw_box_id_list,
                      raw_my_bin_list,
                      raw_date_string,
                      raw_platform_must_first_map,
                      raw_distance_map
                      )
algorithm = Smy_Algorithm(get_reference_directions("das-dennis", 2, n_partitions=10),
                          n_neighbors=8,
                          prob_neighbor_mating=0.7)
res = minimize(problem, algorithm, termination=('n_gen', 10))
print("------res.X______")
print(res.X)
get_visualization("scatter").add(res.F).show()


# 解模式内搜索


# 将最终结果写出到工作空间输出目录




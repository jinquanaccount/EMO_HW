from my_entity.entity import *


def creat_my_bin_list_from_truck_dict_list(truck_dict_list):
    my_bin_list = []
    for truck in truck_dict_list:
        my_bin_list.append(
            My_Bin(truck['truckTypeCode'], truck['length'], truck['width'], truck['height'], truck['maxLoad']))
    return my_bin_list


def creat_box_list_from_box_dict_list(box_dict_list):
    box_list = []
    for box in box_dict_list:
        box_list.append(
            Ag_Box(box['length'], box['width'], box['height'], box['weight'], box['spuBoxId'], box['platformCode']))
    return box_list


def creat_box_id_list_from_box_dict_list(box_dict_list):
    box_id_list = []
    for box in box_dict_list:
        box_id_list.append(box['spuBoxId'])
    return box_id_list


def create_heap_list(box_list):
    heap_list = []
    for box in box_list:
        flag = 1
        for heap in heap_list:
            if flag == 0:
                break
            for temp_box in heap.box_list:
                if (box.d1 == temp_box.d1 and box.d2 == temp_box.d2 and box.platform_code == heap.platform_code) or \
                        (box.d2 == temp_box.d1 and box.d1 == temp_box.d2 and box.platform_code == heap.platform_code):
                    heap.add_box(box)
                    flag = 0
                    break
        if flag == 1:
            temp_box_list = [box]
            heap_list.append(Heap(temp_box_list, box.platform_code))
    return heap_list


def list_to_dict_by_index(temp_list):
    temp_dict = {}
    for i in range(len(temp_list)):
        temp_dict[i] = temp_list[i]
    return temp_dict


def creat_path_and_box_ids_from_solution_mode_and_residual_box_id_list(solution_mode, num_heap_map,
                                                                       raw_platform_must_first_map):
    path = []
    box_ids = []
    for num in solution_mode:
        if num_heap_map[num].box_num > 0:
            if len(path) == 0:
                path.append(num_heap_map[num].platform_code)
                for box in num_heap_map[num].box_list:
                    box_ids.append(box.box_id)
            else:
                if num_heap_map[num].platform_code == path[-1]:
                    for box in num_heap_map[num].box_list:
                        box_ids.append(box.box_id)
                else:
                    if num_heap_map[num].platform_code not in path and \
                            not raw_platform_must_first_map[num_heap_map[num].platform_code]:
                        path.append(num_heap_map[num].platform_code)
                        for box in num_heap_map[num].box_list:
                            box_ids.append(box.box_id)
    paths = [path]
    return paths, box_ids


def creat_raw_platform_must_first_map(raw_platform_list):
    raw_platform_must_first_map = {}
    for i in raw_platform_list:
        raw_platform_must_first_map[i["platformCode"]] = i["mustFirst"]
    return raw_platform_must_first_map


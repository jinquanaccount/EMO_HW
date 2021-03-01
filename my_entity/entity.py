import copy


class Heap:
    def __init__(self,
                 box_list=None,
                 platform_code=None):
        self.box_list = copy.deepcopy(box_list)
        self.box_num = len(self.box_list)
        self.weight = self.total_weight()
        self.volume = self.total_volume()
        self.platform_code = platform_code

        """
        docstring here
            :param box_list: 组成块的箱子
            :param box_num: 组成箱子个数
            :param platform_code: 块所在的提货点
            :param weight=0: 堆的总重量
            :param volume=0: 块的箱子总体积 
        """

    def total_weight(self):
        weight = 0
        for box in self.box_list:
            weight += box.weight
        return weight

    def total_volume(self):
        volume = 0
        for box in self.box_list:
            volume += box.volume
        return volume

    def update_by_total_box_list_by_id(self, total_box_id_list):
        temp_box_list = []
        for my_box in self.box_list:
            for box_id in total_box_id_list:
                if my_box.box_id == box_id:
                    temp_box_list.append(my_box)
        self.box_list = temp_box_list
        self.update()

    def add_box(self, box):
        self.box_list.append(box)
        self.update()

    def update(self):
        self.weight = self.total_weight()
        self.box_num = len(self.box_list)


class Ag_Box:
    def __init__(self,
                 d1=0,
                 d2=0,
                 height=0,
                 weight=0,
                 box_id=None,
                 platform_code=None):
        self.d1 = d1
        self.d2 = d2
        self.height = height
        self.weight = weight
        self.volume = d1 * d2 * height
        self.box_id = box_id
        self.platform_code = platform_code


class My_Bin:
    def __init__(self,
                 truck_id,
                 length,
                 width,
                 height,
                 max_load):
        self.truck_id = truck_id
        self.length = length
        self.width = width
        self.height = height
        self.max_Load = max_load
        self.max_vol = length * width * height


class My_Platform:
    def __init__(self,
                 must_first):
        self.must_first = must_first

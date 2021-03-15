# -*- coding: utf-8 -*-
# @Time    : 2021/3/13 17:25
# @Author  : DannyDong
# @File    : Forward.py
# @describe: 前置条件

import time
import random
import string


# 前置条件-Mock数据
class ForwardMock(object):
    def __init__(self):
        self.num = random.randint(99, 1000)
        eng_list = string.ascii_letters
        self.eng = random.choice(eng_list)
        self.eng1 = random.choice(eng_list)

    # 生成Mock数据类型
    def generate_mock_data(self, mock_type):
        mock_dict = {
            'studentName': '学员', 'staffName': '员工', 'courseName': '课程', 'className': '班级',
            'goodsName': '物品', 'mixName': '杂费', 'courseGroups': '课时包', 'studentNotice': '学员通知',
            'dimension': '评价维度', 'rules': '课酬规则', 'expenses': '支出费用', 'parameter': '字段参数',
            'publicity': '机构宣传语', 'noticeWord': '学员提醒语'
        }
        return "AAT{}{}{}".format(mock_dict[mock_type], self.num, self.eng)

    # 生成数字类型
    @staticmethod
    def generate_num(num_type, up, down):
        # 生成数字(int)
        if mock_type == 1:
            result = random.randint(up, down)
        # 生成数字(float)
        elif mock_type == 2:
            num_float = random.uniform(up, down)
            result = round(num_float, 2)
        else:
            raise Exception('Num Type Error')
        return result

    @staticmethod
    # 生成电话号码
    def generate_phone():
        return "9{}".format(random.randint(999999999, 10000000000))

    # 生成单位&规格
    @staticmethod
    def generate_unit(unit_type):
        # 生成物品单位
        if mock_type == 1:
            unit_list = ['个', '只', '根', '瓶', '杯', '台']
        # 生成物品规格
        elif mock_type == 2:
            unit_list = ['S', 'L', 'M', '极简版', '家庭版', '专业版', '旗舰版']
        else:
            raise Exception('Unit Type Error')
        return random.choice(unit_list)


# 前置条件-测试用例（深度优先搜索dfs）
class ForwardCase(object):
    def __init__(self):
        pass

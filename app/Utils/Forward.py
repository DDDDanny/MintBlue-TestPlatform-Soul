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

    # 选择mock数据类型
    def select_mock_type(self, mock_type, up=0, down=0):
        result = ''
        # 生成学员姓名
        if mock_type == 'studentName':
            result = "AAT学员{}{}".format(self.num, self.eng)
        # 生成员工姓名
        elif mock_type == 'staffName':
            result = "AAT员工{}{}".format(self.num, self.eng)
        # 生成课程名称
        elif mock_type == 'courseName':
            result = "AAT课程{}{}".format(self.num, self.eng)
        # 生成班级名称
        elif mock_type == 'className':
            result = "AAT班级{}{}".format(self.num, self.eng)
        # 生成物品名称
        elif mock_type == 'goodsName':
            result = "AAT物品{}{}".format(self.num, self.eng)
        # 生成杂费名称
        elif mock_type == 'mixName':
            result = "AAT杂费{}{}".format(self.num, self.eng)
        # 生成课时包名称
        elif mock_type == 'courseGroups':
            result = "AAT课时包{}{}".format(self.num, self.eng)
        # 生成学员通知标题
        elif mock_type == 'studentNotice':
            result = "AAT学员通知{}{}".format(self.num, self.eng)
        # 生成评价维度标题
        elif mock_type == 'dimension':
            result = "AAT评价维度{}{}".format(self.num, self.eng)
        # 生成课酬规则标题
        elif mock_type == 'rules':
            result = "AAT课酬规则{}{}".format(self.num, self.eng)
        # 生成支出费用名称
        elif mock_type == 'expenses':
            result = "AAT支出费用{}{}".format(self.num, self.eng)
        # 生成字段参数名称
        elif mock_type == 'parameter':
            result = "AAT字段参数{}{}".format(self.num, self.eng)
        # 生成机构宣传语
        elif mock_type == 'Publicity':
            result = "AAT机构宣传语{}{}".format(self.num, self.eng)
        # 生成学员提醒语
        elif mock_type == 'noticeWord':
            result = "AAT学员提醒语{}{}".format(self.num, self.eng)
        # 生成数字(int)
        elif mock_type == 15:
            result = random.randint(up, down)
        # 生成数字(float)
        elif mock_type == 16:
            num_float = random.uniform(up, down)
            result = round(num_float, 2)
        # 生成电话号码
        elif mock_type == 'phoneNumber':
            phone = random.randint(999999999, 10000000000)
            result = "9{}".format(phone)
        # 生成物品单位
        elif mock_type == 18:
            unit_list = ['个', '只', '根', '瓶', '杯', '台']
            result = random.choice(unit_list)
        # 生成物品规格
        elif mock_type == 19:
            specs_list = ['S', 'L', 'M', '极简版', '家庭版', '专业版', '旗舰版']
            result = random.choice(specs_list)

        return result


# 前置条件-测试用例（深度优先搜索dfs）
class ForwardCase(object):
    def __init__(self):
        pass

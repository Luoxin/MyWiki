'''
字典是另一种可变容器模型，且可存储任意类型对象
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
d = {key1 : value1, key2 : value2 }
'''

# 定义方法
is_dict = dict()
print(is_dict, type(is_dict))

is_dict = {}
print(is_dict, type(is_dict))

# dict的常用方法
is_dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print(is_dict["Name"])  # 通过key获取值

print(is_dict.keys())  # 打印所有key
print(is_dict.values())  # 所有value
print(is_dict.items())  # 整个字典

print(is_dict.__len__())  # 输出长度

# 增加修改值
is_dict[1] = 10  # 增加值
print(is_dict)

is_dict[1] = 11  # 修改值
print(is_dict)

del is_dict[1]  # 删除值
print(is_dict)

is_dict.pop("Age")
print(is_dict)

print(is_dict.popitem())  # 随机输出一个键值对并删除
print(is_dict)

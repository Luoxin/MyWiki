'''
list是列表，类似于数组，不过Python的数据内的数据类型是可变的
'''

# 定义方法
is_list = []
print(is_list, type(is_list))

is_list = list()
print(is_list, type(is_list))

is_list = [i for i in range(10)]  # 通过迭代器生成列表，暂且记得有这种用法，后面会详细说明
print(is_list, type(is_list))


print("*" * 40)
# list的常用方法
is_list_initial = [i for i in range(10)]
print("这是一个原始的list", is_list_initial, type(is_list_initial))

print(is_list_initial[4])  # 通过索引获取值

is_list_initial.append(10)  # 通过append函数,只能添加到对位
print("通过append函数,只能添加到对位", is_list_initial, type(is_list_initial))

is_list_initial.insert(0, "start")  # 通过insert函数将元素添加到指定位置
print("通过insert函数将元素添加到指定位置", is_list_initial, type(is_list_initial))

print(is_list_initial.pop(0))  # 通过pop将第一位元素返回并删除，默认为移除最后一位
print("通过pop将第一位元素返回并删除，默认为移除最后一位", is_list_initial, type(is_list_initial))

is_list_initial.remove(0)  # 通过remove移除第一位
print("通过remove移除第一位", is_list_initial, type(is_list_initial))

print("查找3所在的位置", is_list_initial.index(3), type(is_list_initial))# 查找3所在的位置

print("输出长度", is_list_initial.__len__(), type(is_list_initial))# 输出长度

print("查找5出现的次数", is_list_initial.count(5), type(is_list_initial))# 查找5出现的次数



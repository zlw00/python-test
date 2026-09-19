from random import random

# print("hello")
# print(321 // 123)
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * 3.1416 * radius
# area = 3.1416 * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))
# value = float(input('输入长度：'))
# unit = input('输入单位：')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))

# import random
# answer = random.randint(0,100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入：'))
#     if number == answer:
#         print('回答正确')
#         break
#     elif number > answer:
#         print('大了')
#     else :
#         print('小了')
# print('你一共猜了%d次' % counter)
# print(f'你一共猜了{answer}次') #新写法
#
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)
# items3 = []
# for x in 'ABC':
#     for y in '12':
#         items3.append(x + y)
# print(items3)
# a, b, *c = range(1, 10)
# print(a, b, c)
# a, b, c = [1, 10, 100]
# print(a, b, c)
# a, *b, c = 'hello'
# print(a, b, c)、



# s1 = 'hello, world!'
# s2 = "你好，世界！"
# print(s1, s2)
# # 以三个双引号或单引号开头的字符串可以折行
# s3 = '''
# hello,
# world!
# '''
# print(s3, end='')


# s1 = '\'hello, world!\''
# print(s1)
# s2 = '\\hello, world!\\'
# print(s2)

# 字符串s1中\t是制表符，\n是换行符
# s1 = '\time up \now'
# print(s1)
# # 字符串s2中没有转义字符，每个字符都是原始含义
# s2 = r'\time up \now'
# print(s2)


# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1, s2)

# set1 = set()
# set1.add(33)
# set1.add(55)
# set1.update({1, 10, 100, 1000})
# print(set1)

# set1 = frozenset({1, 3, 5, 7})
# set2 = frozenset(range(1, 6))
# print(set1 & set2)    # frozenset({1, 3, 5})
# print(set1 | set2)    # frozenset({1, 2, 3, 4, 5, 7})
# print(set1 - set2)    # frozenset({7})
# print(set1 < set2)    # False

# xinhua = {
#     '麓': '山脚下',
#     '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
#     '蕗': '甘草的别名',
#     '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
# }
# print(xinhua)
# person = {
#     'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号',
#     'home': '中同仁路8号', 'tel': '13122334455', 'econtact': '13800998877'
# }
# print(person)

# 字典中的值又是一个字典(嵌套的字典)
# students = {
#     1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
#     1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
#     1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
# }
#
# # 使用get方法通过键获取对应的值，如果取不到不会引发KeyError异常而是返回None或设定的默认值
# print(students.get(1002))    # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
# print(students.get(1005))    # None
# print(students.get(1005, {'name': '无名氏'}))    # {'name': '无名氏'}
#
# # 获取字典中所有的键
# print(students.keys())      # dict_keys([1001, 1002, 1003])
# # 获取字典中所有的值
# print(students.values())    # dict_values([{...}, {...}, {...}])
# # 获取字典中所有的键值对
# print(students.items())     # dict_items([(1001, {...}), (1002, {....}), (1003, {...})])
# # 对字典中所有的键值对进行循环遍历
# for key, value in students.items():
#     print(key, '--->', value)
#
# # 使用pop方法通过键删除对应的键值对并返回该值
# stu1 = students.pop(1002)
# print(stu1)             # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
# print(len(students))    # 2
# # stu2 = students.pop(1005)    # KeyError: 1005
# stu2 = students.pop(1005, {})
# print(stu2)             # {}
#
# # 使用popitem方法删除字典中最后一组键值对并返回对应的二元组
# # 如果字典中没有元素，调用该方法将引发KeyError异常
# key, value = students.popitem()
# print(key, value)    # 1003 {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
#
# # 如果这个键在字典中存在，setdefault返回原来与这个键对应的值
# # 如果这个键在字典中不存在，向字典中添加键值对，返回第二个参数的值，默认为None
# result = students.setdefault(1005, {'name': '方启鹤', 'sex': True})
# print(result)        # {'name': '方启鹤', 'sex': True}
# print(students)      # {1001: {...}, 1005: {...}}
#
# # 使用update更新字典元素，相同的键会用新值覆盖掉旧值，不同的键会添加到字典中
# others = {
#     1005: {'name': '乔峰', 'sex': True, 'age': 32, 'place': '北京大兴'},
#     1010: {'name': '王语嫣', 'sex': False, 'age': 19},
#     1008: {'name': '钟灵', 'sex': False}
# }
# students.update(others)
# print(students)      # {1001: {...}, 1005: {...}, 1010: {...}, 1008: {...}}


# def add(*args):
#     total = 0
#     for arg in args:
#         if type(arg) in (int, float):
#             total +=arg
#     return total
# print(add(1,2,3,4,5))
# print(add(1,2,3,4,5))

# def get_suffix(filename, ignore_dot=True):
#     """获取文件名的后缀名
#
#     :param filename: 文件名
#     :param ignore_dot: 是否忽略后缀名前面的点
#     :return: 文件的后缀名
#     """
#     # 从字符串中逆向查找.出现的位置
#     pos = filename.rfind('.')
#     # 通过切片操作从文件名中取出后缀名
#     if pos <= 0:
#         return ''
#     return filename[pos + 1:] if ignore_dot else filename[pos:]

# from os.path import splitext
# def get_suffix(filename, ignore_dot=True):
#     print(splitext(filename))
#
# get_suffix("test.txt")

# import random
# import time
#
#
# def download(filename):
#     print(f'开始下载{filename}.')
#     time.sleep(random.randint(2, 6))
#     print(f'{filename}下载完成.')
#
#
# def upload(filename):
#     print(f'开始上传{filename}.')
#     time.sleep(random.randint(4, 8))
#     print(f'{filename}上传完成.')
#
# # 定义装饰器函数，它的参数是被装饰的函数或类
# def record_time(func):
#     # 定义一个带装饰功能（记录被装饰函数的执行时间）的函数
#     # 因为不知道被装饰的函数有怎样的参数所以使用*args和**kwargs接收所有参数
#     # 在Python中函数可以嵌套的定义（函数中可以再定义函数）
#     def wrapper(*args, **kwargs):
#         # 在执行被装饰的函数之前记录开始时间
#         start = time.time()
#         # 执行被装饰的函数并获取返回值
#         result = func(*args, **kwargs)
#         # 在执行被装饰的函数之后记录结束时间
#         end = time.time()
#         # 计算和显示被装饰函数的执行时间
#         print(f'{func.__name__}执行时间: {end - start:.3f}秒')
#         # 返回被装饰函数的返回值（装饰器通常不会改变被装饰函数的执行结果）
#         return result
#
#     # 返回带装饰功能的wrapper函数
#     return wrapper
#
# download = record_time(download)
# upload = record_time(upload)
# download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')



# import time
#
#
# # 定义数字时钟类
# class Clock(object):
#     """数字时钟"""
#
#     def __init__(self, hour=0, minute=0, second=0):
#         """初始化方法
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self.hour = hour
#         self.min = minute
#         self.sec = second
#
#     def run(self):
#         """走字"""
#         self.sec += 1
#         if self.sec == 60:
#             self.sec = 0
#             self.min += 1
#             if self.min == 60:
#                 self.min = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
#
#     def show(self):
#         """显示时间"""
#         return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'
#
#
# # 创建时钟对象
# clock = Clock(23, 59, 58)
# while True:
#     # 给时钟对象发消息读取时间
#     print(clock.show())
#     # 休眠1秒钟
#     time.sleep(1)
#     # 给时钟对象发消息使其走字
#     clock.run()
#
# import csv
# import random
#
# with open('scores2.csv', 'w') as file:
#     writer = writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
#     writer.writerow(['姓名', '语文', '数学', '英语'])
#     names = ['关羽', '张飞', '赵云', '马超', '黄忠']
#     for name in names:
#         scores = [random.randrange(50, 101) for _ in range(3)]
#         scores.insert(0, name)
#         writer.writerow(scores)

# with open('scores.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#
# with open('scores.csv', 'r') as file:
#     reader = csv.reader(file)
#     for data_list in reader:
#         print(reader.line_num, end='\t')
#         for elem in data_list:
#             print(elem, end='\t')

#         print()

# with open('scores2.csv', 'r') as file:
#     read = csv.reader(file, delimiter='|')
#     for row in read:
#         print(row)
#
#

# import os
# print(os.environ.get("HOME"))      # 用户主目录 /Users/zhangluwen
# print(os.environ.get("PATH"))      # 系统查找命令的路径（和虚拟环境强相关）
# print(os.environ.get("SHELL"))      # 你的终端 zsh


#。查询 GitHub 用户信息并保存为本地 JSON 文件



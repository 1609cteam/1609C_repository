# # # # # # # # # def num(k, n):
# # # # # # # # #     return ''.join(map(str, range(n + 1))).count(str(k))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # number = num(1, 12)
# # # # # # # # # print(number)
# # # # # # # #
# # # # # # # # # print({x ** 2: x for x in range(5, 0, -1)})
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def select(list, d):
# # # # # # # # #     dict = {}
# # # # # # # # #     for i in list:
# # # # # # # # #         if i + d in list:
# # # # # # # # #             dict[i] = i + d
# # # # # # # # #     return dict
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# # # # # # # # # print(select(list, 2))
# # # # # # # # #
# # # # # # # # # list = ['axcd', 'sxe', 'jo68', 'o1q', 'u98', 'axcd', 'o1q']
# # # # # # # # # list1 = []
# # # # # # # # #
# # # # # # # # # list1.append([i for i in sorted(set(list))])
# # # # # # # # # print(list1)
# # # # # # # #
# # # # # # # # # print(sorted(set(['axcd', 'sxe', 'jo68', 'o1q', 'u98', 'axcd', 'o1q'])))
# # # # # # # # a = [1, 2, 3]
# # # # # # # # b = [1, 2, 3]
# # # # # # # #
# # # # # # # # print(a is b)
# # # # # # #
# # # # # # # # a = [1, 5, '', 3, 2, 6, 8, 3, '', 7, '']
# # # # # # # # number = [i for i in a if i != '']
# # # # # # # # import re
# # # # # # # #
# # # # # # # # a = 'abbsbbc'
# # # # # # # # print(re.sub(r'b+', 'b', a))
# # # # # # #
# # # # # # # # def flat(nums):
# # # # # # # #     res = []
# # # # # # # #     for i in nums:
# # # # # # # #         if isinstance(i, list):
# # # # # # # #             res.extend(flat(i))
# # # # # # # #         else:
# # # # # # # #             res.append(i)
# # # # # # # #     return res
# # # # # # # #
# # # # # # # #
# # # # # # # # a = [1, [2, 3, [4.5, 5, [6, 7, [8, [9, ['!'], 11], 'asd'], 13], 14], 15], 16]
# # # # # # # # print(flat(a))
# # # # # # #
# # # # # # #
# # # # # # # a = [1, 2, 3, 4]
# # # # # # #
# # # # # # #
# # # # # # # def fun(x):
# # # # # # #     if x % 2 == 0:
# # # # # # #         return 0
# # # # # # #     else:
# # # # # # #         return 1
# # # # # # #
# # # # # # #
# # # # # # # print(list(map(fun, a)))
# # # # # # #
# # # # # # #
# # # # # # # def fun(x):
# # # # # # #     if x % 2 == 0:
# # # # # # #         return x
# # # # # # #
# # # # # # #
# # # # # # # print(list(filter(fun, a)))
# # # # # #
# # # # # # a, b, c = 0, 1, []
# # # # # # while b < 1000:
# # # # # #     c.append(b)
# # # # # #     a, b = b, a + b
# # # # # # print(c)
# # # # #
# # # # #
# # # # # def order_str(str):
# # # # #     return str[::-1]
# # # # #
# # # # #
# # # # # if __name__ == '__main__':
# # # # #     a = input('请输入一个字符串：')
# # # # #     print(order_str(a))
# # # #
# # # # b1 = [1, 2, 3]
# # # # b2 = [2, 3, 4]
# # # # b3, b4 = [], []
# # # # for i in b1:
# # # #     if i in b2:
# # # #         b3.append(i)
# # # #     else:
# # # #         b4.append(i)
# # # # print('交集', b3)
# # # # print('差集', b4)
# # #
# arr = [7, 4, 3, 67, 34, 1, 8]
#
#
# def list_sort(arr):
#     n = len(arr)
#     for j in range(0, n - 1):
#         for i in range(0, n - 1 - j):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
#
# list_sort(arr)
# print(arr)
# #
# # import winsound  # 导入此模块实现声音播放功能
# # import time  # 导入此模块，获取当前时间
# #
# # # 提示用户设置时间和分钟
# # my_hour = input("请输入时：")
# # my_minute = input("请输入分：")
# # flag = 1
# # while flag:
# #     t = time.localtime()  # 当前时间的纪元值
# #     fmt = "%H %M"
# #     now = time.strftime(fmt, t)  # 将纪元值转化为包含时、分的字符串
# #     now = now.split(' ')  # 以空格切割，将时、分放入名为now的列表中
# #     hour = now[0]
# #     minute = now[1]
# #     if hour == my_hour and minute == my_minute:
# #         music = 'Good Time.wav'
# #         winsound.PlaySound(music, winsound.SND_ALIAS)
# #         flag = 0


# with open('a.txt', 'a', encoding='utf-8') as file:
#
#     file.write('1 test 100 2012-04-18'+'\n')
#     file.write('2 aaa 12 2012-04-19'+'\n')
#     file.write('3 bbb 333 2012-04-18'+'\n')
#     file.write('4 ccc 211 2012-04-17'+'\n')
#     file.write('5 ddd 334 2012-04-16'+'\n')


import codecs

f = codecs.open('a.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
line = f.readline()   # 以行的形式进行读取文件
list1 = []
while line:
    a = line.split()
    b = a[-1]   # 这是选取需要读取的位数
    list1.append(b)  # 将其添加在列表之中
    line = f.readline()
f.close()

for i in list1:
    print(i)
    print(i[-2:])

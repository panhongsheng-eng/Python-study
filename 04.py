"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
Version: 0.1
Author: 潘宏声
Date: 2021-10-11
"""

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
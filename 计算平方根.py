# 要求从控制台接收整数，计算平方根，打印输出。
# 输出占30个字符宽度，内容右对齐，剩余位置用“+”填充。
# 输出结果采用宽度30个字符、右对齐输出、多余字符采用加号(+)填充。
# 如果结果超过30个字符，则以结果宽度为准。

import math
num=int(input('请输入一个整数:'))
print('{:+>30.3f}'.format(math.sqrt(num)))
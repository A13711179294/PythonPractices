# 问题:编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8
# 则输出为:40320
# 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。
num=int(input('请输入一个数字:'))
sum=1
for i in range(1,num+1):
    sum=i*sum
print(sum)
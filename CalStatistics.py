#求解一组不定长数据的基本统计值，即平均值、标准差、中位数
from math import sqrt
def getnumber():#获取用户输入
    nums = []#列表可自由增删元素
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums
def mean(numbers):#计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)
def dev(numbers,mean):#计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2#x的y次幂
    return sqrt(sdev / (len(numbers) - 1))
def median(numbers):#计算中位数
    new = sorted (numbers) #对列表进行排序
    size = len(numbers)
    if size % 2 == 0:
        med = (new[size//2 - 1] + new[size//2])/2
    else:
        med = new[size//2]
    return med
n = getnumber()
m = mean(n)
print("平均值:{},标准差:{:.2},中位数:{}.".format(m,dev(n,m),median(n)))#参数序号：格式控制
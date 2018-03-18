"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
numbertime={}
timelist=[]
for number in calls:
    #进行字典录入如果字典中以存在的电话将其通话时间值进行相加并重新赋值 numbertime为以电话号码为key 以总通话时间为value的字典
    if number[0] in numbertime :
        numbertime[number[0]]+=int(number[3])
    else:
        numbertime[number[0]]=int(number[3])
    if number[1] in numbertime:
        numbertime[number[1]]+=int(number[3])
    else:
        numbertime[number[1]]=int(number[3])
#使用dict.items()以列表返回可遍历的(键, 值) 元组数组，使用sorted方法中的key对字典中的值即通话时间进行排序 返回列表为timelist 参考网址：http://www.runoob.com/python/python-func-sorted.html
timelist=sorted(numbertime.items(),key=lambda x:x[1],reverse=True)
#将结果进行输出   使用format函数进行格式化 参考网址：http://www.runoob.com/python/att-string-format.html
print ("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(timelist[0][0],timelist[0][1]))


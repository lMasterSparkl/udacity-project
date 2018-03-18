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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
#4个连续引号导致错误
sumnumber=[]
#将texts列表中的电话号码通过for循环进行筛选判断如果未在sumnumber列表中则进行添加（发送与接受号码都进行判断）之前用elif进行判断发现当条件一满足时会忽略条件二导致数据输出错误
for textnumber in texts:
    if textnumber[0] not in sumnumber:
        sumnumber.append(textnumber[0])
    if textnumber[1] not in sumnumber:
        sumnumber.append(textnumber[1])
#将calls列表中的电话号码通过for循环进行筛选判断如果未在sumnumber列表中则进行添加（拨打与接听号码都进行判断）
for callnumber in calls:
    if callnumber[0] not in sumnumber:
        sumnumber.append(callnumber[0])
    if callnumber[1] not in sumnumber:
        sumnumber.append(callnumber[1])
#将sumnumber列表进行统计与输出 参考网址：http://www.runoob.com/python/att-string-format.html
print ('There are {0} different telephone numbers in the records.'.format(len(sumnumber)))

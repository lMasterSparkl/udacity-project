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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
baselist=[]
#基础判断条件列表该列表中包括发出或接受过短信或者收到来电的电话号码并且没有重复项
lastlist=[]
#最终筛选出来的可以列表名单 在task3中说过140开头的为电话促销员号码 我觉得电话促销员也有可能使用非140开头的号码所以一并进行筛选
for number in texts:
    #用来判断发送和接受短信的号码是否存在于baselist列表中如果不存在则进行添加操作 可以同时进行baslist添加和去除重复号码的操作 注意不要使用elif进行判断
    if number[0] not in baselist:
        baselist.append(number[0])
    if number[1] not in baselist:
        baselist.append(number[0])
for phonenumber in calls:
    #该驯韩用来将接听号码并且不在baselist列表中的号码添加进baselist中
    if phonenumber[1] not in baselist:
        baselist.append(phonenumber[1])
for nodecide_phonenumber in calls:
    #对calls列表进行最终筛选 只有当拨打号码不在baselist中 并且同时不在lastlist列表中时才将其添加至lastlist列表中
    if (nodecide_phonenumber[0] not in baselist)and (nodecide_phonenumber[0] not in lastlist):
        lastlist.append(nodecide_phonenumber[0])
lastlist.sort()
#对lastlist列表进行排序 参考网址：http://www.runoob.com/python/att-list-sort.html
print("These numbers could be telemarketers: ")
#进行结果输出使用for循环遍历并输出lastlist列表中的每一项
for i in range(len(lastlist)):
    print (lastlist[i])

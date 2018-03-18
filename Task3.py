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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
baselist=[]
#由班加罗尔固话打往班加罗尔的电话列表baselist
lastlist=[]
#第一部分输出的区号及移动前缀列表
for phonenumber in calls:
    if phonenumber[0][0:5]=='(080)':
        #判断拨出电话号码即字典每一列表的第一个元素的前5个字符串是否为（080）如果是则将其添加至baselist列表中
        baselist.append(phonenumber[1])
for i in range (len(baselist)):
    if '('==baselist[i][0] and ((baselist[i][0:baselist[i].index(')')+1]) not in lastlist):
        #在baselist列表中只有当号码以'（'开始以'）'为结束并且该号码的区号不再lastlist列表中才将其添加入lastlist列表中 参考网址：http://www.runoob.com/python/att-list-index.html
        lastlist.append(baselist[i][0:baselist[i].index(')')+1])
    elif ' ' in baselist[i] and (baselist[i][0:4] not in lastlist) :
        #同理在baselist列表中只有当号码中间有‘ ’空格时并且号码前四位没有在lastlist列表中重复时才将其截取并添加入lastlist列表中
        lastlist.append(baselist[i][0:4])
'''    elif '140'==baselist[i][0:3]: #该代码用来判断是否为140开头的促销员号码但是查看结果后发现没有人给140开头的电话打过去故将其注释起来备用
        print (baselist[i])'''

lastlist.sort()
#将lastlist列表进行排序 参考网址：http://www.runoob.com/python/att-list-sort.html
print("The numbers called by people in Bangalore have codes:")
#输出结果使用for循环进行遍历输出
for i in range(len(lastlist)):
    print (lastlist[i])
#第二部分实现代码
a=len(baselist)
b=0 #b为统计由班加罗尔固话打往班加罗尔的电话数量
#使用for循环对baselist（而不是lastlist）进行判断如果同样为（080）开始的号码则对b进行+1处理
for i in range(a):
    if baselist[i][0:5]=='(080)':
        b+=1
#输出结果使用format函数进行百分数的格式化和比例的计算 参考网址：http://www.runoob.com/python/att-string-format.html
print ("{:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(b/a))

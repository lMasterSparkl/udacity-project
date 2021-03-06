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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
#输出短信记录第一条也就是texts列表第一个元素中的三个内容使用format进行格式化 参考网址：http://www.runoob.com/python/att-string-format.html
print('First record of texts, {0} texts {1} at time {2}'.format(texts[0][0],texts[0][1],texts[0][2]))
#输出通话记录第一条也就是calls列表第一个元素中的四个内容使用format进行格式化
print('Last record of calls,{0} calls {1} at time {2}, lasting {3} seconds'.format(calls[-1][0],calls[-1][1],calls[-1][2],calls[-1][3]))

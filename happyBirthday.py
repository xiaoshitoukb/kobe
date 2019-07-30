'''cdays-4-exercise-6.py 文件基本操作
    @note: 文件读取写入, 列表排序, 字符串操作
    @see: 字符串各方法可参考hekp(str)或Python在线文档http://docs.python.org/lib/string-methods.html
'''
# 以读方式打开文件
f = open('/Users/qitmac000483/Desktop/python_script/data/date.txt', 'r')
result = list()
# 依次读取每行
for line in f.readlines():
    # 去掉每行头尾空白
    line = line.strip()
    # 判断是否是空行或注释行
    if not len(line) or line.startswith('#'):
        # 是的话，跳过不处理
        continue
    # 保存
    result.append(line)
# 排序结果
result.sort()
print(result)

open(
    '/Users/qitmac000483/Desktop/python_script/data/date1.txt',
    'w').write(
        '%s' %
    '\n'.join(result))  # 保存入结果文件

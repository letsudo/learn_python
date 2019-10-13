# coding=utf-8
# 变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。
# 基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。

# 变量赋值
print "\n"
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
print counter
print miles
print name


# 多个变量赋值
print "\n"
# a = b = c = 1
a, b, c = 1, 2, "john"
print a,b,c



# 标准数据类型
    # Numbers（数字）
    # String（字符串）
    # List（列表）
    # Tuple（元组）
    # Dictionary（字典）





# Python数字
    # int（有符号整型）
    # long（长整型[也可以代表八进制和十六进制]）
    # float（浮点型）
    # complex（复数）

# Python字符串
print "\n"
s="a1a2···an"
print s

# python的字串列表有2种取值顺序:
    # 从左到右索引默认0开始的，最大范围是字符串长度少1
    # 从右到左索引默认-1开始的，最大范围是字符串开头

# [头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。
s = '1234567890'
print s[1:5]
print s[1:-1]
print s[1:]
print s[1::2]#Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 结尾 的位置并设置为步长为 2（间隔一个位置）来截取字

str = 'Hello World!'
print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第六个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串




# Python列表
    # 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
    # 列表用 [ ] 标识，是 python 最通用的复合数据类型。
    # 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
print "\n"
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表



# Python 元组
# 元组是另一个数据类型，类似于 List（列表）。
# 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
print "\n"
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第四个（不包含）的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组
print "\n"
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用
print tuple, list



# Python 字典
print "\n"
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值




# Python数据类型转换

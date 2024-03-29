# coding=utf-8
# Python语言支持以下类型的运算符:
#
    # 算术运算符
    # 比较（关系）运算符
    # 赋值运算符
    # 逻辑运算符
    # 位运算符
    # 成员运算符
    # 身份运算符
    # 运算符优先级



# Python算术运算符
a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c

c = a * b
print "3 - c 的值为：", c

c = a / b
print "4 - c 的值为：", c

c = a % b
print "5 - c 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print "6 - c 的值为：", c

a = 14
b = 5
c = a // b
print "7 - c 的值为：", c
# Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可。




# Python比较运算符

a = 21
b = 10
c = 0
print ("\n")
if a == b:
    print "1 - a 等于 b"
else:
    print "1 - a 不等于 b"

if a != b:
    print "2 - a 不等于 b"
else:
    print "2 - a 等于 b"

if a <> b:
    print "3 - a 不等于 b"
else:
    print "3 - a 等于 b"

if a < b:
    print "4 - a 小于 b"
else:
    print "4 - a 大于等于 b"

if a > b:
    print "5 - a 大于 b"
else:
    print "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print "6 - a 小于等于 b"
else:
    print "6 - a 大于  b"

if b >= a:
    print "7 - b 大于等于 a"
else:
    print "7 - b 小于 a"




print ('\n')
a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c

c *= a
print "3 - c 的值为：", c

c /= a
print "4 - c 的值为：", c

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c



print ('\n')
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print "1 - c 的值为：", c

c = a | b;  # 61 = 0011 1101
print "2 - c 的值为：", c

c = a ^ b;  # 49 = 0011 0001
print "3 - c 的值为：", c

c = ~a;  # -61 = 1100 0011
print "4 - c 的值为：", c

c = a << 2;  # 240 = 1111 0000  #左移1位相当于*2
print "5 - c 的值为：", c

c = a >> 2;  # 15 = 0000 1111
print "6 - c 的值为：", c


print ('\n')
a = 10
b = 20

if a and b:
    print "1 - 变量 a 和 b 都为 true"
else:
    print "1 - 变量 a 和 b 有一个不为 true"

if a or b:
    print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "2 - 变量 a 和 b 都不为 true"

# 修改变量 a 的值
a = 0
if a and b:
    print "3 - 变量 a 和 b 都为 true"
else:
    print "3 - 变量 a 和 b 有一个不为 true"

if a or b:
    print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "4 - 变量 a 和 b 都不为 true"

if not (a and b):
    print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
    print "5 - 变量 a 和 b 都为 true"


# Python成员运算符
print ('\n')
a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"

if (b not in list):
    print "2 - 变量 b 不在给定的列表中 list 中"
else:
    print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if (a in list):
    print "3 - 变量 a 在给定的列表中 list 中"
else:
    print "3 - 变量 a 不在给定的列表中 list 中"


# Python身份运算符
# 身份运算符用于比较两个对象的存储单元
print ("\n")
a = 20
b = 20

if (a is b):
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if (a is not b):
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"

# 修改变量 b 的值
b = 30
if (a is b):
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"

if (a is not b):
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。
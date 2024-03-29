# coding=utf-8
# 循环类型	描述
# while 循环	在给定的判断条件为 true 时执行循环体，否则退出循环体。
# for 循环	重复执行语句
# 嵌套循环	你可以在while循环体中嵌套for循环

# break 语句	在语句块执行过程中终止循环，并且跳出整个循环
# continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
# pass 语句	pass是空语句，是为了保持程序结构的完整性。

count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1

print "Good bye!"

print ('\n')
# continue 和 break 用法

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

# var = 1
# while var == 1:  # 该条件永远为true，循环将无限执行下去
#     num = raw_input("Enter a number  :")
#     print "You entered: ", num
#
# print "Good bye!"


#
# print ('\n')
# count = 0
# while count < 5:
#    print count, " is  less than 5"
#    count = count + 1
# else:
#    print count, " is not less than 5"
#
#
#
# flag = 1
#
# while (flag): print 'Given flag is really true!'

# print "Good bye!"



for letter in 'Python':  # 第一个实例
    print '当前字母 :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print '当前水果 :', fruit

print "Good bye!"

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果 :', fruits[index]

print "Good bye!"




for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'
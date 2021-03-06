'''
循环的分类
1.while循环
2.for循环
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
while循环语法结构：
while 条件表达式：
    代码
语法特点：
1.有初始值
2.条件表达式
3.变量【循环体内计数变量】的自增自减，否则会造成死循环
使用条件：循环的次数不确定，依靠循环条件来结束
目的：为了将相似或者相同的代码变得更加简洁，使得代码可以重复利用
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for循环
语法特点：遍历操作，依次取集合容器中的每个值
循环格式：
for 临时变量 in 字符串，列表等：
    执行代码块
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
循环和else语句的搭配使用：
for 变量 in 遍历对象：
    执行代码块
else:
    循环体退出时执行的代码
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
# i = 1
# str = 'hello,python'
# for i in str:
#     print(i, end='')
#     pass
# print('\n')
# li = ['a','b','c','d']
# for i in li:
#     print(i, end=' ')

# range 此函数可以生成一个数据集合列表
# range(起始：结束：步长)  步长不能为0，不加步长默认步长为1，数据为左闭右开，即右边不包含

# 案例一，求1~100的累加和
# sum = 0
# for data in range(1,101):
#     sum += data
#     print(data,end=' ')
#     pass
# print('\n')
# print('sum=%d'%sum)

# 案例二，输出20~101之间的偶数
# for data in range(20,102):
#     if data % 2 == 0:
#         print('%d是偶数'%data, end=' ')
#         pass
#     else:
#         print('%d是奇数'%data)

'''
 案例三，限定用户登陆的次数，一旦三次没有登录成功就提示用户已被锁定
 思路：  用for循环控制尝试登陆的次数，执行完整个for循环没有登录成功则锁定账户
 所采用的结构：
 for 变量 in 遍历对象：
    执行代码块
 else:
    循环执行结束后,要执行的内容
'''
usr = 'haha'
pwd = '123'
for i in range(3):
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if usr == username and pwd == password:
        print('欢迎%s'%usr)
        break  # 用户名和密码都正确跳出循环，登陆成功
        pass
    pass
else:   # 如果三次没有登录成功，锁定账户。只要循环语句中break语句没有执行，else就会执行
    print('该账户已被锁定')
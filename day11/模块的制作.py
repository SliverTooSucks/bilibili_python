'''
什么是模块？
python文件都可以作为一个模块，模块的名字就是文件的名字。

模块的作用：
可以使我们有逻辑的组织python代码，以库的形式去封装功能，非常方便的让调用者使用
可以定义函数  类  变量， 也能包含可执行的代码

注意：不同的模块可以定义相同的变量名，但是每个模块中的变量名作用域只是在本模块中

模块的分类：
内置模块------python自带的模块
自定义模块----自己写的模块
第三方模块----他人写的模块

模块的原理：打开python文件，执行模块中的方法

细节：使用from 模块名 import * 时，配合魔术变量 __all__(写在模块中)使用
可以控制哪些方法可以调用，哪些不可以
'''
# 调用自己写的test.py，即使用test模块
# 方式一，导入整个模块
# import test
# 方式二，form关键字导入模块中的具体方法
# from test import add
# from test import subtract
# 方式三，from关键字导入所有

# 调用模块中的add()方法
# result = test.add(1, 2)
# print(result)
# # 调用模块中的subtract()方法
# print(test.subtract(10, 2))
# # 调用模块中的乘法
# test
# print(test.mult(2, 3))



'''
调用模块时，如果模块中有测试代码，则模块中的测试代码也会执行。
为了避免模块中的测试代码执行的这种情况，需要借助魔术变量，在模块中加入如下代码：
if __name__=='__main__':
    执行代码
'''
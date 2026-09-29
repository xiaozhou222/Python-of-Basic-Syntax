# -------------------print输出函数---------------------
"""
print(*values,sep=" ",end="\n",file=None,flush=False)  ##valus值  sep分隔符   end结尾转义字符   file写入文件
"""

# ----写入文件操作----
# 方法一：
f = open("zzz.txt","w")         ## w覆盖写入  a追加写入
print("hello world",file=f)
f.close()

# 方法二：
with open('zzz.txt','a') as f:
	print("hello world",file=f)

# ----格式化输出----
""" %c  字符        %s  字符串        %d  十进制整数          %f  浮点数"""

# 方法一：
print('名字：%s,年龄：%d,身高：%.2f' % ('小明',18,1.75))

# 方法二：
print('名字：{},年龄：{},身高：{:.2f}'.format('小明',18,1.75))

# 方法三（最常用）：
name,age,height = '小明',18,1.75
print(f'名字：{name},年龄：{age},身高：{height:.2f}') ## f是f-string格式化字符串​的标记，作用是让{}里的变量或表达式被求值并替换成实际内容

# --------------------input输入函数--------------------
user_input = input("请输入您的姓名：")
print(f"您输入的姓名是：{user_input}")
print(type(user_input))             ## input输入的内容都是字符串类型

# --------------------变量的命名-----------------------
"""变量名只能包含字母、数字和下划线，且不能以数字开头"""
a = 1
print(a)

import keyword
print(keyword.kwlist)  ##  查看python关键字，关键字不能作为变量名

# --------------------六大数据类型-----------------------
# 1. 数字类型（int, float, complex）
"""
boolean类型（bool）是数字类型的子类，True和False分别对应1和0
complex类型是复数类型a+bj，实部和虚部都是浮点数，虚部用j表示
"""
#-------运算操作-------
round(3.14159,2)    ##四舍五入，保留两位小数
a,b = 10,3
f = a/b             ##除（含小数位）
f = a//b            ##整除（不含小数位）
f = a%b             ##取余
f = a*b
f = a**b            ##幂运算 10的3次方
f = int('10')       ##强制类型转换 字符串转整数
f = 1e3             ##科学计数法表示 1*10^3

# 2. 字符串类型（str）
"""字符串是由字符组成的序列，可以使用单引号、双引号或三引号来定义字符串"""
str1 = 'hello'
str2 = "world"
str3 = '''This is a multi-line string.'''
print(str1,str2,str3)
print(type(str1),type(str2),type(str3))
str1[0]                 ##索引访问字符串中的字符，索引从0开始

#--------切片操作--------
"""通过索引来访问字符串中的子串，语法为：字符串[起始索引:结束索引:步长]，其中起始索引默认为0，结束索引默认为字符串长度，步长默认为1"""
str1 = 'hello world'
print(str1[::])         ##输出hello world
print(str1[:])          ##输出hello world
print(str1[0:5])        ##输出hello
print(str1[:5])         ##输出hello
print(str1[6:11])       ##输出world
print(str1[6:])         ##输出world
print(str1[::2])        ##输出hlool，步长为2，表示每隔一个字符取一个字符
print(str1[-1])         ##输出d，负数索引表示从字符串末尾开始计数，-1表示最后一个字符，-2表示倒数第二个字符，以此类推
print(str1[::-1])       ##输出dlrow olleh，步长为-1，表示反向取字符
print(str1[:-1])        ##输出hello worl，切片操作，取字符串中除最后一个字符外的所有字符
print(str1[-10::-1])    ##输出dlrow olleh
print(str1[1:9:1])      ##输出ello wor，步长为1，表示从索引1开始取到索引8的字符

#------三引号可作注释------
""" 
aaa  123   hhh
这是一个多行注释
可以写很多行
"""
# 3. 列表类型（list）
"""列表是有序的可变集合，可以包含任意类型的元素，使用方括号 [] 定义，元素之间用逗号分隔"""
list1 = [1,"hello",3.14,[4,5]]
print(list1)
print(type(list1))
print(list1[0])     ##索引访问列表中的元素，索引从0开始
print(list1[1])     ##输出hello
print(list1[1::2])  ##输出['hello', [4, 5]]，步长为2，表示每隔一个元素取一个元素
print(list1[:-1])   ##输出[1, 'hello', 3.14]，切片操作，取列表中除最后一个元素外的所有元素

a = [1,2,3]
b = [4,5,6]
c = a + b           ##列表拼接
print(c)            ##输出[1, 2, 3, 4, 5, 6]

a = list(range(1,11))   ##生成一个包含1到10的列表
print(a)                ##输出[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(a))           ##输出列表的长度，即元素个数
print(max(a))           ##输出列表中的最大值
print(min(a))           ##输出列表中的最小值
print(sum(a))           ##输出列表中所有元素的和
a.sort()                ##对列表进行升序排序
print(a)                ##输出[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.sort(reverse=True)    ##对列表进行降序排序
print(a)                ##输出[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

a =[1,2,3] 
a.append(11)        ##在列表末尾添加一个元素
print(a)            ##输出[1, 2, 3, 11]
a.extend([12,13])   ##在列表末尾添加多个元素
print(a)            ##输出[1, 2, 3, 11, 12, 13]
a.remove(2)         ##删除列表中第一个出现的指定元素
print(a)            ##输出[1, 3, 11, 12, 13]
a.pop(0)            ##删除列表中指定索引的元素，默认删除最后一个元素
print(a)            ##输出[3, 11, 12, 13]
a[0] = 100          ##修改列表中指定索引的元素
print(a)            ##输出[100, 11, 12, 13]
a[:]                ##查看列表中所有元素
a[:] = [1,2,3]      ##修改列表中指定索引的元素
print(a)            ##输出[1, 2, 3]

# 4. 元组类型（tuple）
"""元组是有序的不可变集合，即元素不能修改，使用圆括号()定义，元素之间用逗号分隔"""
tuple1 = (1, "hello", 3.14)
print(tuple1)
print(type(tuple1))
print(tuple1[0])            ##索引访问元组中的元素，索引从0开始
print(tuple1[-1])           ##输出3.14，负数索引表示从元组末尾开始计数，-1表示最后一个元素，-2表示倒数第二个元素，以此类推
print(tuple1[1::2])         ##输出('hello', 3.14)，步长为2，表示每隔一个元素取一个元素

tuple2 = (1, )              ##创建一个包含一个元素的元组,结尾处需加上逗号，否则会被认为是一个普通的括号表达式

tuple3 = (1, 2, 2, 1, 3)
print(tuple3.count(2))      ##统计元组中指定元素出现的次数
print(tuple3.index(3))      ##返回元组中指定元素第一次出现的索引位置
print(tuple3[:-1])          ##输出(1, 2, 2, 1)，切片操作，取元组中除最后一个元素外的所有元素
print(tuple3[::-1])         ##输出(3, 1, 2, 2, 1)，步长为-1，表示反向取元素
tuple4 = tuple3 + (4, 5)    ##元组拼接

# 5. 集合类型（set）
"""集合是无序的可变集合，不包含重复元素，元素唯一，使用花括号{}定义"""
set1 = {1, 2, 3, 4, 5}
print(set1)
print(type(set1))
set1.add(6)                         ##向集合中添加一个元素
print(set1)                         ##输出{1, 2, 3, 4, 5, 6}
set1.remove(2)                      ##删除集合中的指定元素
print(set1)                         ##输出{1, 3, 4, 5, 6}
del set1                            ##删除整个集合

myset1 = set([1, 2, 3, 4, 5])       ##创建一个集合，去除重复元素

empty_set = set()                   ##创建一个空集合，不能使用{}，因为{}表示空字典
empty_dict = {}                     ##创建一个空字典

set2 = {1,1,2,3,4,5,3,2}            ##集合中不允许重复元素，重复的元素会被自动去除
print(set2)                         ##输出{1, 2, 3, 4, 5}

set3 = set1 & set2                  ##集合的交集
set4 = set1 | set2                  ##集合的并集
print(set3)                         ##输出{1, 2, 3, 4, 5}
print(set4)                         ##输出{1, 2, 3, 4, 5, 6}

# 6. 字典类型（dict）
"""字典是无序的可变集合，由键值对组成，使用花括号{}定义，其中键值对之间用:分隔，键必须是唯一的，值可以是任意类型"""
dict1 = {"name": "Alice", "age": 25, "city": "Beijing"}
print(dict1)
print(type(dict1))

keys = dict1.keys()         ##获取字典中的所有键
values = dict1.values()     ##获取字典中的所有值
print(keys)                 ##输出dict_keys(['name', 'age', 'city'])
print(values)               ##输出dict_values(['Alice', 25, 'Beijing'])

print(dict1["name"])        ##通过键访问字典中的值
dict1["age"] = 26           ##修改字典中指定键的值
print(dict1)                ##输出{'name': 'Alice', 'age': 26, 'city': 'Beijing'}
dict1["job"] = "Engineer"   ##向字典中添加新的键值对
print(dict1)                ##输出{'name': 'Alice', 'age': 26, 'city': 'Beijing', 'job': 'Engineer'}
del dict1["city"]           ##删除字典中的指定键值对
print(dict1)                ##输出{'name': 'Alice', 'age': 26, 'job': 'Engineer'}

# --------------------三大程序结构-----------------------
#1. 顺序结构：按照代码的书写顺序依次执行
#2. 分支结构：根据条件的不同执行不同的代码块，常用的分支结构有if语句和if-else语句
#方法一：
a = 1
if a > 0:
    print("a是正数")    
elif a < 0:
    print("a是负数")
else:
    print("a是零")
#方法二：
if a>=0:
    if a>0:
        print("a是正数")
    else:
        print("a是零")
else:
    print("a是负数")

#3. 循环结构：重复执行某段代码，直到满足某个条件为止，常用的循环结构有for循环和while循环
#while循环：
i = 0
while i < 5:
    print(i)
    i += 1
#for循环：
for i in range(5):
    print(i)

# --------------------函数-----------------------
"""
def 函数名(参数):
    函数体
    return 返回值
"""
def add(a, b):
    result = a + b
    return result

#-----调用函数-----
sum = add(3, 5)
print(sum)

fun = lambda x, y: x + y  ##匿名函数，lambda关键字定义，冒号前是参数，冒号后是表达式
result = fun(3, 5)
print(result)

#-----递归函数-----
"""递归是指函数在定义中调用自身，递归函数必须有一个终止条件，否则会导致无限递归，最终引发栈溢出错误"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# --------------------类和对象-----------------------
#-----自定义类-----
class Person:
    def __init__(self, name, age):  ##实例方法
        self.name = name
        self.age = age

    def introduce(self):
        print(f"大家好，我叫{self.name}，今年{self.age}岁。")

    """类方法不能调用实例属性和实例方法，只能访问类属性和类方法，通常用于定义与类相关的操作，而不是与具体实例相关的操作"""
    @classmethod                    ##装饰器
    def class_method(cls):
        print("这是一个类方法")

    """静态方法没有访问类属性和实例属性的能力，通常用于定义与类相关的操作，但不需要访问类属性和实例属性，是类中独立的函数"""
    @staticmethod
    def sub(a,b):
        result = a-b
        return result
    pass                            ##pass语句是空语句，表示什么都不做，一般用作占位符

#-----创建对象-----
person1 = Person("小明", 18)
person1.introduce()                 ##调用对象的方法
print(person1.name)                 ##访问对象的属性
print(person1.sub(10,5))            ##调用静态方法
person1.class_method()              ##调用类方法

person2 = Person("小红", 20)
person3 = Person("小刚", 22)
list_person = [person1, person2, person3]
for person in list_person:
    person.introduce()              ##调用对象的方法


# --------------------面向对象-----------------------
#-----继承-----
class Student(Person):               ##Student类继承Person类
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  ##调用父类的构造方法
        self.student_id = student_id

    def introduce(self):
        print(f"大家好，我叫{self.name}，今年{self.age}岁，我的学号是{self.student_id}。")

#-----多态-----
def introduce_person(person):       
    person.introduce()              ##调用对象的方法，不同的对象会有不同的实现

#-----封装-----
"""
访问限制：
在Python中,访问限制是通过在属性或方法名前加上一个或两个下划线来实现的。
单下划线开头表示该属性或方法是受保护的,双下划线开头表示该属性或方法是私有的,外部无法直接访问,只能在类的内部访问。
双下划线开头和结尾的属性或方法是特殊方法,通常用于实现类的特定行为,如__init__()是构造方法,__str__()是字符串表示方法等。
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  ##私有属性，外部无法直接访问
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存款成功，当前余额为{self.__balance}元。")
        else:
            print("存款金额必须大于0。")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"取款成功，当前余额为{self.__balance}元。")
        else:
            print("取款金额不合法或余额不足。")

    def get_balance(self):
        return self.__balance
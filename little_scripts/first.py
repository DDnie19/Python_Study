#python两大特性和四大基本语法
#python语言可以进行GUI开发、web开发、数据的预处理。
#python是一个动态的 强类型语言
#动态语言  类型检查是验证类型约束的过程，编译器或者解释器通常在编译阶段或运行阶段做类型检查。
#类型检查是查看变量和变量的类型，然后判断表达式是否合理。
#例子：
#类型不同不能够进行逻辑运算。
#类型检查发生在程序运行阶段就是动态语言。
#例如：python javascript php
#类型检查发生在编译阶段为“静态类型语言”，常见如：C C++ JAVA C#
#强类型语言：不管在编译还是运行阶段，一旦某种类型绑定到变量后，此变量便会持有此类型，并且不能同
#其它类型在计算表达式是混合使用。
#支持强类型的语言有：python JAVA C# Scala
a = '123'
b = 456
print (int(a)+b)
print (type(a))
print (type(b))
print (id(a))
print (id(b))
#四大基本语法
#命名规则 缩进原则 特殊关键字 特殊运算符
#命名规则：python变量命名规则 允许使用英文 数字 下划线，不能以数字开头。 区分大小写。
#以下划线开头的变量具有特殊意义，类变量以单下划线开头，表示不能被直接访问，不能通过”import”导入
#类变量以双下划线开头表示为类的私有成员，不能被导入和其他类变量访问。
#以下划线开头和双下划线结尾是python中的专有标识，有特殊的身份意义。
#python变量命名遵守蛇形命名（snake case）
#类名首字符大写，特殊变量全部大写。例如：person_name;person_age;方法 get_person_name()
#python的缩进原则，为4个字符，通过层级结构，展现代码的逻辑层次。
class Person(object):
    def __init__(self,person_name,person_age):
        self.name = person_name
        self.age = person_age
        Person.name = person_name
    #def __out__(self,pepole):
    #    return  person_name is person_age

tom = Person('ada',18)
#ada = Person('ada',19)
print (tom.name)
#print (type(tom))
#print (ada)
class Book(object):
    def __init__(self,book_id,book_name,book_count):
        self.book_id = book_id
        self.book_nme = book_name
        self.book_count = book_count
        Book.name = book_name
    #def __add__(self,book):
    #    return self.book_count + book.book_count
a_book = Book(1,'abook',10)
b_book = Book(2,'bbook',20)
c_book = Book(3,'cbook',20)
#print(a_book + b_book)
print (type(a_book.name))
print (id(a_book),id(b_book),id(c_book))
print (id(a_book.name),id(b_book.name),id(c_book.name))
print("a_book's name is" + "  " + a_book.name)
print("b_book's name is" + "  " + b_book.name)
#第一个疑问，我擦为什么内存地址空间是一样的，每个变量传入的属性应该出现自己传入的名字，我R。

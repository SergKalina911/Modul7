"""                                     Автопрверка

                        Теория к авточек 1

Это __init__наиболее часто используемый магический метод. Этот метод отвечает за инициализацию объекта. 
При создании объекта класса сначала создаётся пустой объект, содержащий только необходимые атрибуты сервиса. 
После этого (когда объект уже создан) метод __init__вызывается автоматически. Вы можете изменить его в 
соответствии со своими потребностями.

class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello! I am {self.name}'


bill = Human('Bill')
print(bill.say_hello())  # Hello! I am Bill
print(bill.age)  # 0

jill = Human('Jill', 20)
print(jill.say_hello())  # Hello! I am Jill
print(jill.age)  # 20

В этом примере мы создали Humanкласс, в котором определили __init__ метод. В этом методе мы добавляем поля name 
и age к объектам этого класса. Обратите внимание, что __init__метод может принимать позиционные и/или номинальные 
аргументы, как и любой другой метод. При создании объекта класса Humanмы должны передать классу хотя бы один аргумент, 
поскольку __init__метод всегда должен принимать name.

Метод __init__не обязательно принимает аргументы и только создаёт поля. Этот метод можно использовать для выполнения 
любых необходимых действий на этапе, когда объект уже создан и требует инициализации.

1. Создайте класс Point, который будет отвечать за отображение геометрической точки на плоскости.

Реализовать инициализацию двух атрибутов через __init__конструктор: x и y координат.

Пример:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10"""
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

point = Point(5, 10)
print(point.x)  # 5
print(point.y)  # 10

"""                     Теория к авточек 2 

В Python невозможно инкапсулировать (сделать недоступными) атрибуты класса. Вы всегда можете получить доступ к любому 
атрибуту. Если вы хотите дать разработчику понять, что доступ к атрибуту нежелателен, принято называть такие поля или 
методы, начиная с одного нижнего подчеркивания. Если же имя атрибута начинается с двух нижних подчеркиваний, 
активируется механизм «скрытия» имён. Это не означает, что доступ к этому полю будет закрыт, просто это немного 
сложнее."""
class Secret:
    public_field = 'this is public'
    _private_field = 'avoid using this please'
    __real_secret = 'I am hidden'


s = Secret()
print(s.public_field)  # this is public
print(s._private_field)  # avoid using this please
print(s._Secret__real_secret)  # I am hidden

""" Как видно из этого примера, доступа к нет s.__real_secret, но к тому же полю можно получить доступ через 
s._Secret__real_secret, что, как правило, ничего не защищает.

Этот механизм можно использовать для реализации функциональности сеттера и геттера. Иногда возникает необходимость 
проверить, что пользователь хочет записать в поле. Для этого можно написать отдельный метод для проверки значения в 
поле перед сохранением. При этом само поле останется доступным. Также можно использовать setter декоратор. Кроме того, 
декоратор можно использовать property для вычисления значения сразу или в паре с setter, что превращает любой метод в 
поле. Например, мы хотим проверить, что пользователь вводит только положительные числа."""

class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Only numbers greater zero accepted')


p = PositiveNumber()
p.value = 1
print(p.value)  # 1
p.value = -1  # Only numbers greater zero accepted
p._PositiveNumber__value = -1
print(p.value)  # -1
"""
В этом примере __value поле можно считать скрытым. Оно инкапсулировано. Однако значение этого поля можно получить и 
изменить напрямую. property Декоратор также полезен, когда значение поля необходимо вычислить во время запроса.

2. In the Point class, two attributes are declared through the __init__ constructor: x and y coordinates. You can 
hide access to them with a double underscore: __x and __y.

Implement the setter and getter mechanisms for the Point class for the __x and __y attributes using the property 
and setter decorators.

Example:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10 """
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        self.__x=new_x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        self.__y=new_y

point = Point(5, 10)
print(point.x)  # 5
print(point.y)  # 10

"""                                     Автопроверка 3 

                        Теория к авточек 3
                        
Рассмотрим следующую ситуацию: у нас есть Person класс, обладающий name свойством."""

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (len(name) > 0):
            self.__name = name


person = Person(123)
print(person.name)  # 123

""" В этом коде может быть ошибка. В setter мы проверяем, является ли значение строкой, и ожидаем только строку ненулевой 
длины. Однако при инициализации значения в конструкторе, когда мы присваиваем self.__name=name, мы фактически 
игнорируем setter и присваиваем значение напрямую. Именно это и произошло в нашем коде — __name свойство содержит 
числовое значение.

Чтобы этого не произошло, необходимо переписать код следующим образом:"""

class Person:
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (len(name) > 0):
            self.__name = name


person = Person(123)
print(person.name)  # None

""" Теперь в конструкторе мы присваиваем значение None полю  __name: self.__name=None. Во второй строке конструктора 
мы вызываем оператор setterс self.name=name оператором . В этом случае setter выполняется оператор , который 
предотвращает присвоение недопустимого значения 123 полю __name при создании экземпляра класса person = Person(123).

3. В Pointк лассе добавьте проверку введённого значения в setter механизм свойств x и y. Разрешите устанавливать 
свойства x и y для экземпляра класса только в том случае, если они имеют числовое значение (int или float).

Пример:

point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10"""
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x
        else:
            print('Only numbers accepted')
        
            

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y
        else:
            print('Only numbers accepted')
point = Point("a", 10)
print(point.x)  # None
print(point.y)  # 10


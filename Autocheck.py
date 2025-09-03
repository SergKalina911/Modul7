"""                                     Автопрверка 1

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

"""                                     Автопроверка 2

                        Теория к авточек 2 

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

"""                                     Автопроверка 4 
                        
                        Теория к авточек 4
                        
Квадратные скобки позволяют ссылаться на элементы индексной последовательности или словаря по ключу. Когда требуется 
получить значение с помощью квадратных скобок, __getitem__ вызывается метод . Чтобы записать значение с индексом или 
ключом, вызовите __setitem__ метод .

Оба этих метода принимают self в качестве первого аргумента.  __getitem__ В качестве второго аргумента принимает 
индекс или ключ, по которому ищется элемент, а __setitem__ в качестве второго аргумента — ключ/индекс, а в качестве 
третьего — значение, которое нужно записать по этому ключу/индексу. """

class ListedValuesDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __getitem__(self, key):
        result = str(self.data[key][0])
        for value in self.data[key][1:]:
            result += ", " + str(value)
        return result


l_dict = ListedValuesDict()
l_dict[1] = 'a'
l_dict[1] = 'b'
print(l_dict[1])  # a, b

""" В этом примере мы создали пользовательский класс, который ведёт себя как словарь. Класс A ListedValuesDict 
сохраняет значения в списке и сохраняет этот список как ключевое значение. Главное отличие от словаря заключается 
в том, что он ListedValuesDict не позволяет перезаписывать значения. Он всегда добавляет новое значение в конец 
списка. При получении значения он возвращает строку, состоящую из значений из списка.                        


4. Implement the Vector class. The coordinates property defines the coordinates of the vector and is an instance 
of the Point class. As you know, a vector is a directed segment with a beginning and an end. The beginning will 
be at the point (0, 0), and the end of the vector will be set by the coordinates attribute.

Implement the ability to access the coordinates of an instance of the Vector class through square brackets:

vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Set the x coordinate of the vector to 10

print(vector[0])  # 10
print(vector[1])  # 10

To get a value using the square brackets of the print(vector[0]) object, you have to implement the
__getitem__ method of the Vector class.

To store the value of a vector's coordinates using an index, like vector[0] = 10, implement the method 
__setitem__ in the Vector class.

The x coordinate is accessed at index 0, and the y coordinate is accessed at index 1."""
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

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates
        

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            return None
        return None
    
            
    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            return None
        return None
    
vector = Vector(Point(1, 10))
print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10
vector[0] = 10  # Set the x coordinate of the vector to 10
print(vector[0])  # 10
print(vector[1])  # 10

"""                                  Автопроверка 5
                        
                        Теория к авточек 5
                        
Если вы хотите увидеть содержимое объекта в интерактивном режиме Python, вы можете просто ввести его имя в консоль, 
и интерпретатор отобразит вид объекта в строке.

l = [1, 2]
l
Вы увидите  [1, 2]в консоли.

__repr__ За механизм внутреннего чтения объектов отвечает магический метод. Этот метод принимает только один 
аргумент ( self конечно же,) и должен возвращать строку.

Если вы хотите вывести полезную информацию в случаях, когда программа должна отображать объект, вы можете 
модифицировать этот метод. Например, класс точки на плоскости в декартовых координатах:"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x}, {self.y})'

a = Point(1, 9)
print(a)

""" Запустите этот код в консоли Python, и вы увидите Point(1, 9).

Очень похожий метод, отвечающий за преобразование объекта в строку, — это __str__ метод . Когда вы вызываете
str функцию и передаёте ей объект, этот объект фактически вызывается методом __str__."""

class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Hello! I am {self.name}'

bill = Human('Bill')
bill_str = str(bill)
print(bill_str)  # Hello! I am Bill              

""" 5. Implement the __str__ magic method for the Point and Vector classes. For the Point class, the method must 
return a string of the form Point(x,y), and for the Vector class - the string Vector(x,y), as in the example below 
(instead of x/y, you must substitute the coordinates of the class instance):

point = Point(1, 10)
vector = Vector(point)

print(point)  # Point(1,10)
print(vector)  # Vector(1,10) """

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

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f'Point({self.x},{self.y})'

class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __str__(self):
        return f'Vector({self.coordinates.x},{self.coordinates.y})'
          

point = Point(1, 10)
vector = Vector(point)
print(point)  # Point(1,10)
print(vector)  # Vector(1,10)

"""                                     Автопроверка 6
                        
                        Теория к авточек 6 

Функторы — это объекты, которые ведут себя как функции в том смысле, что их можно вызывать и передавать им 
аргументы. Функция в Python — это тот же объект, но реализующий __call__ метод, который отвечает за синтаксис 
вызова в скобках."""
class Adder:
    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, value):
        return self.add_value + value


two_adder = Adder(2)
print(two_adder(5))  # 7
print(two_adder(4))  # 6

three_adder = Adder(3)
print(three_adder(5))  # 8
print(three_adder(4))  # 7

""" В этом примере мы создали Adderкласс с методом __call__. Теперь объекты этого класса можно вызывать как функции, 
передавая им аргументы. Эти вызовы будут вызывать __call__метод для объектов класса Adder.


6. Вам необходимо реализовать функтор для экземпляра класса Vector. Создайте __call__ метод для Vector класса. 
Он должен реализовывать следующее поведение:

vector = Vector(Point(1, 10))

print(vector())  # (1, 10)

При вызове экземпляра класса как функции он возвращает кортеж с координатами вектора.

Если при вызове мы передаем параметр числа, то выполняем произведение вектора на число: умножаем каждую координату 
на указанное число и возвращаем кортеж с новыми координатами вектора.

vector = Vector(Point(1, 10))

print(vector(5))  # (5, 50)"""
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

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value is None:
            return (self.coordinates.x, self.coordinates.y)
        else:
            return (self.coordinates.x * value, self.coordinates.y * value)
          
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

vector = Vector(Point(1, 10))
print(vector(5))  # (5, 50)
print(vector())  # (1, 10)
print(vector(2))  # (2, 20)
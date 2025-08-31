"""                                     Автопрверка

1. Создайте класс Point, который будет отвечать за отображение геометрической точки на плоскости.

Реализовать инициализацию двух атрибутов через __init__конструктор: xи yкоординат.

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


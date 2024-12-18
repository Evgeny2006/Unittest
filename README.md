# Описание проекта
Проект содержит в себе вычисление периметра и площади плоских геометрических фигур (таких как: круг, прямоугольник, квадрат, треугольник), используя формулы ниже.


# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = $\frac{ah}{2}$

## Perimeter
- Circle: P = 2πR   
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Circle

```python
import math


def area(r):
    '''
    Принимает неотрицательное десятчиное число r и возвращает значение (в десятичном формате),
    равное площади окружности с радиусом r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает неотрицательное десятчиное число r и возвращает значение (в десятичном формате),
    равное длине окружности с радиусом r
    '''
    return 2 * math.pi * r
```
#### Примеры вызова

```python
r = 1
print(area(r))
print(perimeter(r))
```
```python
3.141592653589793
6.283185307179586
```
```python
r = 3.55
print(area(r))
print(perimeter(r))
```
```python
39.59192141686536
22.30530784048753
```
# Rectangle
```python
def area(a, b):
    '''
    Принимает два неотрицательных десятичных числа a и b и выводит значение (в десятичном формате),
    равное площади прямоугольника со сторонами длинами a и b
    '''
    return a * b

def perimeter(a, b):
    '''
    Принимает два неотрицательных десятичных числа a и b и выводит значение (в десятичном формате),
    равное периметру прямоугольника со сторонами длинами a и b
    '''
    return (a + b) * 2
```
#### Примеры вызова
```python
a, b = 5, 10
print(area(a, b))
print(perimeter(a, b))
```
```python
50 
30
```
```python
a, b = 3.2, 11.45
print(area(a, b))
print(perimeter(a, b))
```
```python
36.64
29.299999999999997
```

# Square
```python

def area(a):
    '''
    Принимает неотрицательное десятичное число a и возращает значение (в десятичном формате),
    равное площади квадрата со стороной a
    '''
    return a * a


def perimeter(a):
    '''
    Принимает неотрицательное десятичное число и возращает значение (в десятичном формате),
    равное периметру квадрата со стороной a
    '''
    return 4 * a
```
#### Примеры вызова
```python
a = 4
print(area(a))
print(perimeter(a))
```
```python
16
16
```
```python
a = 2.1
print(area(a))
print(perimeter(a))
```
```python
4.41
8.4
```

# Triangle
```python
def area(a, h):
    '''
    Принимает два неотрицательных десятичных числа a и h и выводит значение (в десятичном формате),
    равное площади треугольника со стороной длины a и с высотой, проведённой к этой стороне, длины h
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Принимает три неотрицательных десятичных числа a, b, c и выводит значение (в десятичном формате),
    равное периметру треугольника со сторонами a, b, c
    '''
    return a + b + c
```
#### Примеры вызова
```python
a, b, c = 1, 2, 3
h = 5
print(area(a, h))
print(perimeter(a, b, c))
```
```python
2.5
6
```
```python
a, b, c = 11.4, 5, 4.1
h = 3.012
print(area(a, h))
print(perimeter(a, b, c))
```
```python
17.168400000000002
20.5
```

# История изменений
![alt text](image.png)
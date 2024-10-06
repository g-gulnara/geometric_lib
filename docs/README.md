# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Библиотека geometric_lib
Это библиотека, написанная на языке программирования **Python**.

Файловая структура данной библиотеки:

    ├── circle.py
    ├── square.py
    └── docs
        └── README.md
    ├── rectangle.py
    ├── triangle.py

## Файл circle.py
Здесь находятся функции, вычисляющие площадь и периметр круга.

``` python
import math
```
Встроенный модуль math в Python. Предоставляет набор функций для выполнения математических, тригонометрических и логарифмических операций.

Функция **area()**:
- Принимает число r.
- Возвращает произведение квадрата числа r и числа pi - площадь круга.

```python
def area(r):
    return math.pi * r * r
```

Пример запуска функции:
```python
def area(r):
    return math.pi * r * r
    
print(area(2))
```
Вывод: 12.566370614359172

Функция **perimeter()**:
- Принимает число r.
- Возвращает удвоенное произведение чисел r и pi - периметр круга.
```python
def perimeter(r):  
    return 2 * math.pi * r
 ```

Пример запуска функции:
```python
def perimeter(r):  
    return 2 * math.pi * r

print(perimeter(3))
 ```
Вывод: 18.84955592153876

## Файл square.py
Здесь находятся функции, вычисляющие площадь и периметр квадрата.

Функция **area()**: 
- Принимает число a.
- Возвращает  квадрат числа a - площадь квадрата.:
``` python
def area(a):
    return a * a
```
Пример запуска функции:
``` python
def area(a):
    return a * a

print(area(4))
```

Вывод: 16

Функция **perimeter()**: 
- Принимает число a.
- Возвращает произведение чисел a и 4 - периметр квадрата.:
``` python
def perimeter(a):
    return 4 * a
```

Пример запуска функции:
``` python
def perimeter(a):
    return 4 * a

print(perimeter(2))
```
Вывод: 8

## Файл rectangle.py
Здесь находятся функции, вычисляющие площадь и периметр прямоугольника.

Функция **area()**: 
- Принимает числа a и b.
- Возвращает произведение a и b - площадь прямоугольника.
``` python
def area(a, b):
    return a * b 
```
Пример запуска функции:
``` python
def area(a, b):
    return a * b 

print(area(2, 3))
```
Вывод: 6

Функция **perimeter()**:
- Принимает числа a и b. 
- Возвращает удвоенную сумму сторон a и b прямоугольника - его периметр.
```python
def perimeter(a, b):
    return 2 * (a + b)
```
Пример запуска функции:
```python
def perimeter(a, b):
    return 2 * (a + b)

print(perimeter(2, 3))
```
Вывод: 10

## Файл triangle.py
Здесь находятся функции, вычисляющие площадь и периметр треугольника.

Функция **area()**: 

- Принимает числа a и h.

- Возвращает произведение a и h, делёное пополам - площадь треугольника.
```python
def area(a, h):
    return a * h / 2
```
Пример запуска функции:
```python
def area(a, h):
    return a * h / 2

print(area(5, 20))
```
Вывод: 50

Фукция perimeter():

- Принимает числа a, b и c.

- Возвращает периметр треугольника (сумма a, b и c).
``` python
def perimeter(a, b, c):
    return a + b + c
```
Пример запуска функции:
``` python
def perimeter(a, b, c):
    return a + b + c

print(perimeter(1, 2, 3))
```
Вывод: 6
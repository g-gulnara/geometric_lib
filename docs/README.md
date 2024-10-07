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
Это библиотека, написанная на языке программирования **Python**. Она вычисляет площадь и периметр круга, квадрата, прямоугольника и треугольника.

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

## История коммитов

```
* 6ed45fbb3f289243935fd66ea37bd4bf49c20682 (HEAD -> new_features_465514) add(README.md): general description was fixed
* e1dcfdbb50e01b128fde1ca65426732edd0cac67 (origin/new_features_465514) add(README.md): commit history was added
* 19eabb4bb2a0ccede1f5e1408fec26f103fd220d add(README.md): documentation was added
* b1abdf52dad0a225a9aac6f597408e4492bfa7ae Comments were added
* c8c613d63876bc2dbc60b6c717d57be58c300011 fix(rectangle.py): fucntions were fixed. fix(triangle.py): functions were fixed
* e0313f7c28621943d45ad779a97145e1289ac19f add (triangle.py): functions area and perimeter for a triangle fix (rectangle.py): function perimetr was fixed
* 752a3b18c5c8ed975293aa56f343ec28e866bb41 add (rectangle.py): functions area, perimeter
| * 86edb1c3dd57fa9abc7ba2ec7052507938084727 (upstream/release) L-05: Update Docs. Add user agreement info
| * 438b89a1dfc58d90e9036fe431771427965cd1ff L-05: Add user agreement
| * 6adb96248a4d00d3bea13bd95d78ef52352cd1b4 L-03: Docs added
| | * 30494317cde4419be779c14306561e0eaa78b88b (upstream/feature) L-04: Add rectangle.py
| |/
|/|
| | * b5b0fae727ca72c317c383b39c0af73d6adcd81c (upstream/develop) L-04: Update docs for calculate.py
| | * d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71 L-04: Add calculate.py
| | * 51c40ebfd0e0b65f52fe5e54740cbb038e492db3 L-04: Doc updated for triangle
| | * d080c7888b81955bad2ed78d58ad910526b5132a L-04: Triangle added
| |/
|/|
* | d078c8d9ee6155f3cb0e577d28d337b791de28e2 (upstream/main, upstream/HEAD, main) L-03: Docs added
|/
* 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
```
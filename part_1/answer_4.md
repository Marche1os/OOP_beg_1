### 4.1

```python
class Transport:
    def __init__(self, weight, type, speed):
        self.weight = weight
        self.type = type
        self.speed = speed

    def Run(self, speed): 
        self.speed = speed
        
class Bus(Transport):
    def __init__(self, doors_are_open, weight, type, speed, engine):
        super().__init__(weight, type, speed)
        self.doors_are_open = doors_are_open
        self.engine = engine

    def open_doors_for_passengers(self):
        self.doors_are_open = True

    def close_doors_for_passengers(self):
        self.doors_are_open = False
        
    def launchEngineAndMoveForward(self):
        self.engine.launch()
        self.Run(40)
        

class Engine:
    def __init__(self, is_running):
        self.is_running = is_running
    
    def launch(self):
        self.is_running = True
        
    def stop(self):
        self.is_running = False
        
class SportCar(Transport):
    def __init__(self, max_speed, has_furious, weight, type, wheels):
        super().__init__(weight, type)
        self.max_speed = max_speed
        self.current_speed = 0
        self.has_furious = has_furious
        self.wheels = wheels

    def run_to_max_speed(self):
        self.current_speed = self.max_speed

    def start_furious_if_has(self):
        if self.has_furious:
            self.current_speed = (self.max_speed * 2)
    
    def turn_to_right(self):
        for wheel in self.wheels:
            wheel.rotate_by(10)

class Wheel:
    def __init__(self, tread, slant):
        self.tread = tread
        self.slant = slant
    
    def rotate_by(self, slant_degrees):
        self.slant = slant_degrees
        
```

### 4.2

В прошлом задании мы реализовывали полиморфизм подтипов: строили иерархии классов, выделяли некий базовый тип, добавляли ему общее для всех подтипов поведение.
Такая иерархия классов и универсальная работа с базовым типом - пример полиморфизма подтипов.

Параметрический полиморфизм это отдельный код, который универсально работает с любым типом. 
В языках со статической типизацией (Как в Java) параметрический полиморфизм выражен через дженерики (Generic),
что позволяет нам задать общий тип и работать по независящей от типа логики.

### 4.3

```python
import random

class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")

def do_something_with_animal(animal: Animal):
    animal.foo()

def shuffle_animals(animals: list[Animal]):
    animals.clear()
    for i in range(0, 500):
        choice = random.randint(0, 1)
        if choice == 0:
            animals.append(Cat())
        else:
            animals.append(Bird())

    return animals



cat = Cat()
bird = Bird()

do_something_with_animal(cat)
do_something_with_animal(bird)

animals = [cat, bird]
shuffled_animals = shuffle_animals(animals)

for anim in shuffled_animals:
    anim.foo()
```

В выводе в случайном порядке выводился текст или "Птица поет", или "Кошка мурлычет".
Это полиморфизм в действии: мы случайным образом положили в список один из двух типов - Cat и Bird.
И так как у них переопределен метод foo, то автоматически вызвался переопределенный на стороне конкретного типа метод. 
В случае Cat это тело `print("Кошка мурлычет")`, а для Bird - `print("Птица поет")`
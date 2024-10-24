#Создание базового класса Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} жрет.")

#Создадим подклассы Bird, Mammal, и Reptile.
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} орет.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")

#Создадим функцию animal_sound()
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

#Использование композиции для создания класса Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

#Создадим классы ZooKeeper и Veterinarian.
class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f"{self.name} пора кормить {animal.name}.")

class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} пора лечить {animal.name}.")


# Создание животных
parrot = Bird("Попугай", 2, "Средний")
tiger = Mammal("Tiger", 5, "Оранжевый")
snake = Reptile("Питон", 3, "Гладкий")

# Создание сотрудников
keeper = ZooKeeper("Жора")
vet = Veterinarian("Доктор Лектор")

# Создание зоопарка и добавление животных и сотрудников
zoo = Zoo()
zoo.add_animal(parrot)
zoo.add_animal(tiger)
zoo.add_animal(snake)

zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрация полиморфизма
animal_sound(zoo.animals)

# Использование методов сотрудников
keeper.feed_animal(tiger)
vet.heal_animal(snake)

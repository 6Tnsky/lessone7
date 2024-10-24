import pickle


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

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump({'animals': self.animals, 'staff': self.staff}, file)
        print("Zoo state has been saved.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                self.animals = data['animals']
                self.staff = data['staff']
            print("Zoo state has been loaded.")
        except FileNotFoundError:
            print("File not found. Starting with an empty zoo.")


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

# Создание зоопарка
zoo = Zoo()

# Попробуем загрузить состояние зоопарка из файла
zoo.load_from_file('zoo_state.pkl')

# Создание животных
parrot2 = Bird("Ара", 2, "Большой>")
tiger2 = Mammal("Lion", 5, "Оранжевый")
snake2 = Reptile("Удав", 3, "Гладкий")

# Создание сотрудников
#keeper = ZooKeeper("Жора")
#vet = Veterinarian("Доктор Лектор")

# Создание зоопарка и добавление животных и сотрудников
#zoo = Zoo()
#zoo.add_animal(parrot2)
#zoo.add_animal(tiger2)
#zoo.add_animal(snake2)

#zoo.add_staff(keeper)
#zoo.add_staff(vet)

# Сохраним текущее состояние зоопарка в файл
zoo.save_to_file('zoo_state.pkl')

# Демонстрация полиморфизма
animal_sound(zoo.animals)

# Использование методов сотрудников
#keeper.feed_animal(tiger)
#vet.heal_animal(snake)

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но останется в истории.")

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f"В доме {self.name} не сеществует этажа под № {new_floor}")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        if isinstance(self, House):
            return self.number_of_floors

    def __str__(self):
        if isinstance(self, House):
            return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __ed__(self, other):
        if isinstance(other, House):
            return self.name == other.name and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors or self.number_of_floors == other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors or self.number_of_floors == other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.name != other.name and self.number_of_floors != other.number_of_floors

    def __iadd__(self, other):
        if isinstance(other, House):
            return self.number_of_floors

    def __eq__(self, other):
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors \
            and self.number_of_floors == other.number_of_floors


x = House('"ЖК Эльбрус"', 9)
y = House('"Домик в деревне"', 8)
x.go_to(12)
y.go_to(9)

x = House('ЖК Эльбрус', 10)
y = House('ЖК Акация', 20)

# __str__
print(x)
print(y)

# __len__
print(len(x))
print(len(y))

print(x == y)
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)
print(x != y)

x += y  # __iadd__
print(x)

x = y == x  # __radd__
print(x)

z = House('ЖК Матрёшки', 8)
print(House.houses_history)
p = House('ЖК Черти', 14)
print(House.houses_history)
del p
del z
print(House.houses_history)
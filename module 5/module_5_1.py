class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует!')
        else:
            for i in range(new_floor):
                print(i+1)


    def house_info(self):
        print(f'Название объекта: {self.name}, количество этажей: {self.number_of_floors} ')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Этажи', 25)
h4 = House('Василек', 5)
h1.go_to(5)
h2.go_to(10)
h3.go_to(25)
h4.go_to(9)
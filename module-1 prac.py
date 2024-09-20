class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def start_engine(self):
        return f"Двигатель {self.brand} {self.model} запущен."
    def stop_engine(self):
        return f"Двигатель {self.brand} {self.model} остановлен."


class Car(Vehicle):
    def __init__(self, brand, model, year, doors, transmission):
        super().__init__(brand, model, year)
        self.doors = doors
        self.transmission = transmission
    
    def __str__(self):
        return f"Автомобиль: {self.brand} {self.model}, {self.year} год, {self.doors} дверей, трансмиссия: {self.transmission}"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, body_type, has_box):
        super().__init__(brand, model, year)
        self.body_type = body_type
        self.has_box = has_box
    
    def __str__(self):
        return f"Мотоцикл: {self.brand} {self.model}, {self.year} год, тип кузова: {self.body_type},наличие бокса: {'Да' if self.has_box else 'Нет'}"



class Garage:
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        return f"Транспортное средство {vehicle.brand} {vehicle.model} добавлено в гараж."
    
    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            return f"Транспортное средство {vehicle.brand} {vehicle.model} удалено из гаража."
        else:
            return f"Транспортное средство {vehicle.brand} {vehicle.model} не найдено в гараже."
    
    def list_vehicles(self):
        return [str(vehicle) for vehicle in self.vehicles] if self.vehicles else "Гараж пуст."



class Fleet:
    def __init__(self):
        self.garages = []
    
    def add_garage(self, garage):
        self.garages.append(garage)
        return "Гараж добавлен в автопарк."
    
    def remove_garage(self, garage):
        if garage in self.garages:
            self.garages.remove(garage)
            return "Гараж удален из автопарка."
        else:
            return "Гараж не найден в автопарке."
    
    def search_vehicle(self, brand, model):
        for garage in self.garages:
            for vehicle in garage.vehicles:
                if vehicle.brand == brand and vehicle.model == model:
                    return f"Транспортное средство {brand} {model} найдено."
        return f"Транспортное средство {brand} {model} не найдено."


#мотоциклы и авто
car1 = Car("Toyota", "Camry", 2020, 4, "Автоматическая")
car2 = Car("Honda", "Civic", 2018, 4, "Механическая")
motorcycle1 = Motorcycle("Yamaha", "r1", 2021, "Спорт", False)
motorcycle2 = Motorcycle("Davidson", "83", 2019, "спорт", True)

garage1 = Garage()
garage2 = Garage()

print(garage1.add_vehicle(car1))
print(garage1.add_vehicle(motorcycle1))
print(garage2.add_vehicle(car2))
print(garage2.add_vehicle(motorcycle2))

# Список в гаражах
print("\nТранспортные средства в гараже 1:")
print(garage1.list_vehicles())
print("\nТранспортные средства в гараже 2:")
print(garage2.list_vehicles())






# автопарк 
fleet = Fleet()
print("\n" + fleet.add_garage(garage1))
print(fleet.add_garage(garage2))

# Поиск 
print("\n" + fleet.search_vehicle("Honda", "Civic"))
print(fleet.search_vehicle("Ford", "Mustang"))

# Удаление
print("\n" + garage1.remove_vehicle(motorcycle1))
print(garage1.list_vehicles())

print("\n" + fleet.remove_garage(garage2))

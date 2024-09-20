class Employee:
    def __init__(self, name, emp_id, position):
        self.name = name
        self.emp_id = emp_id
        self.position = position

    def calculate_salary(self):
        pass

class Worker(Employee):
    def __init__(self, name, emp_id, position, hourly_rate, hours_worked):
        super().__init__(name, emp_id, position)
        self.hourly_rate = hourly_rate  
        self.hours_worked = hours_worked 

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Manager(Employee):
    def __init__(self, name, emp_id, position, salary, bonus):
        super().__init__(name, emp_id, position)
        self.salary = salary 
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


class EmployeeSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


    def show_salaries(self):
        for emp in self.employees:
            print(f"Сотрудник: {emp.name}, Должность: {emp.position}, Зарплата: {emp.calculate_salary()} руб.")





worker1 = Worker("Асыл", 1, "Рабочий", hourly_rate=500, hours_worked=160)
worker2 = Worker("Ярослав", 2, "Рабочий", hourly_rate=450, hours_worked=170)
manager1 = Manager("Стас", 3, "Менеджер", salary=50000, bonus=10000)


employee_system = EmployeeSystem()

employee_system.add_employee(worker1)
employee_system.add_employee(worker2)
employee_system.add_employee(manager1)


employee_system.show_salaries()


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


user_1 = Position("Basil", "Ivanov", "разработчик", 200000, 100000)
print("Первый разработчик:", user_1.get_full_name())
print("Доход:", user_1.get_total_income())

user_1 = Position("Вася", "Пупкин", "президент", 200000000, 22000000000)
print("Первый разработчик:", user_1.get_full_name())
print("Доход:", user_1.get_total_income())

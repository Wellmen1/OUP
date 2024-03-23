# class Miko:
#     strange = 9
#     live = 5400
#     damage = 1962

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"
Student1 = Student("Іван",20)
print(Student1.get_info())
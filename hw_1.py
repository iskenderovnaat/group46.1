class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "женат/замужем" if self.is_married else "не женат/не замужем"
        print(f"Имя: {self.fullname}\nВозраст: {self.age}\nСемейное положение: {marital_status}")






class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks
    def calculate_average(self):
        if not self.marks:
            return 0
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        return total_marks / num_subjects

    def introduce_myself(self):
        super().introduce_myself()
        print("Оценки:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Средняя оценка: {self.calculate_average():.2f}\n")



class Teacher(Person):
    base_salary = 50000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            bonus_years = self.experience - 3
            bonus = bonus_years * (self.base_salary * 0.05)
        else:
            bonus = 0
        return self.base_salary + bonus

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Опыт работы: {self.experience} лет\nЗарплата: {self.calculate_salary():} сомов\n")




teacher = Teacher("Анна Сергеевна", 35, True, 10)
teacher.introduce_myself()


def create_students():
    student1 = Student("Адина Рахатова", 16, False, {"Математика": 3, "Физика": 5, "История": 5})
    student2 = Student("Анастасия Петрова", 17, False, {"Математика": 4, "Физика": 3, "История": 4})
    student3 = Student("Олег Иванов", 16, False, {"Математика": 5, "Физика": 5, "История": 3})
    return [student1, student2, student3]



students = create_students()
for student in students:
    student.introduce_myself



person = Person(fullname="Искендер Азизов", age=21, is_married=False)
person.introduce_myself()




student = Student(fullname="Ольга Анатольевна", age=18, is_married=False, marks={"Математика": 4, "История": 5, "Биология": 3})
student.introduce_myself()




teacher = Teacher(fullname="Алия Ишенбекова", age=40, is_married=True, experience=18)
teacher.introduce_myself()




students = create_students()
for student in students:
    student.introduce_myself()




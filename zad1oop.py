class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # lista ocen

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 50
# Przykładowe obiekty klasy Student


student1 = Student("Jan", [60, 70, 80])     # średnia = 70 → True
student2 = Student("Anna", [30, 40, 50])    # średnia = 40 → False

# Sprawdzenie wyników
print(student1.name, "passed:", student1.is_passed())
print(student2.name, "passed:", student2.is_passed())

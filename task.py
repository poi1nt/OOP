class Student:
    instance_list = []    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.__class__.instance_list.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
                return 'Ошибка'
            
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Cредняя оценка за домашние задания: {average_grade(self)}\n"
                f"Курсы вы процессе обучения: {(', '.join(self.courses_in_progress))}\n"
                f"Завершенные курсы: {(', '.join(self.finished_courses))}")
    
    def __lt__(self, other):
        if not isinstance(other, Student) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) < average_grade(other)

    def __le__(self, other):
        if not isinstance(other, Student) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) <= average_grade(other)

    def __eq__(self, other):
        if not isinstance(other, Student) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) == average_grade(other)
    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)            
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    instance_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.__class__.instance_list.append(self)

    def __str__(self):    
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self)}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) < average_grade(other)

    def __le__(self, other):
        if not isinstance(other, Lecturer) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) <= average_grade(other)

    def __eq__(self, other):
        if not isinstance(other, Lecturer) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) == average_grade(other)   

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    
def average_grade(self):
    if self.grades:
        return sum([sum(i) for i in self.grades.values()]) / sum([len(i) for i in self.grades.values()])
    else:
        return 'Оценок нет!'

def average_grade_students(students_list, course):
    result = 0
    count = 0
    for stud in students_list:
        if course in stud.courses_in_progress and course in stud.grades:
            result += sum(stud.grades[course]) / len(stud.grades[course])
            count += 1
    if count:
        return f'Средняя оценка студентов за курс: {course} - {result / count}'
    else:
        return 'нет данных для сравнения'

def average_grade_lecturers(lecturers_list, course):
    result = 0
    count = 0
    for lect in lecturers_list:
        if course in lect.courses_attached and course in lect.grades:
            result += sum(lect.grades[course]) / len(lect.grades[course])
            count += 1
    if count:
        return f'Средняя оценка лекторов за курс: {course} - {result / count}'
    else:
        return 'нет данных для сравнения'            
    
first_lecturer = Lecturer('Иван', 'Федотов')
second_lecturer = Lecturer('Ульяна', 'Чернова')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']
first_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

first_reviewer = Reviewer('Мария', 'Громова')
second_reviewer = Reviewer('Роман', 'Долгов')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Git']
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Git']

first_student = Student('Дмитрий','Крюков', 'м')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Введение в программирование']

second_student = Student('Анастасия','Зимина', 'ж')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Введение в программирование']

first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(second_lecturer, 'Python', 9)
first_student.rate_lecturer(first_lecturer, 'Git', 9)
first_student.rate_lecturer(second_lecturer, 'Git', 10)

second_student.rate_lecturer(first_lecturer, 'Python', 8)
second_student.rate_lecturer(second_lecturer, 'Python', 7)
second_student.rate_lecturer(first_lecturer, 'Git', 6)
second_student.rate_lecturer(second_lecturer, 'Git', 5)

first_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Git', 10)
first_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Git', 8)
first_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Git', 10)
first_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Git', 8)

print(first_student)
print(second_student)
print(first_lecturer)
print(second_lecturer)

print(average_grade_students(Student.instance_list, 'Python'))
print(average_grade_lecturers(Lecturer.instance_list, 'Git'))

print(first_student < second_student)
print(first_student > second_student)
print(first_student <= second_student)
print(first_student == second_student)
print(first_lecturer < second_lecturer)
print(first_lecturer > second_lecturer)
print(first_lecturer >= second_lecturer)
print(first_lecturer != second_lecturer)
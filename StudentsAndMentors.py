class Student:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}

	def __str__(self):
		res = f"{self.name}\n"
		res += f"{self.surname}\n"
		res += f"Средняя оценка за домашние задания: {self.average_grade(): .1f}\n"
		res += f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n"
		res += f"Завершенные курсы: {", ".join(self.finished_courses)}\n"
		return res

	def rate_hw(self, lecturer, course, grade):
		if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
			if course in lecturer.grades:
				lecturer.grades[course] += [grade]
			else:
				lecturer.grades[course] = [grade]
		else:
			return 'Ошибка'

	def average_grade(self):
		total_grade = []
		for grade in self.grades.values():
			total_grade.extend(grade)
		return sum(total_grade) / len(total_grade) if total_grade else 0


class Mentor:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.courses_attached = []


class Lecturer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)
		self.grades = {}

	def __str__(self):
		res = f"{self.name}\n"
		res += f"{self.surname}\n"
		res += f"Средняя оценка за лекции: {self.average_grade(): .1f}\n"
		return res

	def average_grade(self):
		total_grade = []
		for grade in self.grades.values():
			total_grade.extend(grade)
		return sum(total_grade) / len(total_grade)

class Reviewer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)

	def __str__(self):
		res = f"{self.name}\n{self.surname}\n"
		return res

	def rate_hw(self, student, course, grade):
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'


student1 = Student("Иван", "Головачев", "male")
lecturer1 = Lecturer("Олег", "Булыгин")
reviewer1 = Reviewer("Сергей", "Сергеев")
student2 = Student("Валерия", "Головачева", "female")
lecturer2 = Lecturer("Тимур", "Анвартдинов")
reviewer2 = Reviewer("Николай", "Николаев")


student1.finished_courses.append("Введение в программирование")
student1.courses_in_progress.append("Python")
student1.courses_in_progress.append("Git")
student2.finished_courses.append("Основы Python")
student2.courses_in_progress.append("Python")
student2.courses_in_progress.append("Git")

lecturer1.courses_attached.append("Python")
lecturer2.courses_attached.append("Git")
reviewer1.courses_attached.append("Python")
reviewer2.courses_attached.append("Git")

reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "Python", 8)
reviewer2.rate_hw(student1, "Git", 9)
reviewer2.rate_hw(student1, "Git", 9)

reviewer1.rate_hw(student2, "Python", 6)
reviewer1.rate_hw(student2, "Python", 8)
reviewer2.rate_hw(student2, "Git", 6)
reviewer2.rate_hw(student2, "Git", 7)

student1.rate_hw(lecturer1, "Python", 10)
student1.rate_hw(lecturer1, "Git", 8)
student1.rate_hw(lecturer2, "Python", 4)
student1.rate_hw(lecturer2, "Git", 5)

student2.rate_hw(lecturer1, "Python", 8)
student2.rate_hw(lecturer1, "Git", 6)
student2.rate_hw(lecturer2, "Python", 8)
student2.rate_hw(lecturer2, "Git", 6)

print(student1)
print(student2)
print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)

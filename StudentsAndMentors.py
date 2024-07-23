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
		res += f"Средняя оценка за домашние задания: {self.average_grade():1f}\n"
		res += f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n"
		res += f"Завершенные курсы: {", ".join(self.finished_courses)}"
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
		return 0


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
		res += f"Средняя оценка за лекции: {self.average_grade():1f}\n"
		return res

class Reviewer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)

	def __str__(self):
		res = f"{self.name}\n{self.surname}"
		return res

	def rate_hw(self, student, course, grade):
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'


student1 = Student("Ivan", "Golovachev", "male")
print(student1)
reviewer1 = Reviewer("Олег", "Булыгин")

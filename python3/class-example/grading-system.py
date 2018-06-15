

#purpose: create a "grading system" that manages students, teachers, and grades

#breakdown: have a Student class, a Teacher class, and a Course class

cutoffs = [
  (81, 'A'), # if grade > number, return letter.
  (61, 'B'),
  (41, 'C'),
  (21, 'D'),
  (0,  'F'), # This is -1, aka the last item
]

def number_to_grade(number):
	for cutoff in cutoffs:
		if number > cutoff[0]: # Because it's the number in the list of tuples
			return cutoff[1] # We return the letter in the list of tuples

	return cutoff[-1][1] # Return lowest grade otherwise

class Student:

	grade = 100 # Students have grades.

	def __init__(self):
		pass
		# self.join_course


	def __del__(self):
		print("Student dropped from course!")

	def complete(self, assignment): # As a Student, complete an Assignment.
		assignment.students_completed.add(self)

s = Student()
a = Assignment()

s.complete(a)

s.__del__()
del s


class Assignment:

	students_completed = set() # A list of students who have completed this assignment

	def __init__(self):
		pass

	def student_finished(student):
		return True if (student in students_completed) else False


class Course:

	def __init__(self, name="Course about Courses"): # name is this BY DEFAULT, but is different if an arg is given.
		self.name = name

	def math(self):
		self.room = "101"

	def english(self):
		self.room = "102"

	def comp_sci(self):
		self.room = "103"


class Teacher:

	course = Course("I am a cool course")

	def __init__(self):
		pass






Christian_Hunter = Student()
print(Christian_Hunter.grade)

Henry = Teacher()

Henry.course.name = "an even better course"
print(Henry.course.name)

a = Assignment()

a.student_finished.add(Christian_Hunter) # Direct manipulation of the data structure

Christian_Hunter.complete(a) # A little nicer

c = Course()
print(c.name)



# Teachers can add assignments to the Course

# Students can join or leave Courses

# Upon joining a Course..
#  the student is initially assigned with all 0's for all existisng assignments

# Upon a teacher adding an assignment to a Course...
#  all enrolled students are initially given 0's for the assignment

# Upon withdrawing from a course...
#  all grades a student has earned in the course are dropped/removed

# Students can be in multiple courses

# Courses can contain multiple students::

# Only one teacher can be in charge of a course

# Students and teachers have First and Last names

# Courses have room numbers & subject names

# A course should be able to report how many students are enrolled

# A course should be able to report the name of the professor

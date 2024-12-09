# Define the base class Course
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_info(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"


# Define the subclass CoreCourse which inherits from Course
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_info(self):
        core_info = super().display_info()
        return f"{core_info}, Required for Major: {self.required_for_major}"


# Define the subclass ElectiveCourse which inherits from Course
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_info(self):
        elective_info = super().display_info()
        return f"{elective_info}, Elective Type: {self.elective_type}"


# Example usage
core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course = ElectiveCourse("HS101", "Introduction to History", 2, "Liberal Arts")

print(core_course.display_info())
print(elective_course.display_info())






# employee.py
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

# main.py
from employee import Employee

# Create an Employee object
employee_1 = Employee("John Doe", 50000)

# Display the employee's name and salary
print(f"Employee Name: {employee_1.get_name()}")
print(f"Employee Salary: {employee_1.get_salary()}")



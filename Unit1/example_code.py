# Don't worry about this code for now, you're welcome to look at it if you want to, but you might not understand it yet. That is okay! You don't need to know everything to make things work!
# Python is a popular language for this exact reason, it's easy to learn and use without having to know everything about it or write everything from scratch!
# Why reinvent the wheel when you can use something that already works?

# This code will be imported into the lesson files so you can use some more complex code that we'll learn about later.


class student:
    def __init__(self, name):
        self.name = name
        self._classes = {} 
        self.gpa = 0.0
        self.add_class("Math", 89)
        self.add_class("Science", 37)
        self.add_class("English", 100)

    # The class inside of the student class. It's a class inside of a class that is called "Class". Duh.
    class Class:
        def __init__(self, student, class_name, grade = 0):
            self._student = student
            self._name = class_name
            self.grade = grade

        def get_grade(self):
            return self.grade
        def do_homework(self, times = 1):
            for _ in range(times):
                print(f"{self._student.name} is doing homework for {self._name} class. {self._student.name}'s grade increased!")
                if self.grade < 100:
                    self.grade += 10
                if self.grade > 100:
                    self.grade = 100
            else:
                print(f"{self._student.name} is already at 100%! You should probably do work for another class!")

    def add_class(self, class_name, grade = 0):
        """Add a new Class for this student."""
        if class_name in self._classes:
            print(f"{self.name} already has a class named '{class_name}'.")
        else:
            class_instance = self.Class(self, class_name, grade)
            class_name = class_name.lower().strip().replace(" ", "_")
            self._classes[class_name] = class_instance
            setattr(self, class_name, class_instance)

    def __getattr__(self, attr):
        # only allow access to classes explicitly added
        if attr in self._classes:
            return self._classes[attr]
        raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {attr!r}")
    
    def get_gpa(self):
        """Prints the calculation for the student's GPA"""
        print(f"{self.name}'s GPA:")
        if self.gpa is None:
            self.calculate_gpa()
        print(f"GPA: {self.gpa}")
        return self.gpa
    def calculate_gpa(self):
        """Calculates the student's GPA"""
        print(f"Calculating {self.name}'s GPA...")
        total_grade = 0
        for _class in self._classes.values():
            total_grade += _class.get_grade()
        
        self.gpa = (total_grade / len(self._classes.values()))/25
        return self.gpa

    def print_classes(self):
        """prints a formatted list of the student's classes and grades"""
        print(f"{self.name}'s classes:")
        for _class in self._classes.values():
            print(f"{_class._name}: {_class.get_grade()}")

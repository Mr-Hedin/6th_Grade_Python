# Now we're going to make our student do some work!
# Don't worry, this is the easiest homework assignment you'll ever see a student do!

# First we're going to import the example_code module again.
import example_code

# Now we're going to create a student object to work with.
student = example_code.student("Bob the Destroyer")

# Now we're going to add a class to our student!
# This is called "calling a method"
# The stuff in the parentheses is called an "argument", it tells the method any extra information it needs to do its job. In this case, we're adding a class called "Computer Science" to the student.
student.add_class("Computer Science")

# Now we're going to print out the student's classes and grades by calling the print_classes method! This should tell us our classes and grades.
student.print_classes()

# Looks like we're not doing so hot in our Computer Science class.
# Let's make our student do some homework and see if it helps!


# Use the following method to do homework: student.computer_science.do_homework()

...

# Try calling the print_classes method again to see if the grade changed. Look at the example code to see how to call the method, usually you can reuse other's code to make your own.
...


# One last thing, some methods can take multiple arguments.
# Try adding a class with a grade of 100 to our student's schedule! Seems easier than doing all that homework...

student.add_class("History", 100)
student.print_classes()

# Add your own, then make that student do some homework for their new class!

student.add_class(..., ...)

student.print_classes()


# ----------------VOCAB------------------
# 1. Method - What the object can do. Like a student can do homework.
# 2. Call - To use a method. Like calling do_homework() to make the student do homework.

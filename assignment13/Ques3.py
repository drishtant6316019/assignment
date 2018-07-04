'''Ques 3. What will be the output of the following code:

# Program to depict Raising Exception

try:
    raise NameError("hello world")  # Raise Error
except NameError:
    print
    "no one here"
    raise  # To determine whether the exception was raised or not'''


# try:
#     raise NameError("Hello world")  # Raise Error
# except NameError:
#     print
#     "no one here"
#     raise

# Output...
# Traceback (most recent call last):
#   File "C:/Users/HP/PycharmProjects/Python_Assignments/Ques3.py", line 14, in <module>
#     raise NameError("Hello world")  # Raise Error
# NameError: Hello world



# Code of removing above Error
try:
    raise NameError("Hello world")
except NameError:
    print("no one here")


# Output...

# no one here
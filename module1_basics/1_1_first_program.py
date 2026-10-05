# ============================================================
# IBM PY0101EN - Python for Data Science
# Module 1 - Lesson 1: FULL SUMMARY
# Topic: Your First Program
# ============================================================
# HOW TO USE THIS FILE:
#   1. Read each section.
#   2. Run the file:  python 1_0_lesson1_summary.py
#   3. Uncomment the "TRY IT" lines and re-run.
#   4. Break things on purpose. Read the errors.
# ============================================================


# ------------------------------------------------------------
# SECTION 1 - WHAT IS PYTHON?
# ------------------------------------------------------------
# Python is a high-level, interpreted programming language.
# - High-level  : reads like English
# - Interpreted : runs line by line, no compile step
# - Executes    : top to bottom, one line at a time
# ------------------------------------------------------------


# ------------------------------------------------------------
# SECTION 2 - YOUR FIRST PROGRAM
# ------------------------------------------------------------
# print() displays output on the screen.
# "..." is a STRING (text data).
# ( ) hold the ARGUMENTS (inputs) to the function.

print("Hello, world!")
print("My name is Student.")
print("I am learning Python for Data Science.")


# ------------------------------------------------------------
# SECTION 3 - PYTHON IS CASE-SENSITIVE
# ------------------------------------------------------------
# print  -> valid function
# Print  -> NameError (Python doesn't know "Print")
# PRINT  -> NameError

# TRY IT (uncomment one at a time and re-run):
# Print("Hello")     # NameError
# PRINT("Hello")     # NameError


# ------------------------------------------------------------
# SECTION 4 - COMMON ERRORS (READ THESE OUT LOUD)
# ------------------------------------------------------------
# SyntaxError : broken grammar. Example: print("Hello)   <- missing quote
# NameError   : unknown name.    Example: print(hello)     <- hello not defined
# TypeError   : wrong type.      Example: "Hello" + 5      <- str + int
# ValueError  : wrong value.     Example: int("abc")       <- can't convert

# TRY IT (uncomment one at a time):
# print("Hello)          # SyntaxError
# print(hello)           # NameError
# print("Hello" + 5)     # TypeError
# int("abc")             # ValueError


# ------------------------------------------------------------
# SECTION 5 - COMMENTS
# ------------------------------------------------------------
# Single-line comment: starts with #
# Python ignores comments when running.
# Use comments to explain WHY, not WHAT.

# This is a comment
print("Comments are ignored by Python")  # inline comment


# ------------------------------------------------------------
# SECTION 6 - PRINTING MULTIPLE THINGS
# ------------------------------------------------------------
# print() can take multiple arguments, separated by commas.
# By default, Python adds a space between them.

print("Python", "for", "Data", "Science")
# Output: Python for Data Science

# The 'sep' argument changes the separator:
print("Python", "for", "Data", "Science", sep="-")
# Output: Python-for-Data-Science

# The 'end' argument changes what's printed at the end:
print("Line 1", end=" | ")
print("Line 2")
# Output: Line 1 | Line 2


# ------------------------------------------------------------
# SECTION 7 - ESCAPE CHARACTERS
# ------------------------------------------------------------
# \n  -> new line
# \t  -> tab
# \\  -> backslash
# \"  -> double quote inside a double-quoted string

 


# ------------------------------------------------------------
# SECTION 8 - KEY TAKEAWAYS (MEMORIZE THESE)
# ------------------------------------------------------------
# 1. Python runs top to bottom.
# 2. print() displays output.
# 3. Strings are text wrapped in quotes (" " or ' ').
# 4. Python is case-sensitive: print != Print.
# 5. Errors are messages, not failures.
# 6. # starts a comment.
# 7. sep= and end= control print() formatting.
# 8. \n and \t are escape characters.


# ------------------------------------------------------------
# SECTION 9 - SELF-CHECK (MCQ - answer in comments below)
# ------------------------------------------------------------
# Q1. What does print("Hello") do?
#     a) Reads input
#     b) Displays Hello on screen
#     c) Stores Hello in a variable
#     d) Deletes Hello
#
# YOUR ANSWER: b
#
# Q2. Which is a valid string?
#     a) Hello
#     b) 'Hello'
#     c) (Hello)
#     d) print
#
# YOUR ANSWER: b
#
# Q3. What error does print("Hello) raise?
#     a) NameError
#     b) ValueError
#     c) SyntaxError
#     d) TypeError
#
# YOUR ANSWER: c
#
# Q4. What error does Print("Hello") raise?
#     a) Prints Hello
#     b) NameError
#     c) SyntaxError
#     d) Nothing
#
# YOUR ANSWER: b
#
# Q5. Python executes code in which order?
#     a) Bottom to top
#     b) Random
#     c) Top to bottom
#     d) Alphabetical
#
# YOUR ANSWER: c


# ------------------------------------------------------------
# SECTION 10 - YOUR TO-DO
# ------------------------------------------------------------
# [1] Run this file.
# [1] Uncomment each "TRY IT" line, run, read the error.
# [1] Answer Q1-Q5 above in the comments.
print("Abdelbaset")
print("City:", " ", "Sohag")
print("Age\t29")
# [1] Write 3 new print() lines about yourself.
# [1] Move on to Lesson 1.2 - Types.
# ------------------------------------------------------------


# ------------------------------------------------------------
# END OF LESSON 1 SUMMARY
# ------------------------------------------------------------
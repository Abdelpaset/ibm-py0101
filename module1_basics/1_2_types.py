# ============================================================
# IBM PY0101EN - Python for Data Science
# Module 1 - Lesson 1.2: TYPES
# ============================================================
# HOW TO USE THIS FILE:
#   Run it:  python 1_2_types.py
#   Read the output. Answer the quiz at the bottom.
# ============================================================


# ------------------------------------------------------------
# SECTION 1 - WHAT IS A TYPE?
# ------------------------------------------------------------
# Every value in Python has a TYPE.
# The type tells Python:
#   - What the value means
#   - What you can do with it
#   - How it is stored in memory
#
# The 4 core types you must know:
#   int    -> whole numbers        (e.g., 42, -7, 0)
#   float  -> decimal numbers      (e.g., 3.14, -0.5, 2.0)
#   str    -> text                 (e.g., "hello", 'python')
#   bool   -> True or False        (only two values)
# ------------------------------------------------------------


# ------------------------------------------------------------
# SECTION 2 - THE type() FUNCTION
# ------------------------------------------------------------
# type(x) returns the type of x.

print("=== Section 2: type() ===")
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>


# ------------------------------------------------------------
# SECTION 3 - INT (whole numbers)
# ------------------------------------------------------------
# int = integer. No decimal point.
# Can be positive, negative, or zero.
# No limit on size in Python 3.

print("\n=== Section 3: int ===")
age = 29
year = 2026
temperature = -5
print(age, type(age))
print(year, type(year))
print(temperature, type(temperature))

# Big numbers work fine:
big = 123456789012345678901234567890
print(big, type(big))


# ------------------------------------------------------------
# SECTION 4 - FLOAT (decimal numbers)
# ------------------------------------------------------------
# float = floating-point number. Has a decimal point.
# Used for measurements, money, science, etc.

print("\n=== Section 4: float ===")
pi = 3.14159
price = 19.99
negative = -0.5
whole_like = 2.0     # still a float because of the .0
print(pi, type(pi))
print(price, type(price))
print(negative, type(negative))
print(whole_like, type(whole_like))


# ------------------------------------------------------------
# SECTION 5 - STR (text)
# ------------------------------------------------------------
# str = string. Text wrapped in quotes.
# Single ' ' or double " " quotes both work.
# Strings can be empty: ""

print("\n=== Section 5: str ===")
name = "Abdelbaset"
country = 'Egypt'
empty = ""
number_as_text = "29"    # this is TEXT, not a number
print(name, type(name))
print(country, type(country))
print(empty, type(empty))
print(number_as_text, type(number_as_text))


# ------------------------------------------------------------
# SECTION 6 - BOOL (True / False)
# ------------------------------------------------------------
# bool = boolean. Only two values: True or False.
# Note the CAPITAL T and F.
# Used in conditions (if statements) - we'll see this in Module 3.

print("\n=== Section 6: bool ===")
is_student = True
is_teacher = False
print(is_student, type(is_student))
print(is_teacher, type(is_teacher))

# true (lowercase) is NOT the same as True:
# print(true)   # NameError


# ------------------------------------------------------------
# SECTION 7 - TYPE CONVERSION (casting)
# ------------------------------------------------------------
# You can convert between types using:
#   int(x)   -> convert x to integer
#   float(x) -> convert x to float
#   str(x)   -> convert x to string
#   bool(x)  -> convert x to boolean

print("\n=== Section 7: Type Conversion ===")

# str -> int
print(int("42"))          # 42
print(int("42") + 8)      # 50

# str -> float
print(float("3.14"))      # 3.14

# int -> float
print(float(5))           # 5.0

# int -> str
print(str(100))           # "100"
print(str(100) + "!")     # "100!"  (concatenation, not addition)

# float -> int (TRUNCATES, does not round)
print(int(3.99))          # 3  (not 4!)
print(int(-3.99))         # -3

# bool conversions
print(bool(0))            # False  (0 is falsy)
print(bool(1))            # True
print(bool(""))           # False  (empty string is falsy)
print(bool("hello"))      # True
print(bool(0.0))          # False


# ------------------------------------------------------------
# SECTION 8 - TYPE ERRORS (common beginner trap)
# ------------------------------------------------------------

print("\n=== Section 8: Common Type Errors ===")

# Adding string + int  -> TypeError
try:
    print("Age: " + 29)   #use: str(29)
except TypeError as e:
    print("TypeError:", e)

# Fix: convert int to str
print("Age: " + str(29))       # works
print(f"Age: {29}")            # works (f-string)

# Adding string number + int  -> surprise!
print("5" + "3")               # "53"  (string concatenation)
print(int("5") + int("3"))     # 8     (real addition)


# ------------------------------------------------------------
# SECTION 9 - len() AND str vs int
# ------------------------------------------------------------
# len(x) returns the length of a string (number of characters).
# You CANNOT use len() on int or float.

print("\n=== Section 9: len() ===")
print(len("hello"))       # 5
print(len(""))            # 0
print(len("Python 3"))    # 8

# print(len(42))   # TypeError: object of type 'int' has no len()


# ------------------------------------------------------------
# SECTION 10 - QUICK REFERENCE TABLE
# ------------------------------------------------------------
# +----------------+-------------------+---------------------+
# | Type           | Example           | type() returns      |
# +----------------+-------------------+---------------------+
# | int            | 42, -7, 0         | <class 'int'>       |
# | float          | 3.14, -0.5, 2.0   | <class 'float'>     |
# | str            | "hello", 'a', ""  | <class 'str'>       |
# | bool           | True, False       | <class 'bool'>      |
# +----------------+-------------------+---------------------+


# ------------------------------------------------------------
# SECTION 11 - KEY TAKEAWAYS
# ------------------------------------------------------------
# 1. Every value has a type.
# 2. int, float, str, bool are the 4 core types.
# 3. type(x) tells you the type of x.
# 4. int("42") and str(42) convert between types.
# 5. int(3.99) truncates to 3 (does NOT round).
# 6. "5" + "3" gives "53", not 8.
# 7. bool(0), bool(""), bool(0.0) are all False.
# 8. len() works on strings, NOT on numbers.


# ============================================================
# SECTION 12 - MCQ QUIZ
# ============================================================
# Answer in the YOUR ANSWER lines below.
# Then run: python 1_2_types.py
# The quiz will also run interactively at the end.

# Q1. What is the type of 3.14?
#     a) int
#     b) float
#     c) str
#     d) bool
#
# YOUR ANSWER: ___

# Q2. What does type("42") return?
#     a) <class 'int'>
#     b) <class 'float'>
#     c) <class 'str'>
#     d) <class 'bool'>
#
# YOUR ANSWER: ___

# Q3. What does int(3.99) return?
#     a) 4
#     b) 3
#     c) 3.99
#     d) Error
#
# YOUR ANSWER: ___

# Q4. What does "5" + "3" produce?
#     a) 8
#     b) "53"
#     c) 53
#     d) Error
#
# YOUR ANSWER: ___

# Q5. What does bool("") return?
#     a) True
#     b) False
#     c) Error
#     d) ""
#
# YOUR ANSWER: ___

# Q6. What does len("Python") return?
#     a) 5
#     b) 6
#     c) 7
#     d) Error
#
# YOUR ANSWER: ___

# Q7. Which type has only two possible values?
#     a) int
#     b) float
#     c) str
#     d) bool
#
# YOUR ANSWER: ___


# ============================================================
# SECTION 13 - INTERACTIVE QUIZ (runs when you execute the file)
# ============================================================

def quiz():
    questions = [
        {
            "q": "Q1. What is the type of 3.14?",
            "options": ["int", "float", "str", "bool"],
            "answer": "float"
        },
        {
            "q": "Q2. What does type('42') return?",
            "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'bool'>"],
            "answer": "<class 'str'>"
        },
        {
            "q": "Q3. What does int(3.99) return?",
            "options": ["4", "3", "3.99", "Error"],
            "answer": "3"
        },
        {
            "q": "Q4. What does '5' + '3' produce?",
            "options": ["8", "53", "Error", "'8'"],
            "answer": "53"
        },
        {
            "q": "Q5. What does bool('') return?",
            "options": ["True", "False", "Error", "''"],
            "answer": "False"
        },
        {
            "q": "Q6. What does len('Python') return?",
            "options": ["5", "6", "7", "Error"],
            "answer": "6"
        },
        {
            "q": "Q7. Which type has only two possible values?",
            "options": ["int", "float", "str", "bool"],
            "answer": "bool"
        }
    ]

    score = 0
    total = len(questions)

    print("\n" + "=" * 50)
    print("LESSON 1.2 - TYPES QUIZ")
    print("=" * 50)

    for item in questions:
        print("\n" + item["q"])
        for i, opt in enumerate(item["options"], 1):
            print(f"  {i}. {opt}")
        while True:
            try:
                c = int(input("Your answer (1-4): "))
                if 1 <= c <= len(item["options"]):
                    break
                print("Enter 1-4.")
            except ValueError:
                print("Enter a number.")
        if item["options"][c - 1] == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer: {item['answer']}")

    print("\n" + "=" * 50)
    print(f"Score: {score}/{total}")
    if score == total:
        print("Perfect. Move to Lesson 1.3 - Expressions and Variables.")
    elif score >= total * 0.7:
        print("Good. Review missed questions, then move on.")
    else:
        print("Reread Section 2-8 and retake the quiz.")
    print("=" * 50)


if __name__ == "__main__":
    quiz()


# ------------------------------------------------------------
# SECTION 14 - YOUR TO-DO
# ------------------------------------------------------------
# [ ] Run this file. Read every output line.
# [ ] Answer Q1-Q7 in Section 12 comments.
# [ ] Take the interactive quiz at the end.
# [ ] Reply with:
#       - Your comment answers (e.g., 1-b, 2-c, ...)
#       - Your interactive quiz score
#       - One thing that surprised you
# [ ] Move on to Lesson 1.3 - Expressions and Variables.
# ------------------------------------------------------------
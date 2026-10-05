# ============================================================
# IBM PY0101EN - Python for Data Science
# Module 1 - Lesson 1.3: EXPRESSIONS AND VARIABLES
# ============================================================
# HOW TO USE THIS FILE:
#   Run it:  python 1_3_expressions_variables.py
#   Read every output line. Answer the quiz at the end.
# ============================================================


# ------------------------------------------------------------
# SECTION 1 - WHAT IS AN EXPRESSION?
# ------------------------------------------------------------
# An EXPRESSION is any piece of code that PRODUCES A VALUE.
# Python evaluates it and hands you back a result.
#
# Examples of expressions:
#   5 + 3            -> 8
#   10 / 2           -> 5.0
#   "Hello" + "!"    -> "Hello!"
#   2 > 1            -> True
# ------------------------------------------------------------


# ------------------------------------------------------------
# SECTION 2 - WHAT IS A VARIABLE?
# ------------------------------------------------------------
# A VARIABLE is a NAME that points to a value in memory.
# Assignment uses the "=" sign.
#   name = expression
#
# Read "=" as "gets" or "is assigned", NOT "equals".
# ------------------------------------------------------------

print("=== Section 2: Variables ===")
x = 5              # x gets 5
y = x + 3          # y gets the result of x + 3 (= 8)
name = "Abdelbaset"
is_student = True

print("x =", x)
print("y =", y)
print("name =", name)
print("is_student =", is_student)


# ------------------------------------------------------------
# SECTION 3 - ARITHMETIC OPERATORS
# ------------------------------------------------------------
# +   addition           5 + 3  -> 8
# -   subtraction        5 - 3  -> 2
# *   multiplication     5 * 3  -> 15
# /   TRUE division      5 / 2  -> 2.5   (always returns float)
# //  FLOOR division     5 // 2 -> 2     (drops the decimal)
# %   MODULUS (remainder) 5 % 2 -> 1
# **  EXPONENT           5 ** 2 -> 25
# ------------------------------------------------------------

print("\n=== Section 3: Arithmetic Operators ===")
a = 10
b = 3

print("a =", a, ", b =", b)
print("a + b =", a + b)     # 13
print("a - b =", a - b)     # 7
print("a * b =", a * b)     # 30
print("a / b =", a / b)     # 3.333...   (float)
print("a // b =", a // b)   # 3          (int)
print("a % b =", a % b)     # 1
print("a ** b =", a ** b)   # 1000

# Division ALWAYS returns float, even when exact:
print("10 / 2 =", 10 / 2)   # 5.0 (not 5)

# Modulus is great for even/odd checks:
print("10 % 2 =", 10 % 2)   # 0  -> 10 is even
print("7 % 2 =", 7 % 2)     # 1  -> 7 is odd


# ------------------------------------------------------------
# SECTION 4 - OPERATOR PRECEDENCE (order of operations)
# ------------------------------------------------------------
# Python follows PEMDAS, with a couple of rules:
#
#   1. ()       parentheses
#   2. **       exponent
#   3. * / // % multiplication, division, modulus  (left to right)
#   4. + -      addition, subtraction              (left to right)
#
# When in doubt, USE PARENTHESES. Readability wins.
# ------------------------------------------------------------

print("\n=== Section 4: Precedence ===")
print("2 + 3 * 4 =", 2 + 3 * 4)         # 14, not 20
print("(2 + 3) * 4 =", (2 + 3) * 4)     # 20
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)     # 512 (right-associative)
print("2 + 10 / 2 =", 2 + 10 / 2)       # 7.0
print("10 - 2 - 3 =", 10 - 2 - 3)       # 5 (left to right)


# ------------------------------------------------------------
# SECTION 5 - COMPARISON OPERATORS (produce booleans)
# ------------------------------------------------------------
# ==   equal to
# !=   not equal to
# <    less than
# >    greater than
# <=   less than or equal
# >=   greater than or equal
#
# WARNING: == is COMPARISON, = is ASSIGNMENT. Do not confuse.
# ------------------------------------------------------------

print("\n=== Section 5: Comparison ===")
print("5 == 5  ->", 5 == 5)      # True
print("5 == 6  ->", 5 == 6)      # False
print("5 != 6  ->", 5 != 6)      # True
print("5 < 10  ->", 5 < 10)      # True
print("5 >= 5  ->", 5 >= 5)      # True
print("5 > 10  ->", 5 > 10)      # False

# Strings compare alphabetically (lexicographically):
print("'apple' < 'banana' ->", "apple" < "banana")   # True


# ------------------------------------------------------------
# SECTION 6 - LOGICAL OPERATORS (and / or / not)
# ------------------------------------------------------------
# and : True only if BOTH sides are True
# or  : True if AT LEAST ONE side is True
# not : flips True/False
#
# Truth tables:
#   True  and True   -> True
#   True  and False  -> False
#   False or  True   -> True
#   False or  False  -> False
#   not True         -> False
# ------------------------------------------------------------

print("\n=== Section 6: Logical Operators ===")
print("True and True   ->", True and True)     # True
print("True and False  ->", True and False)    # False
print("False or True   ->", False or True)     # True
print("False or False  ->", False or False)    # False
print("not True        ->", not True)          # False
print("not False       ->", not False)         # True

# Combining:
age = 25
print("age > 18 and age < 65 ->", age > 18 and age < 65)   # True


# ------------------------------------------------------------
# SECTION 7 - VARIABLE NAMING RULES
# ------------------------------------------------------------
# Rules (must follow):
#   - Must start with a letter or underscore _
#   - Can contain letters, digits, underscores
#   - Case-sensitive: age, Age, AGE are three different names
#   - Cannot be a Python keyword (if, for, while, class, etc.)
#
# Conventions (should follow):
#   - Use snake_case: student_name, total_price
#   - Use meaningful names: "price" not "p"
#   - Avoid single letters except loop counters (i, j)
# ------------------------------------------------------------

print("\n=== Section 7: Naming ===")
student_name = "Abdelbaset"
total_price = 99.99
is_active = True
_private = "convention: leading _ means internal use"

print(student_name, total_price, is_active)

# Bad examples (do NOT do this):
# 1st_place = "x"     # SyntaxError: starts with digit
# my-var = 5          # SyntaxError: hyphen not allowed
# class = "Math"      # SyntaxError: 'class' is a keyword


# ------------------------------------------------------------
# SECTION 8 - MULTIPLE ASSIGNMENT
# ------------------------------------------------------------
# You can assign multiple variables in one line.
# ------------------------------------------------------------

print("\n=== Section 8: Multiple Assignment ===")

# Unpacking (one-to-one):
x, y, z = 1, 2, 3
print("x, y, z =", x, y, z)

# Same value to many variables:
a = b = c = 0
print("a, b, c =", a, b, c)

# Swap without a temporary variable (Pythonic!):
p, q = 10, 20
print("before swap:", p, q)
p, q = q, p
print("after swap: ", p, q)


# ------------------------------------------------------------
# SECTION 9 - AUGMENTED ASSIGNMENT
# ------------------------------------------------------------
# Shorthand for "apply operator and reassign".
#   x += 5   is the same as   x = x + 5
#   x -= 5   is the same as   x = x - 5
#   x *= 5   is the same as   x = x * 5
#   x /= 5   is the same as   x = x / 5
#   x //= 5  is the same as   x = x // 5
#   x %= 5   is the same as   x = x % 5
#   x **= 5  is the same as   x = x ** 5
# ------------------------------------------------------------

print("\n=== Section 9: Augmented Assignment ===")
n = 10
print("start:", n)
n += 5;  print("n += 5  ->", n)   # 15
n -= 3;  print("n -= 3  ->", n)   # 12
n *= 2;  print("n *= 2  ->", n)   # 24
n //= 5; print("n //= 5 ->", n)   # 4
n **= 3; print("n **= 3 ->", n)   # 64


# ------------------------------------------------------------
# SECTION 10 - WORKING WITH STRINGS (brief preview)
# ------------------------------------------------------------
# + concatenates strings
# * repeats strings
# (Full string operations come in Lesson 1.4)
# ------------------------------------------------------------

print("\n=== Section 10: String Expressions ===")
first = "Abdel"
last = "baset"
print(first + " " + last)    # concatenation
print("ha" * 3)              # "hahaha"
print("-" * 30)              # a divider line


# ------------------------------------------------------------
# SECTION 11 - QUICK REFERENCE TABLE
# ------------------------------------------------------------
# +------------------+--------------------------+------------------+
# | Operator         | Meaning                  | Example -> Result|
# +------------------+--------------------------+------------------+
# | +                | add / concatenate        | 5 + 3  -> 8      |
# | -                | subtract                 | 5 - 3  -> 2      |
# | *                | multiply / repeat        | 5 * 3  -> 15     |
# | /                | divide (always float)    | 5 / 2  -> 2.5    |
# | //               | floor divide             | 5 // 2 -> 2      |
# | %                | remainder                | 5 % 2  -> 1      |
# | **               | power                    | 5 ** 2 -> 25     |
# | ==               | equal to                 | 5 == 5 -> True   |
# | !=               | not equal                | 5 != 3 -> True   |
# | <, >, <=, >=     | comparisons              | 5 < 3  -> False  |
# | and, or, not     | logical                  | T and F -> False |
# | += -= *= /= etc. | augmented assignment     | x += 1           |
# +------------------+--------------------------+------------------+


# ------------------------------------------------------------
# SECTION 12 - KEY TAKEAWAYS
# ------------------------------------------------------------
# 1. An expression produces a value.
# 2. "=" assigns. "==" compares. Never confuse them.
# 3. Python follows PEMDAS. Use ( ) to be clear.
# 4. / always returns float. // returns int (floor).
# 5. % gives the remainder. Great for even/odd checks.
# 6. and / or / not produce booleans.
# 7. Variable names: snake_case, meaningful, case-sensitive.
# 8. a, b = 1, 2 and a, b = b, a work in one line.
# 9. x += 5 is shorthand for x = x + 5.
# 10. "ha" * 3 gives "hahaha". + concatenates strings.


# ============================================================
# SECTION 13 - MCQ QUIZ (answer in comments below)
# ============================================================

# Q1. What does 7 // 2 evaluate to?
#     a) 3.5
#     b) 3
#     c) 4
#     d) 1
#
# YOUR ANSWER: ___

# Q2. What does 7 % 2 evaluate to?
#     a) 0
#     b) 1
#     c) 3
#     d) 3.5
#
# YOUR ANSWER: ___

# Q3. What does 2 + 3 * 4 evaluate to?
#     a) 20
#     b) 14
#     c) 24
#     d) 9
#
# YOUR ANSWER: ___

# Q4. What is the difference between = and ==?
#     a) No difference
#     b) = assigns, == compares
#     c) = compares, == assigns
#     d) Both compare
#
# YOUR ANSWER: ___

# Q5. What does 10 / 2 return?
#     a) 5
#     b) 5.0
#     c) 2
#     d) Error
#
# YOUR ANSWER: ___

# Q6. What does 2 ** 3 evaluate to?
#     a) 6
#     b) 8
#     c) 9
#     d) 5
#
# YOUR ANSWER: ___

# Q7. If x = 5, what is x after x += 3?
#     a) 3
#     b) 5
#     c) 8
#     d) 15
#
# YOUR ANSWER: ___

# Q8. What does True and False evaluate to?
#     a) True
#     b) False
#     c) Error
#     d) None
#
# YOUR ANSWER: ___

# Q9. What does "ha" * 3 evaluate to?
#     a) "hahaha"
#     b) "ha ha ha"
#     c) Error
#     d) 3
#
# YOUR ANSWER: ___

# Q10. Which variable name is INVALID?
#      a) student_name
#      b) _count
#      c) 2nd_place
#      d) totalPrice
#
# YOUR ANSWER: ___


# ============================================================
# SECTION 14 - INTERACTIVE QUIZ (runs when you execute the file)
# ============================================================

def quiz():
    questions = [
        {"q": "Q1. 7 // 2 = ?",
         "options": ["3.5", "3", "4", "1"], "answer": "3"},
        {"q": "Q2. 7 % 2 = ?",
         "options": ["0", "1", "3", "3.5"], "answer": "1"},
        {"q": "Q3. 2 + 3 * 4 = ?",
         "options": ["20", "14", "24", "9"], "answer": "14"},
        {"q": "Q4. Difference between = and == ?",
         "options": ["No difference", "= assigns, == compares",
                     "= compares, == assigns", "Both compare"],
         "answer": "= assigns, == compares"},
        {"q": "Q5. 10 / 2 = ?",
         "options": ["5", "5.0", "2", "Error"], "answer": "5.0"},
        {"q": "Q6. 2 ** 3 = ?",
         "options": ["6", "8", "9", "5"], "answer": "8"},
        {"q": "Q7. If x = 5, then x += 3 -> x = ?",
         "options": ["3", "5", "8", "15"], "answer": "8"},
        {"q": "Q8. True and False = ?",
         "options": ["True", "False", "Error", "None"], "answer": "False"},
        {"q": "Q9. 'ha' * 3 = ?",
         "options": ["'hahaha'", "'ha ha ha'", "Error", "3"], "answer": "'hahaha'"},
        {"q": "Q10. Which variable name is INVALID?",
         "options": ["student_name", "_count", "2nd_place", "totalPrice"],
         "answer": "2nd_place"},
    ]

    score = 0
    total = len(questions)

    print("\n" + "=" * 50)
    print("LESSON 1.3 - EXPRESSIONS AND VARIABLES QUIZ")
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
                print(f"Enter 1-{len(item['options'])}.")
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
        print("Perfect. Move to Lesson 1.4 - String Operations.")
    elif score >= total * 0.7:
        print("Good. Review missed questions, then move on.")
    else:
        print("Reread Sections 3-9 and retake the quiz.")
    print("=" * 50)


if __name__ == "__main__":
    quiz()


# ------------------------------------------------------------
# SECTION 15 - YOUR TO-DO
# ------------------------------------------------------------
# [ ] Run this file from the TERMINAL (not the Run button):
#       python module1_basics\1_3_expressions_variables.py
# [ ] Read every output line.
# [ ] Answer Q1-Q10 in Section 13 comments.
# [ ] Take the interactive quiz at the end.
# [ ] Reply with:
#       - Your comment answers (e.g., 1-b, 2-b, ...)
#       - Your interactive score
#       - One thing that surprised you
# [ ] Move on to Lesson 1.4 - String Operations.
# ------------------------------------------------------------
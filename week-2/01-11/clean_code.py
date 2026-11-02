# תרגילים: שמות ופונקציות קטנות

# תרגיל :1 שמות שמסבירים את עצמם
# הקוד הבא עובד, אבל אי אפשר להבין מה הוא עושה:

def f(a, b):
    c = a * b
    if c > 500:
        c = c - 50
    return c

print(f(120, 5))
print(f(30, 2))

pass_price = 500
discount = 50

def test_discount(price, quantity):
    total_price = price * quantity

    if total_price > pass_price:
        total_price -= discount
    return total_price

print(test_discount(120, 5))
print(test_discount(30, 2))

# תרגיל :2 מוסכמות השמות
# לכל שם — האם הוא כתוב לפי מוסכמות Python ?אם לא, כתבו את השם הנכון.

# TotalPrice (a variable) = total_price
# numberofstudents (a variable) = number_of_students
# max_grade (a variable) = True
# vat_rate (a constant that never changes) = VAT_RATE
# GetAverage (a function) = get_average


# תרגיל :3 פונקציה אחת — אחריות אחת
# הפונקציה הבאה מחשבת ממוצע, מחליטה אם עבר, וגם מדפיסה — שלושה תפקידים:

def report(name, grades):
    total = 0
    for g in grades:
        total = total + g
    avg = total / len(grades)
    if avg >= 55:
        print(name + ": average", avg, "- passed")
    else:
        print(name + ": average", avg, "- failed")

report("Dana", [80, 85])
report("Avi", [50, 46])


def calculate_average(grades):
    total = 0
    for g in grades:
        total = total + g
    return total / len(grades)

def is_passing(average):
    PASSING_GRADE = 55
    return average > PASSING_GRADE

def print_report(name, grades):
    average = calculate_average(grades)
    if is_passing(average):
        print(name + ": average", average, "- passed")
    else:
        print(name + ": average", average, "- failed")

print_report("Dana", [80, 85])
print_report("Avi", [50, 46])


# תרגיל :4 בלי מספרי קסם
# בחנות אונליין, הפונקציה הבאה מקבלת את סכום ההזמנה ומחזירה את הסכום לתשלום:

def final_price(total):
    if total < 200:
        total = total + 30
    return total

print(final_price(150))
print(final_price(250))

VAT_RATE = 30
TEST_NUMBER = 200

def calculate_final_price(total_price):
    if total_price < TEST_NUMBER:
        total_price += VAT_RATE
    return total_price

print(calculate_final_price(150))
print(calculate_final_price(250))


# תרגיל :5 פונקציה קטנה שעונה על שאלה אחת
# כתבו פונקציה (password(password_valid_is שמחזירה True אם הסיסמה באורך 8 תווים לפחות וגם מכילה
# לפחות ספרה אחת, אחרת False. הפונקציה לא מדפיסה — רק מחזירה

def is_valid_password(password):

    if len(password) >= 8:
        for i in password:
            if i.isdigit():
                return True

    return False

print(is_valid_password("abc12345"))
print(is_valid_password("abcdefgh"))
print(is_valid_password("a1"))





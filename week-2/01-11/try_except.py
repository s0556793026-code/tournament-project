# מצגת 09 · טיפול בשגיאות ((except / try
# תרגיל :1 המרה בטוחה למספר
def to_number(text):
    try:
        return int(text)
    except ValueError:
        return f"{text} is not a number"

print(to_number("42"))
print(to_number("hello"))
print(to_number("7"))

# תרגיל :2 טיפול שונה לכל סוג שגיאה
def safe_divide(text1, text2):
    try:
        return int(text1) / int(text2)
    except ValueError:
        return "numbers only"
    except ZeroDivisionError:
        return "cannot divide by zero"

print(safe_divide("10", "4"))
print(safe_divide("10", "0"))
print(safe_divide("ten", "2"))

# תרגיל :3 להציג את הודעת השגיאה

try:
    number = int("12abc")
except ValueError as e:
    print("Could not convert:", e)

# תרגיל :4 בחירה מרשימה

def pick(names, position_text):
    try:
        return names[int(position_text) - 1]
    except ValueError:
        return "not a number"
    except IndexError:
        return "no such position"

names = ["Dana", "Avi", "Noa"]
print(pick(names, "2"))
print(pick(names, "abc"))
print(pick(names, "9"))

# תרגיל :5 except שתופס הכול

def read_age(text):
    try:
        return int(text)
    except:
        return 0


# .1 למה :except בלי סוג שגיאה מסוכן?: כי אתה לא יודע מה לתקן
# .2 תנו דוגמה לבאג אמיתי שהקוד הזה היה מסתיר.: אם זה היה ריק
# .3הבדילו בין ValueError ל TypeError: טייפ זה אומר שיש בעיה במבנה נתונים של פייתון לדוגמא חסר סוגריים נקודתיים וכדו ערך זה אומר שיש בעיה שאני מנסה להפוך ערך למשהו שהוא לא קיים

def read_age(text):
    try:
        return int(text)
    except ValueError:
        return 0


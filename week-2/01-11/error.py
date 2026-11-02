# תרגילים: באגים ו-Stack Trace
# תרגיל :1 איזה סוג שגיאה?


# A
# if age > 18
#     print("adult") 
# B
# print(total_price) # total_price was never defined
# C
# def area(width, height):
#     return width + height # should be the area of a rectangle

# A SyntaxError חסר : על התנאי
# B Runtime Error הוא לא מוגדר
# C  Logical Error  הלוגיקה הנכונה היא רוחב כפול אורך


# Trace Stack קריאת :2 תרגיל

# 1 Runtime Error  סוג השגיאה הודעה היא ZeroDivisionError: division by zero
# 2 File "shop.py", line 3, in average_price
#return sum(prices) / count
# 3 File "shop.py", line 12, in <module>
# print(chec


# תרגיל :3 באג לוגי בהמרת טמפרטורה

def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(to_celsius(212))
print(to_celsius(32))

# TypeError :4 תרגיל

# age = 25
# print("Age: " + age)

#  TypeError היות שאין פעולות חשבון על סטרינג

age = 25
print("Age: ", age)


print("Age: " + str(age))

# תרגיל :5 ממוצע של רשימה ריקה

# def average(numbers):
#     return sum(numbers) / len(numbers)

# print(average([80, 90]))
# print(average([]))

#  מה יקרה בקריאה השנייה, ואיזו שגיאה תתקבל? =  יתקבל שגיאה שך ZeroDivisionError לא יודפס רק שגיאה
# .2 תקנו את הפונקציה כך שעבור רשימה ריקה היא תחזיר .

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(average([80, 90]))
print(average([]))



# מצגת 08 · תהליך הדיבאג ((II Debugging
# תרגיל :1 חמשת השלבים
# סדרו את שלבי הדיבאג לפי הסדר, והסבירו במשפט מה עושים בכל שלב:

# 1 Reproduce : לגרום לבאג לקרוא שוב עם קלט ידוע
# 2 Isolate : לבודד את השורה או הפונקציה שבו השגיאה דרך דיבוג 
# 3  Undorstending : לשחזר למה זה קרה שלא יקרה שוב
# 4 Fix :  תיקון לאחר ההבנה את שורש הבעיה
# 5 Verify : לאמת שאכן זה תוקן

# תרגיל :2 המקסימום שיצא 0

def find_max(numbers):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print(find_max([4, 9, 2]))
print(find_max([-7, -3, -10]))
print()
# .1 איפה הייתם שמים Breakpoint, ומה הייתם רואים בחלון ?Variables: הייתי שם מתחילת הלולאה לסופה ורואה מה קורה למשתנה שאותו אנו מחזירים שהוא נשאר 0 היות שהכל שלילי
# .2 תקנו את הבאג.

def find_maximum(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print(find_maximum([4, 9, 2]))
print(find_maximum([-7, -3, -10]))


# תרגיל :3 שגיאה לוגית בלולאה

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count = count + 1
        return count
        
print(count_vowels("banana"))
print()


def count_vowels_words(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count = count + 1
    return count
        
print(count_vowels_words("banana"))


# תרגיל :4 כלי ה-Debugger

# 1. Breakpoint: נקודה שבה ההרצה עוצרת לבדוק לשים שורה לפני השורה החשודה
# 2. Step Over: דילוג על הפונקציות ללא בדיקה
# 3. Step Into: בדיקה בתוך הפונקציות שקורות בו
# Variables חלון .4 חלון שמראה מה שווה המשתנה בכל סיבוב


# Off-by-one :5 תרגיל

def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(sum_to(5))

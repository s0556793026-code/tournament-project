
print("Bread", 8, "x", 2, "=", 8 * 2)
print("Milk", 6, "x", 3, "=", 6 * 3)
print("Eggs", 14, "x", 1, "=", 14 * 1)
print("Total:", 8 * 2 + 6 * 3 + 14 * 1)
print()
# קוד שחוזר על עצמו
# תרגיל :1 DRY — קבלה בלי העתק-הדבק

def items_order(items_details):
    total = 0

    for name, price, quantity in items_details:
        total_price = price * quantity
        print (name, price, 'x', quantity, "=", total_price)
        total += total_price

    print ("Total:", total)

items_details = [("Bread", 8, 2), ("Milk", 6, 3), ("Eggs", 14, 1)]

items_order(items_details)

# תרגיל :2 KISS — קוד "חכם" מדי

def parity(n):
    return (n % 2 == 0) * "even" + (n % 2 == 1) * "odd"

print(parity(4))
print(parity(7))
print()

def is_even(num):
    if num % 2 == 0:
        return "even"
    return "add"

print(is_even(4))
print(is_even(7))
print()

# תרגיל :3 הערות — למה, לא מה
# לכל הערה — האם היא טובה, מיותרת או מזיקה? הסבירו.

# count = count + 1 # add 1 to count = הערה לא במקום הוא מסביר מה והערה תפקידה היא להסביר למה
# 2. # 30 days: the refund policy of the shop = מסביר למה זה טוב
#REFUND_DAYS = 30
#3. total = price * 2 # multiply price by 3 = הערה לא במקום גם לא נכון זה מכפיל ב 2
# 4. # retry 3 times — the payment API sometimes fails on the first call = מסביר למה זה טוב

# תרגיל :4 הפרדת אחריות — חישוב מול קלט ופלט

def bmi():
    weight = float(input("Weight: "))
    height = float(input("Height: "))
    print("BMI:", round(weight / (height * height), 1))



def calculate_bmi(weight, height):
    return round(weight / (height * height), 1)

print(f"BMI: {calculate_bmi(70, 1.75)}")


# תרגיל :5 Refactoring בצעדים
t = 12
if t < 15:
    print(12, "cold")
elif t < 28:
    print(12, "pleasant")
else:
    print(12, "hot")
t = 24
if t < 15:
    print(24, "cold")
elif t < 28:
    print(24, "pleasant")
else:
    print(24, "hot")


def classify(temperature):
    for t in temperature:
        if t < 15:
            print(t, "cold")
        elif t < 28:
            print(t, "pleasant")
        else:
            print(t, "hot")

classify([12, 24, 33])



# ============================================
# 1-masala: Supermarket savatchasi
# ============================================
class CartItem:
    def __init__(self, name, price, quantity, discount):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def total_price(self):
        return self.price * self.quantity * (1 - self.discount / 100)


class FoodItem(CartItem):
    def total_cost(self):
        cost = self.total_price()
        return f"🍎 Oziq-ovqat: {self.name}, Jami: {cost:.2f} so'm"


class NonFoodItem(CartItem):
    def total_cost(self):
        cost = self.total_price()
        return f"📦 Nooziq-ovqat: {self.name}, Jami: {cost:.2f} so'm"


items = [
    FoodItem("Olma", 15000, 3, 10),
    FoodItem("Non", 4000, 2, 0),
    NonFoodItem("Sovun", 8000, 5, 5)
]

print("=" * 40)
print("  SUPERMARKET SAVATCHASI")
print("=" * 40)
total_sum = 0
for item in items:
    print(item.total_cost())
    total_sum += item.total_price()
print(f"\n💰 Jami savat narxi: {total_sum:.2f} so'm\n")


# ============================================
# 2-masala: Transport xarajatlari
# ============================================
class Vehicle:
    def __init__(self, name, distance, fuel_per_km, fuel_price):
        self.name = name
        self.distance = distance
        self.fuel_per_km = fuel_per_km
        self.fuel_price = fuel_price

    def trip_cost(self):
        return self.distance * self.fuel_per_km * self.fuel_price


class Car(Vehicle):
    def trip_cost(self):
        cost = super().trip_cost()
        return f"🚗 Avtomobil: {self.name}, Safar narxi: {cost:.2f} so'm"


class Motorcycle(Vehicle):
    def trip_cost(self):
        cost = super().trip_cost()
        return f"🏍️ Motosikl: {self.name}, Safar narxi: {cost:.2f} so'm"


vehicles = [
    Car("Toyota", 150, 0.1, 12000),
    Motorcycle("Yamaha", 100, 0.05, 12000)
]

print("=" * 40)
print("  TRANSPORT XARAJATLARI")
print("=" * 40)
for v in vehicles:
    print(v.trip_cost())
print()


# ============================================
# 3-masala: Uy hayvonlari ovqatlanishi
# ============================================
class Pet:
    def __init__(self, name, daily_food):
        self.name = name
        self.daily_food = daily_food

    def feeding_plan(self, days):
        return self.daily_food * days


class Dog(Pet):
    def feeding_plan(self, days):
        food = super().feeding_plan(days)
        return f"🐕 It: {self.name}, {days} kunlik ovqat: {food} gramm"


class Cat(Pet):
    def feeding_plan(self, days):
        food = super().feeding_plan(days)
        return f"🐈 Mushuk: {self.name}, {days} kunlik ovqat: {food} gramm"


pets = [Dog("Rex", 300), Cat("Murka", 150)]
print("=" * 40)
print("  UY HAYVONLARI OVQATLANISHI")
print("=" * 40)
for pet in pets:
    print(pet.feeding_plan(7))
print()


# ============================================
# 4-masala: Restoran buyurtmalari
# ============================================
class Order:
    def __init__(self, name, price, service_fee_percent):
        self.dish_name = name
        self.price = price
        self.service_fee_percent = service_fee_percent

    def total_cost(self):
        return self.price * (1 + self.service_fee_percent / 100)


class MainDish(Order):
    def total_cost(self):
        cost = super().total_cost()
        return f"🍽️ Asosiy taom: {self.dish_name}, Jami: {cost:.2f} so'm"


class SideDish(Order):
    def total_cost(self):
        cost = super().total_cost()
        return f"🥗 Qo'shimcha taom: {self.dish_name}, Jami: {cost:.2f} so'm"


orders = [MainDish("Lavash", 35000, 10), SideDish("Salat", 15000, 5)]
print("=" * 40)
print("  RESTORAN BUYURTMALARI")
print("=" * 40)
for o in orders:
    print(o.total_cost())
print()


# ============================================
# 5-masala: O‘quvchilarning baholari
# ============================================
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def get_average(self):
        return sum(self.grades) / len(self.grades)


class HighSchoolStudent(Student):
    def average_grade(self):
        avg = self.get_average()
        return f"🏫 Maktab o'quvchisi: {self.name}, O'rtacha baho: {avg:.1f}"


class CollegeStudent(Student):
    def average_grade(self):
        avg = self.get_average()
        return f"🎓 Kollej talabasi: {self.name}, O'rtacha baho: {avg:.1f}"


students = [
    HighSchoolStudent("Ali", [85, 90, 78, 92]),
    CollegeStudent("Vali", [88, 76, 95, 89])
]
print("=" * 40)
print("  O'QUVCHILAR BAHOLARI")
print("=" * 40)
for s in students:
    print(s.average_grade())
print()


# ============================================
# 6-masala: Kitob ijarasi
# ============================================
class BookRental:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def is_overdue(self, current_date):
        return self.due_date < current_date


class FictionBook(BookRental):
    def overdue_status(self, current_date):
        overdue = self.is_overdue(current_date)
        status = "❌ Kechikkan" if overdue else "✅ Vaqtida"
        return f"📚 Badiiy kitob: {self.title}, Holati: {status}"


class NonFictionBook(BookRental):
    def overdue_status(self, current_date):
        overdue = self.is_overdue(current_date)
        status = "❌ Kechikkan" if overdue else "✅ Vaqtida"
        return f"📖 Ilmiy kitob: {self.title}, Holati: {status}"


books = [
    FictionBook("Alchemist", "2024-06-01"),
    NonFictionBook("Sapiens", "2025-02-01")
]
curr_date = "2025-02-10"
print("=" * 40)
print("  KITOB IJARASI HOLATI")
print("=" * 40)
for b in books:
    print(b.overdue_status(curr_date))
print()


# ============================================
# 7-masala: Kommunal xarajatlar
# ============================================
class Utility:
    def __init__(self, u_type, amount, rate):
        self.u_type = u_type
        self.amount = amount
        self.rate = rate

    def calculate_cost(self):
        return self.amount * self.rate


class Electricity(Utility):
    def total_cost(self):
        cost = self.calculate_cost()
        return f"⚡ Elektr ({self.u_type}): {cost:.2f} so'm"


class Water(Utility):
    def total_cost(self):
        cost = self.calculate_cost()
        return f"💧 Suv ({self.u_type}): {cost:.2f} so'm"


utilities = [Electricity("Xonadon", 350, 450), Water("Xonadon", 25, 1200)]
print("=" * 40)
print("  KOMMUNAL XARAJATLARI")
print("=" * 40)
for u in utilities:
    print(u.total_cost())
print()


# ============================================
# 8-masala: Fitness mashqlari
# ============================================
class Exercise:
    def __init__(self, name, duration, cal_per_min):
        self.name = name
        self.duration = duration
        self.cal_per_min = cal_per_min

    def total_calories(self):
        return self.duration * self.cal_per_min


class CardioExercise(Exercise):
    def calories_info(self):
        cal = self.total_calories()
        return f"🏃 Kardio: {self.name}, Sarflandi: {cal} kcal"


class StrengthExercise(Exercise):
    def calories_info(self):
        cal = self.total_calories()
        return f"💪 Kuch mashqi: {self.name}, Sarflandi: {cal} kcal"


exercises = [CardioExercise("Yugurish", 30, 10), StrengthExercise("Turnik", 20, 8)]
print("=" * 40)
print("  FITNESS MASHQLARI")
print("=" * 40)
for e in exercises:
    print(e.calories_info())
print()


# ============================================
# 9-masala: Ta’til rejalashtiruvchisi
# ============================================
class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def get_info(self):
        return f"{self.category}: ${self.amount}"


class TransportExpense(Expense):
    def get_info(self):
        return f"✈️ Transport ({self.category}): ${self.amount}"


class AccommodationExpense(Expense):
    def get_info(self):
        return f"🏨 Yashash ({self.category}): ${self.amount}"


trip_expenses = [TransportExpense("Aviabilet", 500), AccommodationExpense("Mehmonxona", 300)]
print("=" * 40)
print("  TA'TIL XARAJATLARI")
print("=" * 40)
for exp in trip_expenses:
    print(exp.get_info())
print()


# ============================================
# 10-masala: Telefon tariflari
# ============================================
class PhonePlan:
    def __init__(self, name, minutes, sms, min_rate, sms_rate):
        self.name = name
        self.minutes = minutes
        self.sms = sms
        self.min_rate = min_rate
        self.sms_rate = sms_rate

    def total_cost(self):
        return (self.minutes * self.min_rate) + (self.sms * self.sms_rate)


class StandardPlan(PhonePlan):
    def get_summary(self):
        cost = self.total_cost()
        return f"📱 Standart tarif ({self.name}): ${cost:.2f}"


class PremiumPlan(PhonePlan):
    def get_summary(self):
        cost = self.total_cost()
        return f"👑 Premium tarif ({self.name}): ${cost:.2f}"


plans = [StandardPlan("Ekonom", 100, 50, 0.1, 0.05), PremiumPlan("VIP", 500, 200, 0.05, 0.02)]
print("=" * 40)
print("  TELEFON TARIFLARI")
print("=" * 40)
for p in plans:
    print(p.get_summary())
print()


# ============================================
# 11-masala: Bog‘dorchilik rejasi
# ============================================
class Plant:
    def __init__(self, name, water_liters):
        self.name = name
        self.water_liters = water_liters


class Flower(Plant):
    def watering_plan(self):
        return f"🌸 Gul: {self.name}, Suv: {self.water_liters}L"


class Tree(Plant):
    def watering_plan(self):
        return f"🌳 Daraxt: {self.name}, Suv: {self.water_liters}L"


garden = [Flower("Atirgul", 2), Tree("Archa", 10)]
print("=" * 40)
print("  BOG'DORCHILIK REJASI")
print("=" * 40)
for p in garden:
    print(p.watering_plan())
print()


# ============================================
# 12-masala: Ish haqi hisoblash
# ============================================
class Employee:
    def __init__(self, name, hourly_rate, hours):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_base_salary(self):
        return self.hourly_rate * self.hours


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        salary = self.calculate_base_salary()
        if self.hours > 40:
            salary += (self.hours - 40) * self.hourly_rate * 0.5
        return f"👔 Full-time: {self.name}, Maosh: ${salary:.2f}"


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        salary = self.calculate_base_salary()
        return f"🕒 Part-time: {self.name}, Maosh: ${salary:.2f}"


staff = [FullTimeEmployee("Ali", 25, 45), PartTimeEmployee("Vali", 20, 30)]
print("=" * 40)
print("  ISH HAQI HISOB-KITOBI")
print("=" * 40)
for s in staff:
    print(s.calculate_salary())
print()


# ============================================
# 13-masala: Internet tezligi
# ============================================
class InternetTest:
    def __init__(self, mode, download, upload):
        self.mode = mode
        self.download = download
        self.upload = upload

    def get_average(self):
        return (self.download + self.upload) / 2


class WiFiTest(InternetTest):
    def report(self):
        avg = self.get_average()
        return f"📶 WiFi ({self.mode}): O'rtacha {avg} Mbps"


class MobileTest(InternetTest):
    def report(self):
        avg = self.get_average()
        return f"📲 4G ({self.mode}): O'rtacha {avg} Mbps"


speed_tests = [WiFiTest("Uy", 50, 20), MobileTest("Ko'cha", 30, 15)]
print("=" * 40)
print("  INTERNET TEZLIGI TESTI")
print("=" * 40)
for t in speed_tests:
    print(t.report())
print()


# ============================================
# 14-masala: Oziq-ovqat yetkazib berish
# ============================================
class Delivery:
    def __init__(self, item, price, dist, rate_per_km):
        self.item = item
        self.price = price
        self.dist = dist
        self.rate_per_km = rate_per_km

    def calculate_total(self):
        return self.price + (self.dist * self.rate_per_km)


class FoodDelivery(Delivery):
    def info(self):
        total = self.calculate_total()
        return f"🥡 Taom: {self.item}, Jami: {total} so'm"


class GroceryDelivery(Delivery):
    def info(self):
        total = self.calculate_total()
        return f"🛒 Savdo: {self.item}, Jami: {total} so'm"


deliveries = [FoodDelivery("Pitsa", 70000, 5, 2000), GroceryDelivery("Sut/Mevalar", 50000, 3, 1500)]
print("=" * 40)
print("  YETKAZIB BERISH XIDMATI")
print("=" * 40)
for d in deliveries:
    print(d.info())
print()


# ============================================
# 15-masala: Uxlash vaqti kuzatuvchisi
# ============================================
class SleepTracker:
    def __init__(self, name, hours_list):
        self.name = name
        self.hours_list = hours_list

    def get_average(self):
        return sum(self.hours_list) / len(self.hours_list)


class DaySleep(SleepTracker):
    def report(self):
        avg = self.get_average()
        return f"☀️ Kunduzgi ({self.name}): o'rtacha {avg:.1f} soat"


class NightSleep(SleepTracker):
    def report(self):
        avg = self.get_average()
        return f"🌙 Tungi ({self.name}): o'rtacha {avg:.1f} soat"


sleeps = [DaySleep("Dushanba", [1, 1.5]), NightSleep("Haftalik", [7, 8, 6, 7.5, 8])]
print("=" * 40)
print("  UXLASH VAQTI KUZATUVCHISI")
print("=" * 40)
for s in sleeps:
    print(s.report())
print()


# ============================================
# 16-masala: Budjet rejalashtiruvchisi
# ============================================
class Budget:
    def __init__(self, b_type, total, expenses):
        self.b_type = b_type
        self.total = total
        self.expenses = expenses

    def get_remaining(self):
        return self.total - sum(self.expenses)


class FamilyBudget(Budget):
    def summary(self):
        rem = self.get_remaining()
        return f"👨‍👩‍👧‍👦 Oila budjeti ({self.b_type}): Qoldiq ${rem}"


class PersonalBudget(Budget):
    def summary(self):
        rem = self.get_remaining()
        return f"👤 Shaxsiy budjet ({self.b_type}): Qoldiq ${rem}"


budgets = [FamilyBudget("Fevral", 2000, [500, 300, 200]), PersonalBudget("Talaba", 500, [100, 150])]
print("=" * 40)
print("  BUDJET REJALASHTIRUVCHISI")
print("=" * 40)
for b in budgets:
    print(b.summary())
print()

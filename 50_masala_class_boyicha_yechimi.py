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
print("  KOMMUNAL XARAJATLAR")
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


# ============================================
# 17-masala: Sport musobaqasi
# ============================================
class Competitor:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_result(self):
        return f"{self.name}: {self.score} ball"


class Runner(Competitor):
    def get_result(self):
        return f"🏃 Yuguruvchi {self.name} - natija: {self.score} ball"


class Swimmer(Competitor):
    def get_result(self):
        return f"🏊 Suzuvchi {self.name} - natija: {self.score} ball"


runner1 = Runner("Ali", 85)
runner2 = Runner("Jasur", 92)
swimmer1 = Swimmer("Vali", 90)
swimmer2 = Swimmer("Sardor", 88)

print("=" * 40)
print("  SPORT MUSOBAQASI NATIJALARI")
print("=" * 40)
print(runner1.get_result())
print(runner2.get_result())
print(swimmer1.get_result())
print(swimmer2.get_result())
print()


# ============================================
# 18-masala: Xona harorati
# ============================================
class Room:
    def __init__(self, room_type, temperatures):
        self.room_type = room_type
        self.temperatures = temperatures

    def average_temperature(self):
        avg = sum(self.temperatures) / len(self.temperatures)
        return f"{self.room_type}: o'rtacha harorat {avg:.1f}°C"


class Bedroom(Room):
    def average_temperature(self):
        avg = sum(self.temperatures) / len(self.temperatures)
        return f"🛏️ Yotoqxona ({self.room_type}): o'rtacha harorat {avg:.1f}°C"


class Kitchen(Room):
    def average_temperature(self):
        avg = sum(self.temperatures) / len(self.temperatures)
        return f"🍳 Oshxona ({self.room_type}): o'rtacha harorat {avg:.1f}°C"


bedroom1 = Bedroom("Yotoqxona", [22.5, 23.0, 22.8])
kitchen1 = Kitchen("Oshxona", [21.0, 22.0, 23.5])

print("=" * 40)
print("  XONA HARORATI MONITORING")
print("=" * 40)
print(bedroom1.average_temperature())
print(kitchen1.average_temperature())
print()


# ============================================
# 19-masala: Kafe buyurtmalari
# ============================================
class CafeOrder:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def order_summary(self):
        return f"{self.name}: {self.quantity} dona"


class HotDrink(CafeOrder):
    def order_summary(self):
        return f"☕ Issiq ichimlik - {self.name}: {self.quantity} dona"


class ColdDrink(CafeOrder):
    def order_summary(self):
        return f"🧊 Sovuq ichimlik - {self.name}: {self.quantity} dona"


order1 = HotDrink("Kofe", 5)
order2 = HotDrink("Choy", 3)
order3 = ColdDrink("Mojito", 4)
order4 = ColdDrink("Limonad", 6)

buyurtmalar = [order1, order2, order3, order4]

print("=" * 40)
print("  KAFE BUYURTMALARI")
print("=" * 40)
for buyurtma in buyurtmalar:
    print(buyurtma.order_summary())

eng_kop = max(buyurtmalar, key=lambda x: x.quantity)
print(f"\n🏆 Eng ko'p buyurtma: {eng_kop.name} ({eng_kop.quantity} dona)")
print()


# ============================================
# 20-masala: Mashq rejalashtiruvchisi
# ============================================
class Workout:
    def __init__(self, workout_type, duration):
        self.workout_type = workout_type
        self.duration = duration

    def total_time(self):
        return f"{self.workout_type}: {self.duration} daqiqa"


class Cardio(Workout):
    def total_time(self):
        return f"🏃 Kardio - {self.workout_type}: {self.duration} daqiqa"


class YogaWorkout(Workout):
    def total_time(self):
        return f"🧘 Yoga - {self.workout_type}: {self.duration} daqiqa"


mashq1 = Cardio("Yugurish", 60)
mashq2 = Cardio("Velosiped", 45)
mashq3 = YogaWorkout("Ertalabki yoga", 30)
mashq4 = YogaWorkout("Kechki yoga", 45)

mashqlar = [mashq1, mashq2, mashq3, mashq4]

print("=" * 40)
print("  HAFTALIK MASHQ REJASI")
print("=" * 40)
for mashq in mashqlar:
    print(mashq.total_time())

umumiy = sum(m.duration for m in mashqlar)
print(f"\n⏱️ Umumiy mashq vaqti: {umumiy} daqiqa")
print()


# ============================================
# 21-masala: Elektr avtomobil zaryadlash
# ============================================
class EV:
    def __init__(self, model, kwh, rate):
        self.model = model
        self.kwh = kwh
        self.rate = rate

    def charging_cost(self):
        cost = self.kwh * self.rate
        return f"{self.model}: {cost:.2f} $"


class Tesla(EV):
    def charging_cost(self):
        cost = self.kwh * self.rate
        return f"🚗 Tesla {self.model} - zaryadlash narxi: {cost:.2f} $"


class Nissan(EV):
    def charging_cost(self):
        cost = self.kwh * self.rate
        return f"🚙 Nissan {self.model} - zaryadlash narxi: {cost:.2f} $"


tesla1 = Tesla("Model 3", 50, 0.15)
tesla2 = Tesla("Model S", 75, 0.15)
nissan1 = Nissan("Leaf", 40, 0.15)
nissan2 = Nissan("Ariya", 65, 0.15)

avtomobillar = [tesla1, tesla2, nissan1, nissan2]

print("=" * 40)
print("  ELEKTR AVTOMOBIL ZARYADLASH")
print("=" * 40)
for avto in avtomobillar:
    print(avto.charging_cost())
print()


# ============================================
# 22-masala: O'quv jadvali
# ============================================
class Schedule:
    def __init__(self, subject, hours):
        self.subject = subject
        self.hours = hours

    def total_hours(self):
        return f"{self.subject}: {self.hours} soat"


class MathSchedule(Schedule):
    def total_hours(self):
        return f"📐 Matematika - {self.subject}: {self.hours} soat"


class PhysicsSchedule(Schedule):
    def total_hours(self):
        return f"⚛️ Fizika - {self.subject}: {self.hours} soat"


math1 = MathSchedule("Algebra", 3)
math2 = MathSchedule("Geometriya", 2)
physics1 = PhysicsSchedule("Mexanika", 2)
physics2 = PhysicsSchedule("Optika", 1)

jadval = [math1, math2, physics1, physics2]

print("=" * 40)
print("  HAFTALIK O'QUV JADVALI")
print("=" * 40)
for dars in jadval:
    print(dars.total_hours())

umumiy_soat = sum(d.hours for d in jadval)
print(f"\n📚 Umumiy dars soatlari: {umumiy_soat} soat")
print()


# ============================================
# 23-masala: Parkovka xarajatlari
# ============================================
class Parking:
    def __init__(self, parking_type, hourly_rate, hours):
        self.parking_type = parking_type
        self.hourly_rate = hourly_rate
        self.hours = hours

    def total_cost(self):
        cost = self.hourly_rate * self.hours
        return f"{self.parking_type}: {cost} $"


class StreetParking(Parking):
    def total_cost(self):
        cost = self.hourly_rate * self.hours
        return f"🅿️ Ko'cha parkovka - {self.parking_type}: {cost} $ ({self.hours} soat)"


class GarageParking(Parking):
    def total_cost(self):
        cost = self.hourly_rate * self.hours
        return f"🏢 Garaj parkovka - {self.parking_type}: {cost} $ ({self.hours} soat)"


park1 = StreetParking("Ko'cha A", 5, 3)
park2 = StreetParking("Ko'cha B", 4, 2)
park3 = GarageParking("Garaj 1", 7, 2)
park4 = GarageParking("Garaj 2", 8, 4)

parkovkalar = [park1, park2, park3, park4]

print("=" * 40)
print("  PARKOVKA XARAJATLARI")
print("=" * 40)
for park in parkovkalar:
    print(park.total_cost())

umumiy_park = sum(p.hourly_rate * p.hours for p in parkovkalar)
print(f"\n💰 Umumiy parkovka xarajati: {umumiy_park} $")
print()


# ============================================
# 24-masala: Oziq-ovqat xarajatlari
# ============================================
class Grocery:
    def __init__(self, grocery_type, cost):
        self.grocery_type = grocery_type
        self.cost = cost

    def get_cost(self):
        return f"{self.grocery_type}: {self.cost} $"


class Meat(Grocery):
    def get_cost(self):
        return f"🥩 Go'sht - {self.grocery_type}: {self.cost} $"


class Dairy(Grocery):
    def get_cost(self):
        return f"🥛 Sut mahsuloti - {self.grocery_type}: {self.cost} $"


meat1 = Meat("Mol go'shti", 15)
meat2 = Meat("Tovuq go'shti", 8)
dairy1 = Dairy("Sut", 3)
dairy2 = Dairy("Pishloq", 6)

mahsulotlar = [meat1, meat2, dairy1, dairy2]

print("=" * 40)
print("  HAFTALIK OZIQ-OVQAT XARAJATLARI")
print("=" * 40)
for mahsulot in mahsulotlar:
    print(mahsulot.get_cost())

umumiy_xarajat = sum(m.cost for m in mahsulotlar)
print(f"\n🛒 Umumiy xarajat: {umumiy_xarajat} $")
print()


# ============================================
# 25-masala: Yo'l harakati tezligi
# ============================================
class Traffic:
    def __init__(self, traffic_type, speeds):
        self.type = traffic_type
        self.speeds = speeds

    def average_speed(self):
        return sum(self.speeds) / len(self.speeds)


class CityTraffic(Traffic):
    def average_speed(self):
        avg = super().average_speed()
        return f"🏙️ Shahar ichi ({self.type}): o'rtacha tezlik {avg:.1f} km/soat"


class HighwayTraffic(Traffic):
    def average_speed(self):
        avg = super().average_speed()
        return f"🛣️ Tashqarida ({self.type}): o'rtacha tezlik {avg:.1f} km/soat"


t1 = CityTraffic("Markaz", [60, 70, 55])
t2 = HighwayTraffic("Magistral", [80, 90, 100])

print("=" * 40)
print("  YO'L HARAKATI TEZLIGI")
print("=" * 40)
print(t1.average_speed())
print(t2.average_speed())
print()


# ============================================
# 26-masala: Oziq-ovqat tayyorlash
# ============================================
class Recipe:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def total_time(self):
        return self.time


class MainCourse(Recipe):
    def total_time(self):
        t = super().total_time()
        return f"🍲 Asosiy taom - {self.name}: {t} daqiqa"


class SideDishRecipe(Recipe):
    def total_time(self):
        t = super().total_time()
        return f"🥗 Salat/Garnir - {self.name}: {t} daqiqa"


r1 = MainCourse("Osh", 60)
r2 = SideDishRecipe("Salat", 15)

print("=" * 40)
print("  OZIQ-OVQAT TAYYORLASH VAQTI")
print("=" * 40)
print(r1.total_time())
print(r2.total_time())

jami_vaqt = r1.time + r2.time
print(f"\n⏱️ Jami tayyorlash vaqti: {jami_vaqt} daqiqa")
print()


# ============================================
# 27-masala: Sport zali og'irliklari
# ============================================
class GymEquipment:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def total_weight(self):
        return self.weight


class Barbell(GymEquipment):
    def total_weight(self):
        w = super().total_weight()
        return f"🏋️ Shtanga ({self.name}): {w} kg"


class Dumbbell(GymEquipment):
    def total_weight(self):
        w = super().total_weight()
        return f"💪 Gantel ({self.name}): {w} kg"


e1 = Barbell("Asosiy", 50)
e2 = Dumbbell("Kichik", 20)

print("=" * 40)
print("  SPORT ZALI OG'IRLIKLARI")
print("=" * 40)
print(e1.total_weight())
print(e2.total_weight())

jami_ogirlik = e1.weight + e2.weight
print(f"\n⚖️ Jami og'irlik: {jami_ogirlik} kg")
print()


# ============================================
# 28-masala: Sayohat marshrutlari
# ============================================
class Route:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def get_distance(self):
        return self.distance


class CityRoute(Route):
    def get_distance(self):
        d = super().get_distance()
        return f"🏙️ Shahar yo'li ({self.name}): {d} km"


class CountryRoute(Route):
    def get_distance(self):
        d = super().get_distance()
        return f"🌄 Tashqari yo'li ({self.name}): {d} km"


m1 = CityRoute("A yo'li", 100)
m2 = CountryRoute("B yo'li", 80)

print("=" * 40)
print("  SAYOHAT MARSHRUTLARI")
print("=" * 40)
print(m1.get_distance())
print(m2.get_distance())

eng_qisqa = m1 if m1.distance < m2.distance else m2
print(f"\n📍 Eng qisqa masofa: {eng_qisqa.name} ({eng_qisqa.distance} km)")
print()


# ============================================
# 29-masala: Uy ishlari
# ============================================
class Chore:
    def __init__(self, task, done):
        self.task = task
        self.done = done

    def is_pending(self):
        return not self.done


class CleaningChore(Chore):
    def is_pending(self):
        pending = super().is_pending()
        status = "⏳ Bajarilmagan" if pending else "✅ Bajarilgan"
        return f"🧹 Tozalash: {self.task} - Holati: {status}"


class CookingChore(Chore):
    def is_pending(self):
        pending = super().is_pending()
        status = "⏳ Bajarilmagan" if pending else "✅ Bajarilgan"
        return f"🍳 Ovqat pishirish: {self.task} - Holati: {status}"


chores = [CleaningChore("Supurish", False), CookingChore("Yuvish", True)]
print("=" * 40)
print("  UY ISHLARI")
print("=" * 40)
for chore in chores:
    print(chore.is_pending())
print()


# ============================================
# 30-masala: Kitob o'qish
# ============================================
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def total_pages(self):
        return self.pages


class FictionBookReading(Book):
    def total_pages(self):
        p = super().total_pages()
        return f"📚 Badiiy kitob - {self.title}: {p} sahifa"


class NonFictionBookReading(Book):
    def total_pages(self):
        p = super().total_pages()
        return f"📖 Ilmiy kitob - {self.title}: {p} sahifa"


books_read = [FictionBookReading("Python", 300), NonFictionBookReading("AI", 200)]
print("=" * 40)
print("  O'QILGAN KITOB SAHIFALARI")
print("=" * 40)
for b in books_read:
    print(b.total_pages())

jami_sahifa = sum(b.pages for b in books_read)
print(f"\n📑 Jami o'qilgan sahifalar: {jami_sahifa}")
print()


# ============================================
# 31-masala: Onlayn kurslar
# ============================================
class Course:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def total_hours(self):
        return self.hours


class ProgrammingCourse(Course):
    def total_hours(self):
        h = super().total_hours()
        return f"💻 Dasturlash - {self.name}: {h} soat"


class DesignCourse(Course):
    def total_hours(self):
        h = super().total_hours()
        return f"🎨 Dizayn - {self.name}: {h} soat"


courses = [ProgrammingCourse("Python Dasturlash", 40), DesignCourse("UI/UX Dizayn", 30)]
print("=" * 40)
print("  ONLAYN KURSLAR DAVOMIYLIGI")
print("=" * 40)
for c in courses:
    print(c.total_hours())

jami_soat = sum(c.hours for c in courses)
print(f"\n🎓 Jami o'quv soatlari: {jami_soat} soat")
print()


# ============================================
# 32-masala: Supermarket inventarizatsiyasi
# ============================================
class Inventory:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def check_stock(self):
        return self.stock


class FoodInventory(Inventory):
    def check_stock(self):
        s = super().check_stock()
        return f"🍎 Oziq-ovqat - {self.name}: {s} dona qoldi"


class NonFoodInventory(Inventory):
    def check_stock(self):
        s = super().check_stock()
        return f"📦 Nooziq-ovqat - {self.name}: {s} dona qoldi"


stock_items = [FoodInventory("Olma", 100), NonFoodInventory("Sovun", 50)]
print("=" * 40)
print("  SUPERMARKET INVENTARIZATSIYASI")
print("=" * 40)
for item in stock_items:
    print(item.check_stock())
print()


# ============================================
# 33-masala: Tibbiy yozuvlar
# ============================================
class MedicalRecord:
    def __init__(self, patient, record_type):
        self.patient = patient
        self.record_type = record_type

    def get_record(self):
        return self.record_type


class LabRecord(MedicalRecord):
    def get_record(self):
        r = super().get_record()
        return f"🧪 Tahlil natijasi - {self.patient}: {r}"


class DiagnosisRecord(MedicalRecord):
    def get_record(self):
        r = super().get_record()
        return f"📋 Tashxis - {self.patient}: {r}"


medical_records = [LabRecord("Ali", "Tahlil"), DiagnosisRecord("Vali", "Tashxis")]
print("=" * 40)
print("  TIBBIY YOZUVLAR")
print("=" * 40)
for rec in medical_records:
    print(rec.get_record())
print()


# ============================================
# 34-masala: Do'kon chegirmalari
# ============================================
class Discount:
    def __init__(self, name, price, discount_percent):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def final_price(self):
        return self.price * (1 - self.discount_percent / 100)


class SaleDiscount(Discount):
    def final_price(self):
        p = super().final_price()
        return f"🔥 Aksiyadagi mahsulot ({self.name}): {p:.2f} $ (-{self.discount_percent}%)"


class RegularDiscount(Discount):
    def final_price(self):
        p = super().final_price()
        return f"🏷️ Oddiy chegirma ({self.name}): {p:.2f} $ (-{self.discount_percent}%)"


discounts = [SaleDiscount("Kiyim", 50, 20), RegularDiscount("Elektronika", 100, 10)]
print("=" * 40)
print("  DO'KON CHEGIRMALARI")
print("=" * 40)
for d in discounts:
    print(d.final_price())
print()


# ============================================
# 35-masala: Transport yo'nalishlari
# ============================================
class TransportRoute:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def get_distance(self):
        return self.distance


class BusRoute(TransportRoute):
    def get_distance(self):
        d = super().get_distance()
        return f"🚌 Avtobus yo'nalishi ({self.name}): {d} km"


class MetroRoute(TransportRoute):
    def get_distance(self):
        d = super().get_distance()
        return f"🚇 Metro yo'nalishi ({self.name}): {d} km"


routes = [BusRoute("14-yo'nalish", 15), MetroRoute("Chilanzar", 10)]
print("=" * 40)
print("  TRANSPORT YO'NALISHLARI")
print("=" * 40)
for r in routes:
    print(r.get_distance())
print()


# ============================================
# 36-masala: Onlayn do'kon savati
# ============================================
class Cart:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity


class ElectronicsCart(Cart):
    def total_cost(self):
        cost = super().total_cost()
        return f"💻 Elektronika ({self.name}): {cost:.2f} $ ({self.quantity} dona)"


class ClothingCart(Cart):
    def total_cost(self):
        cost = super().total_cost()
        return f"👕 Kiyim-kechak ({self.name}): {cost:.2f} $ ({self.quantity} dona)"


cart_items = [ElectronicsCart("Telefon", 500, 2), ClothingCart("Ko'ylak", 30, 3)]
print("=" * 40)
print("  ONLAYN DO'KON SAVATI")
print("=" * 40)
for item in cart_items:
    print(item.total_cost())

jami_savat = sum(i.price * i.quantity for i in cart_items)
print(f"\n🛒 Savatning umumiy narxi: {jami_savat:.2f} $")
print()


# ============================================
# 37-masala: Fitness kaloriya kuzatuvchisi
# ============================================
class FitnessTracker:
    def __init__(self, workout_type, duration, calories_per_min):
        self.type = workout_type
        self.duration = duration
        self.calories_per_min = calories_per_min

    def total_calories(self):
        return self.duration * self.calories_per_min


class RunningTracker(FitnessTracker):
    def total_calories(self):
        cal = super().total_calories()
        return f"🏃 Yugurish ({self.type}): {cal} kcal ({self.duration} daqiqa)"


class SwimmingTracker(FitnessTracker):
    def total_calories(self):
        cal = super().total_calories()
        return f"🏊 Suzish ({self.type}): {cal} kcal ({self.duration} daqiqa)"


workouts = [RunningTracker("Yengil", 30, 10), SwimmingTracker("Hovuz", 20, 12)]
print("=" * 40)
print("  FITNESS KALORIYA KUZATUVCHISI")
print("=" * 40)
for w in workouts:
    print(w.total_calories())
print()


# ============================================
# 38-masala: Kino chiptalari
# ============================================
class Ticket:
    def __init__(self, ticket_type, price):
        self.type = ticket_type
        self.price = price

    def get_price(self):
        return self.price


class AdultTicket(Ticket):
    def get_price(self):
        p = super().get_price()
        return f"👨 Katta yoshdagilar ({self.type}): {p} $"


class ChildTicket(Ticket):
    def get_price(self):
        p = super().get_price()
        return f"👶 Bolalar uchun ({self.type}): {p} $"


tickets = [AdultTicket("Kattalar", 10), ChildTicket("Bolalar", 5)]
print("=" * 40)
print("  KINO CHIPTALARI")
print("=" * 40)
for t in tickets:
    print(t.get_price())
print()


# ============================================
# 39-masala: Uy hayvonlari parvarishi
# ============================================
class PetCare:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def get_cost(self):
        return self.cost


class DogCare(PetCare):
    def get_cost(self):
        c = super().get_cost()
        return f"🐕 It parvarishi ({self.name}): {c} $"


class CatCare(PetCare):
    def get_cost(self):
        c = super().get_cost()
        return f"🐈 Mushuk parvarishi ({self.name}): {c} $"


pet_activities = [DogCare("It", 50), CatCare("Mushuk", 30)]
print("=" * 40)
print("  UY HAYVONLARI PARVARISHI")
print("=" * 40)
for act in pet_activities:
    print(act.get_cost())
print()


# ============================================
# 40-masala: Ta'til xarajatlari
# ============================================
class VacationExpense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def get_cost(self):
        return self.amount


class TransportExpenseVacation(VacationExpense):
    def get_cost(self):
        a = super().get_cost()
        return f"✈️ Transport ({self.category}): {a} $"


class FoodExpenseVacation(VacationExpense):
    def get_cost(self):
        a = super().get_cost()
        return f"🍴 Ovqatlanish ({self.category}): {a} $"


v_expenses = [TransportExpenseVacation("Transport", 200), FoodExpenseVacation("Ovqatlanish", 100)]
print("=" * 40)
print("  TA'TIL XARAJATLARI")
print("=" * 40)
for exp in v_expenses:
    print(exp.get_cost())

jami_tatil = sum(e.amount for e in v_expenses)
print(f"\n🏖️ Jami ta'til xarajatlari: {jami_tatil} $")
print()


# ============================================
# 41-masala: Sport zali a'zoligi
# ============================================
class Membership:
    def __init__(self, m_type, price):
        self.type = m_type
        self.price = price

    def get_price(self):
        return self.price


class BasicMembership(Membership):
    def get_price(self):
        p = super().get_price()
        return f"🎟️ Oddiy a'zolik ({self.type}): {p} $"


class PremiumMembership(Membership):
    def get_price(self):
        p = super().get_price()
        return f"👑 Premium a'zolik ({self.type}): {p} $"


memberships = [BasicMembership("30 kun", 30), PremiumMembership("30 kun VIP", 50)]
print("=" * 40)
print("  SPORT ZALI A'ZOLIGI")
print("=" * 40)
for m in memberships:
    print(m.get_price())
print()


# ============================================
# 42-masala: Uy isitish tizimi
# ============================================
class HeatingSystem:
    def __init__(self, h_type, consumption, rate):
        self.type = h_type
        self.consumption = consumption
        self.rate = rate

    def total_cost(self):
        return self.consumption * self.rate


class GasHeating(HeatingSystem):
    def total_cost(self):
        cost = super().total_cost()
        return f"🔥 Gaz isitish ({self.type}): {cost:.2f} $"


class ElectricHeating(HeatingSystem):
    def total_cost(self):
        cost = super().total_cost()
        return f"⚡ Elektr isitish ({self.type}): {cost:.2f} $"


heating_units = [GasHeating("Uy", 100, 0.05), ElectricHeating("Kottej", 200, 0.1)]
print("=" * 40)
print("  UY ISITISH TIZIMI XARAJATLARI")
print("=" * 40)
for h in heating_units:
    print(h.total_cost())
print()


# ============================================
# 43-masala: O'quv materiallari
# ============================================
class LearningMaterial:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class BookMaterial(LearningMaterial):
    def get_price(self):
        p = super().get_price()
        return f"📖 Kitob ({self.name}): {p} $"


class VideoMaterial(LearningMaterial):
    def get_price(self):
        p = super().get_price()
        return f"🎥 Video dars ({self.name}): {p} $"


materials = [BookMaterial("Python", 20), VideoMaterial("Algoritmlar", 15)]
print("=" * 40)
print("  O'QUV MATERIALLARI NARXLARI")
print("=" * 40)
for m in materials:
    print(m.get_price())
print()


# ============================================
# 44-masala: Restoran menyusi
# ============================================
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class HotMenuItem(MenuItem):
    def get_price(self):
        p = super().get_price()
        return f"🥣 Issiq taom ({self.name}): {p} $"


class ColdMenuItem(MenuItem):
    def get_price(self):
        p = super().get_price()
        return f"🥗 Sovuq taom ({self.name}): {p} $"


menu = [HotMenuItem("Sho'rva", 8), ColdMenuItem("Salat", 5)]
print("=" * 40)
print("  RESTORAN MENYUSI")
print("=" * 40)
for item in menu:
    print(item.get_price())
print()


# ============================================
# 45-masala: Sport kiyimlari
# ============================================
class Sportswear:
    def __init__(self, s_type, price):
        self.type = s_type
        self.price = price

    def get_price(self):
        return self.price


class Sneaker(Sportswear):
    def get_price(self):
        p = super().get_price()
        return f"👟 Krossovka ({self.type}): {p} $"


class Apparel(Sportswear):
    def get_price(self):
        p = super().get_price()
        return f"🎽 Sport kiyimi ({self.type}): {p} $"


clothes = [Sneaker("Nike", 60), Apparel("Adidas", 40)]
print("=" * 40)
print("  SPORT KIYIMLARI NARXLARI")
print("=" * 40)
for c in clothes:
    print(c.get_price())
print()


# ============================================
# 46-masala: Mobil ilova obunalari
# ============================================
class Subscription:
    def __init__(self, sub_type, price):
        self.type = sub_type
        self.price = price

    def get_price(self):
        return self.price


class MonthlySubscription(Subscription):
    def get_price(self):
        p = super().get_price()
        return f"📅 Oylik obuna ({self.type}): {p} $"


class YearlySubscription(Subscription):
    def get_price(self):
        p = super().get_price()
        return f"🗓️ Yillik obuna ({self.type}): {p} $"


subs = [MonthlySubscription("Premium", 10), YearlySubscription("Premium", 100)]
print("=" * 40)
print("  MOBIL ILOVA OBUNALARI")
print("=" * 40)
for s in subs:
    print(s.get_price())
print()


# ============================================
# 47-masala: Bog‘ parvarishi
# ============================================
class GardenCare:
    def __init__(self, p_type, cost):
        self.type = p_type
        self.cost = cost

    def get_cost(self):
        return self.cost


class FlowerCare(GardenCare):
    def get_cost(self):
        c = super().get_cost()
        return f"🌸 Gul parvarishi ({self.type}): {c} $"


class TreeCare(GardenCare):
    def get_cost(self):
        c = super().get_cost()
        return f"🌳 Daraxt parvarishi ({self.type}): {c} $"


garden_tasks = [FlowerCare("Atirgul", 20), TreeCare("Archa", 50)]
print("=" * 40)
print("  BOG' PARVARISHI XARAJATLARI")
print("=" * 40)
for task in garden_tasks:
    print(task.get_cost())
print()


# ============================================
# 48-masala: O‘yin ballari
# ============================================
class GameScore:
    def __init__(self, g_type, score):
        self.type = g_type
        self.score = score

    def get_score(self):
        return self.score


class SoloGame(GameScore):
    def get_score(self):
        s = super().get_score()
        return f"👤 Individual o'yin ({self.type}): {s} ball"


class TeamGame(GameScore):
    def get_score(self):
        s = super().get_score()
        return f"👥 Jamoaviy o'yin ({self.type}): {s} ball"


game_results = [SoloGame("Shaxmat", 100), TeamGame("Futbol", 150)]
print("=" * 40)
print("  O'YIN BALLARI")
print("=" * 40)
for res in game_results:
    print(res.get_score())
print()


# ============================================
# 49-masala: Do‘kon zaxiralari
# ============================================
class Stock:
    def __init__(self, s_type, quantity):
        self.type = s_type
        self.quantity = quantity

    def check_quantity(self):
        return self.quantity


class FoodStock(Stock):
    def check_quantity(self):
        q = super().check_quantity()
        return f"🍎 Oziq-ovqat zaxirasi ({self.type}): {q} dona"


class ElectronicsStock(Stock):
    def check_quantity(self):
        q = super().check_quantity()
        return f"📱 Elektronika zaxirasi ({self.type}): {q} dona"


stocks = [FoodStock("Meva", 200), ElectronicsStock("Telefon", 50)]
print("=" * 40)
print("  DO'KON ZAXIRALARI")
print("=" * 40)
for item in stocks:
    print(item.check_quantity())
print()


# ============================================
# 50-masala: Sayohat vaqtlari
# ============================================
class Travel:
    def __init__(self, t_type, duration):
        self.type = t_type
        self.duration = duration

    def get_duration(self):
        return self.duration


class FlightTravel(Travel):
    def get_duration(self):
        hr = super().get_duration()
        return f"✈️ Samolyotda sayohat ({self.type}): {hr} soat"


class TrainTravel(Travel):
    def get_duration(self):
        hr = super().get_duration()
        return f"🚂 Poezdda sayohat ({self.type}): {hr} soat"


travel_plans = [FlightTravel("Toshkent-Dubai", 2), TrainTravel("Toshkent-Samarqand", 5)]
print("=" * 40)
print("  SAYOHAT VAQTLARI")
print("=" * 40)
for plan in travel_plans:
    print(plan.get_duration())
print()

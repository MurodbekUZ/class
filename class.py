# 1-masala. Supermarket savatchasi 
# class CartItem:
#     def __init__(self, name, price, quantity, discount):
#         # Mahsulot nomi 
#         self.name = name   
#         # Mahsulot narxi
#         self.price = price
#         # Mahsulot miqdori
#         self.quantity = quantity
#         # Mahsulot chegirmasi
#         self.discount = discount

#     def total_price(self):
#         # Umumiy narxni hisoblash
#         return self.price * self.quantity * (1 - self.discount / 100)
    
#     # Oziq-ovqat mahsulotlari uchun alohida sinf
# class FoodItem(CartItem):
#     def total_cost(self):
#         # Asosiy narxni hisoblash
#         cost = super().total_price()
#         # Formatlangan natijani qaytarish
#         return f"Oziq-ovqat mahsuloti: {self.name}, Umumiy narx: {cost:.2f} so'm"
    
#     # Oziq-ovqat bo'lmagan mahsulotlar uchun alohida sinf
# class NonFoodItem(CartItem):
#     def total_cost(self):
#         # Asosiy narxni hisoblash
#         cost = super().total_price()
#         # Formatlangan natijani qaytarish
#         return f"Oziq-ovqat bo'lmagan mahsulot: {self.name}, Umumiy narx: {cost:.2f} so'm"
    
    
#     # Savatchadagi mahsulotlar ro'yxati
# items = [
    
#     FoodItem("Olma", 1.5, 3, 10),
#     NonFoodItem("Non", 2.0, 2, 5)
# ]    
       
#     #    Barcha mahsulotlar uchun umumiy narxni hisoblash 
# total_sum = 0

#     # Har bir mahsulot uchun umumiy narxni chiqarish
# for item in items:
#     print(item.total_cost())
#     total_sum += item.price * item.quantity * (1 - item.discount / 100)

#     # Umumiy narxni chiqarish
# print(f"Jami savat narxi: {round(total_sum, 2)} so'm")

# 2-masala. Transport xarajatlari
# class Vehicle:
#     def __init__(self, name, distance, fuel_efficiency, fuel_price):
#         # Transport vositasi nomi
#         self.name = name
#         # Masofa (km)
#         self.distance = distance
#         # Yoqilg'i samaradorligi (km/l)
#         self.fuel_efficiency = fuel_efficiency
#         # Yoqilg'i narxi (so'm/l)
#         self.fuel_price = fuel_price
        
#     def trip_cost(self):
#         return self.distance * self.fuel_efficiency * self.fuel_price
    
# class Car(Vehicle):
#     def trip_cost(self):
#         cost = super().trip_cost()
#         return f"Avtomobil: {self.name}, Safar narxi: {cost:.2f} so'm"
    
# class Motorcycle(Vehicle):
#     def trip_cost(self):
#         cost = super().trip_cost()
#         return f"Motosikl: {self.name}, Safar narxi: {cost:.2f} so'm"
    
# items = [
#     Car("Toyota", 150, 0.1, 12000),
#     Motorcycle("Yamaha", 100, 0.05, 12000)
# ]

# total_sum = 0

# for item in items:
#     print(item.trip_cost())
#     total_sum += item.distance * item.fuel_efficiency * item.fuel_price
# print(f"Jami transport xarajatlari: {round(total_sum, 2)} so'm")        

# 3-masala. Uy hayvonlari ovqatlanishi
# class Pet:
#     def __init__(self, name, daily_food):
#         # Uy hayvoni nomi
#         self.name = name
#         # Kunlik ovqat miqdori (gramm)
#         self.daily_food = daily_food
        
#     def feeding_plan(self, days):
#         return self.daily_food * days
    
# class Dog(Pet):
#     def feeding_plan(self, days):
#         food = super().feeding_plan(days)
#         return f"It: {self.name}, {days} kunlik ovqat miqdori: {food} gramm"
    
# class Cat(Pet):
#     def feeding_plan(self, days):
#         food = super().feeding_plan(days)
#         return f"Mushuk: {self.name}, {days} kunlik ovqat miqdori: {food} gramm"
    
# items = [
#     Dog("Rex", 300),
#     Cat("Murka", 150)
# ]

# total_food = 0

# for item in items:
#     print(item.feeding_plan(7))
#     total_food += item.daily_food * 7
# print(f"Jami 7 kunlik ovqat miqdori: {total_food} gramm")      

# 4-masala. Restoran buyurtmalari
# class Order:
#     def __init__(self, name, price, service_fee):
#         # Taom nomi
#         self.dish_name = name
#         # Taom narxi
#         self.price = price
#         # Xizmat haqi
#         self.service_fee = service_fee

#     def total_cost(self):
#         return self.price * (1 + self.service_fee / 100)
        
# class MainDish(Order):
#     def total_cost(self):
#         cost = super().total_cost()
#         return f"Asosiy taom: {self.dish_name}, Umumiy narx: {cost:.2f} so'm"
    
# class SideDish(Order):
#     def total_cost(self):
#         cost = super().total_cost()
#         return f"Qo'shimcha taom: {self.dish_name}, Umumiy narx: {cost:.2f} so'm"
    
# items = [
#     MainDish("Lavash", 15000, 10),
#     SideDish("Salat", 8000, 5)
# ]

# total_sum = 0

# for item in items:
#     print(item.total_cost())
#     total_sum += item.price * (1 + item.service_fee / 100)
# print(f"Jami buyurtma narxi: {round(total_sum, 2)} so'm")            
        
# 5-masala. O‘quvchilarning baholari
# class Student:
#     def __init__(self, name, grades):
#         # O'quvchi nomi
#         self.name = name
#         # O'quvchi baholari ro'yxati
#         self.grades = grades
        
#     def average_score(self):
#         return sum(self.grades) / len(self.grades)
    
# class HighSchoolStudent(Student):
#     def average_grade(self):
#         avg = super().average_grade()
#         return f"O'rta maktab o'quvchisi: {self.name}, O'rtacha baho: {avg:.2f}"  
    
# class CollegeStudent(Student):
#     def average_grade(self):
#         avg = super().average_grade()
#         return f"Kollej o'quvchisi: {self.name}, O'rtacha baho: {avg:.2f}"
    
# items = [
#     HighSchoolStudent("Ali", [85, 90, 78, 92]),
#     CollegeStudent("Vali", [88, 76, 95, 89])
# ]

# total_sum = 0

# for item in items:
#     print(item.average_grade())
#     total_sum += item.average_grade()
# print(f"Jami o'quvchilar soni: {len(items)}")
        
# 6-masala. Kitob ijarasi
# class BookRental:
#     def __init__(self, title, due_date):
#         # Kitob nomi
#         self.title = title
#         # Kunlik ijara narxi
#         self.due_date = due_date

#     def is_overdue(self, current_date):
#         return self.due_date < current_date
    
# class FictionBook(BookRental):
#     def overdue_status(self, current_date):
#         overdue = super().is_overdue(current_date)
#         status = "Ha" if overdue else "Yo'q"
#         return f"Fiction kitob: {self.title}, Kechikkanmi: {status}"
    
# class NonFictionBook(BookRental):
#     def overdue_status(self, current_date):
#         overdue = super().is_overdue(current_date)
#         status = "Ha" if overdue else "Yo'q"
#         return f"Non-Fiction kitob: {self.title}, Kechikkanmi: {status}"
    
# items = [
#     FictionBook("Alchemist", "2024-06-01"),
#     NonFictionBook("Sapiens", "2024-05-20")
# ]

# current_date = "2025-01-15"        

# for item in items:
#     print(item.overdue_status(current_date))    
#     total += item.is_overdue(current_date)
# print(f"Jami kechikkan kitoblar soni: {total}")

# 7-masala.  Kommunal xarajatlari
# class Utility:
#     def __init__(self, type, amount, rate):
#         # Xizmat turi
#         self.type = type
#         # Sarf miqdori
#         self.amount = amount
#         # Tarif (so'm birligi)
#         self.rate = rate

#     def calculate_cost(self):
#         return self.amount * self.rate
    
# class Electricity(Utility):
#     def total_cost(self):
#         cost = super().calculate_cost()
#         return f"Elektr energiyasi: {self.type}, Umumiy xarajat: {cost:.2f} so'm"
    
# class Water(Utility):
#     def total_cost(self):
#         cost = super().calculate_cost()
#         return f"Suv: {self.type}, Umumiy xarajat: {cost:.2f} so'm"
    
# items = [
#     Electricity("Uy", 350, 1200),
#     Water("Uy", 25, 8000)
# ]

# total_sum = 0

# for item in items:
#     print(item.total_cost())
#     total_sum += item.amount * item.rate
# print(f"Jami kommunal xarajatlar: {round(total_sum, 2)} so'm")            

# 8-masala. Fitness mashqlari
# class Exercise:
#     def __init__(self, name, duration, calories_burned):
#         # Mashq nomi
#         self.name = name
#         # Mashq davomiyligi (daqiqa)
#         self.duration = duration
#         # Yoqilgan kaloriya miqdori
#         self.calories_burned = calories_burned

#     def total_calories(self):
#         return self.duration * self.calories_burned
    
# class CardioExercise(Exercise):
#     def calories_info(self):
#         calories = super().total_calories()
#         return f"Kardio mashq: {self.name}, Yoqilgan kaloriya: {calories} kcal"
    
# class StrengthExercise(Exercise):
#     def calories_info(self):
#         calories = super().total_calories()
#         return f"Kuch mashqi: {self.name}, Yoqilgan kaloriya: {calories} kcal"
    
# items = [
#     CardioExercise("Yugurish", 30, 10),
#     StrengthExercise("Og'irlik ko'tarish", 20, 8)
# ]

# total_calories = 0

# for item in items:
#     print(item.calories_info())
#     total_calories += item.duration * item.calories_burned
# print(f"Jami yoqilgan kaloriya: {total_calories} kcal")    

# 9-masala. Ta’til rejalashtiruvchisi
# class Expense:
#     def __init__(self, category, amount):
#         self.category = category
#         self.amount = amount

#     def get_cost(self):
#         return self.amount


# # 2. Transport xarajatlari
# class TransportExpense(Expense):
#     def get_cost(self):
#         return f"Transport xarajati: ${self.amount}"


# # 3. Yashash xarajatlari
# class AccommodationExpense(Expense):
#     def get_cost(self):
#         return f"Yashash xarajati: ${self.amount}"


# # 4. Misol xarajatlar
# expenses = [
#     TransportExpense("Transport", 200),
#     AccommodationExpense("Yashash", 300)
# ]

# # 5. Xarajatlarni chop etish
# for expense in expenses:
#     print(expense.get_cost())

# 10-masala. Telefon tariflari
# 1. Asosiy PhonePlan sinfi
# class PhonePlan:
#     def __init__(self, name, minutes, sms, minute_rate, sms_rate):
#         self.name = name
#         self.minutes = minutes
#         self.sms = sms
#         self.minute_rate = minute_rate
#         self.sms_rate = sms_rate

#     def total_cost(self):
#         return self.minutes * self.minute_rate + self.sms * self.sms_rate


# # 2. Standart tarif
# class StandardPlan(PhonePlan):
#     def total_cost(self):
#         cost = super().total_cost()
#         return f"Standart tarif xarajati: ${cost:.2f}"


# # 3. Premium tarif
# class PremiumPlan(PhonePlan):
#     def total_cost(self):
#         cost = super().total_cost()
#         return f"Premium tarif xarajati: ${cost:.2f}"


# # 4. Misol tariflar
# plans = [
#     StandardPlan("Standart", 100, 50, 0.1, 0.05),
#     PremiumPlan("Premium", 200, 100, 0.08, 0.04)
# ]

# # 5. Tarif xarajatlarini chop etish
# for plan in plans:
#     print(plan.total_cost())

# 11-masala. Bog‘dorchilik rejasi
# class Plant:
#     def __init__(self, name, water_needed):
#         self.name = name
#         self.water_needed = water_needed

#     def watering_plan(self):
#         return self.water_needed


# # 2. Gul uchun sinf
# class Flower(Plant):
#     def watering_plan(self):
#         return f"{self.name} sug‘orish miqdori: {self.water_needed} litr"


# # 3. Daraxt uchun sinf
# class Tree(Plant):
#     def watering_plan(self):
#         return f"{self.name} sug‘orish miqdori: {self.water_needed} litr"


# # 4. Misol o‘simliklar
# plants = [
#     Flower("Gul", 2),
#     Tree("Daraxt", 5)
# ]

# # 5. Sug‘orish miqdorini chop etish
# for plant in plants:
#     print(plant.watering_plan())

# 12-masala. Ish haqi hisoblash
# class Employee:
#     def __init__(self, name, hourly_rate, hours, overtime):
#         self.name = name
#         self.hourly_rate = hourly_rate
#         self.hours = hours
#         self.overtime = overtime
        
#     def calculate_salary(self):
#         base_salary = self.hourly_rate * self.hours
        
#         overtime_pay = self.overtime * (self.hourly_rate * 1.5)
#         return base_salary + overtime_pay
    
# class FullTimeEmployee(Employee):
#     def calculate_salary(self):
#         base_salary = super().calculate_salary()
#         overtime_bonus = 0
#         if self.overtime and self.hours > 40:
#             # 40 soatdan ortiq ishlasa, 50% bonus qo‘shiladi
#             overtime_hours = self.hours - 40
#             overtime_bonus = overtime_hours * self.hourly_rate * 0.5
#         return base_salary + overtime_bonus
    
# class PartTimeEmployee(Employee):
#     def calculate_salary(self):
#         return super().calculate_salary()
         
# employees_data = [
#     {"name": "Ali", "hourly_rate": 20, "hours": 45, "overtime": True},
#     {"name": "Vali", "hourly_rate": 15, "hours": 40, "overtime": False}
# ]              

# employees = []
# for data in employees_data:
#     if data["hours"] > 40:
#         employees.append(FullTimeEmployee(**data))
#     else:
#         employees.append(PartTimeEmployee(**data))

# # 6. Ish haqlarini chop etish
# for emp in employees:
#     print(f"{emp.name} ning ish haqi: ${emp.calculate_salary():.2f}")        

# 13-masala. Internet tezligi
# 1. Asosiy InternetTest sinfi
# class InternetTest:
#     def __init__(self, test_type, download, upload):
#         self.type = test_type        # Test turi: WiFi yoki 4G
#         self.download = download     # Yuklash tezligi (Mbps)
#         self.upload = upload         # Yuborish tezligi (Mbps)

#     # 2. O'rtacha tezlikni hisoblovchi metod
#     def average_speed(self):
#         return (self.download + self.upload) / 2


# # 3. WiFi va Mobile (4G) testlari uchun meros oluvchi sinflar
# class WiFiTest(InternetTest):
#     def average_speed(self):
#         avg = super().average_speed()  # Asosiy metodni ishlatamiz
#         return f"WiFi o'rtacha tezligi: {avg} Mbps"

# class MobileTest(InternetTest):
#     def average_speed(self):
#         avg = super().average_speed()
#         return f"4G o'rtacha tezligi: {avg} Mbps"


# # 4. Misol test ma'lumotlari
# tests = [
#     WiFiTest("WiFi", 50, 20),
#     MobileTest("4G", 30, 15)
# ]

# # 5. O'rtacha tezliklarni chop etish
# for test in tests:
#     print(test.average_speed())

     
        
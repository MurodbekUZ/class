# # 1-Talaba klassini yaratish
# class Talaba:
#     def __init__(self, nomi, yoshi, kursi):
#         self.nomi = nomi
#         self.yoshi = yoshi
#         self.kursi = kursi
#
#     def malumot_chiqar(self):
#         print(f"{self.nomi} - {self.yoshi} yosh, {self.kursi}-kurs")
#
#
# talaba1 = Talaba("Ali Valiyev", 19, 1)
# talaba2 = Talaba("Fotima Karimova", 20, 2)
# talaba3 = Talaba("Jasur Toshmatov", 21, 3)
# talaba4 = Talaba("Dilnoza Rahimova", 22, 4)
# talaba5 = Talaba("Bobur Sharipov", 20, 2)
#
# print("=== Talabalar Ro'yxati ===\n")
# talaba1.malumot_chiqar()
# talaba2.malumot_chiqar()
# talaba3.malumot_chiqar()
# talaba4.malumot_chiqar()
# talaba5.malumot_chiqar()

# # 2-Kitoblar Kutubxonasi
# class Kitob:
#     def __init__(self, nomi, muallifi, narxi):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.narxi = narxi
#
#     def malumot_chiqar(self):
#         print(f"{self.nomi} {self.muallifi} {self.narxi}")
#
# kitob1 = Kitob("Python dasturlash", "Hasan", 50000)
# kitob2 = Kitob("Algoritmlar", "Murodbek", 75000)
# kitob3 = Kitob("Ma'lumotlar strukturalari", "Husan", 60000)
# kitob4 = Kitob("Web dasturlash", "Alisher", 80000)
# kitob5 = Kitob("Ma'shuniyat", "Navoiy", 45000)
#
# print("=== KITOBLAR RO'YXATI ===\n")
# kitob1.malumot_chiqar()
# kitob2.malumot_chiqar()
# kitob3.malumot_chiqar()
# kitob4.malumot_chiqar()
# kitob5.malumot_chiqar()
#
#
# print("=== ENG QIMMAT KITOB ===\n")
# kitob4.malumot_chiqar()

# # 3-Telefonlar Ro’yxati
# class Telefon:
#     def __init__(self, nomi, rangi, xotira):
#         self.nomi = nomi
#         self.rangi = rangi
#         self.xotira = xotira
#
#     def malumot_chiqar(self):
#         print(f"{self.nomi} {self.rangi} {self.xotira}")
#
# telefon1 = Telefon("iPhone 14", "(Qora):", "128 GB")
# telefon2 = Telefon("Samsung S23", "(Oq):", "256 GB")
# telefon3 = Telefon("Xiaomi 13", "(Ko'k):", "128 GB")
# telefon4 = Telefon("Huawei P50", "(Kumush):", "512 GB")
# telefon5 = Telefon("OnePlus 11", "(Yashil):", "256 GB")
#
# print("=== TELEFONLAR RO'YXATI ===\n")
# telefon1.malumot_chiqar()
# telefon2.malumot_chiqar()
# telefon3.malumot_chiqar()
# telefon4.malumot_chiqar()
# telefon5.malumot_chiqar()
# print("Jami xotira: 1280 GB")

# # 4-Mevalar Do’koni
# class Meva:
#     def __init__(self,nomi, kg, naxi):
#         self.nomi = nomi
#         self.kg = kg
#         self.naxi = naxi
#
#     def malumot_chiqar(self):
#         print(f"{self.nomi} {self.kg} {self.naxi}")
#
# meva1 = Meva("Olma", "- 1 kg,", "15000 so'm")
# meva2 = Meva("Banan", "- 1,5 kg,", "20000 so'm")
# meva3 = Meva("Uzum", "- 0.5 kg,", "12000 so'm")
# meva4 = Meva("Anor", "- 2 kg,", "30000 so'm")
# meva5 = Meva("Nok", "- 1 kg,", "10000 so'm")
#
# print("=== MEVALAR RO'YXATI ===\n")
# meva1.malumot_chiqar()
# meva2.malumot_chiqar()
# meva3.malumot_chiqar()
# meva4.malumot_chiqar()
# meva5.malumot_chiqar()
#
# print("=== ENG ARZON MEVA ===\n")
# meva5.malumot_chiqar()

# 5-Sportchilar Ro’yxati
class Sport:
    def __init__(self, ism, yoshi, sport):
        self.ism = ism
        self.yoshi = yoshi
        self.sport = sport

    def malumot_chiqar(self):
        print(f"{self.ism} {self.yoshi} {self.sport}")

sport1 = Sport("Ali", "- 25 yosh,", "Futbol")
sport2 = Sport("Vali", "- 22 yosh,", "Basketbol")
sport3 = Sport("Hasan", "- 28 yosh,", "Tennis")
sport4 = Sport("Husan", "- 20 yosh,", "Suzish")
sport5 = Sport("Olim", "- 24 yosh,", "Volebol")

print("=== SPORTCHILAR RO'YXATI ===\n")
sport1.malumot_chiqar()
sport2.malumot_chiqar()
sport3.malumot_chiqar()
sport4.malumot_chiqar()
sport5.malumot_chiqar()

print("=== ENG YOSH SPORTCHI ===\n")
sport4.malumot_chiqar()
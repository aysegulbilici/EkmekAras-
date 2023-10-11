# görev:
# aynı dizindeki metin belgelerini tek tek oku ve gerekli yapılara dök. not: SEVİYE1 direkt okunup listelere dökülebilir.
# tüm dosyalar okunduktan sonra kullanıcıya konsol aracılığı ile sandviç içinde hangi malzemeleri istediği sorulsun ve kullanıcılar malzeme seçebilsin.

# KONSOL ARAYUZU
# Ekmek aranızda hangi (sebze-VEGATABLES) olsun?
# 1. tomatoes
# 2. lettuce
# 3. cucumber
# 4. pepper
# 5. pickle
#
# Ekmek aranızda hangi (birincil malzeme-PRIMARY) olsun?
# 1. raw somon
# 2. beef
# 3. cheese
# 4. chicken
#
# Ekmek aranızda hangi (sos-SAUCES) olsun?
# 1. ketchup
# 2. mayonise
# 3. salca
# 4. salsa
# 5. mustard
# 6. extra hot sauce
# 7. barbecue sauce
#
# ...
#
# CIKTI not: parantez içi kullanıcının konsoldan seçtiği ogelerle doldurulacaktır.
# (Primary) (sauces) (vegatables) ekmek arası siparişiniz alınmıştır. yanında içecek olarak (beverages) getirilecektir.
#
#
#fonksiyonlara böl
#





#reading vegatables.txt
v = open("C:/Users/ayseg/Desktop/EkmekArası/VEGATABLES.txt","r")
#creating list for vegetables datas 
vegetables_lists=[]
#vegatables.txt's datas loading to list
with open("C:/Users/ayseg/Desktop/EkmekArası/VEGATABLES.txt", "r") as v:
    vegetables_lists = v.readlines()
#ordering vegetables
for index, element in enumerate(vegetables_lists, start=1):
      print(f"{index}. {element}")
print("-----------")

#reading primary.txt
p = open("C:/Users/ayseg/Desktop/EkmekArası/PRIMARY.txt","r")
#creating list for primaries datas 
primary_lists=[]
#primary.txt's datas loading to list
with open("C:/Users/ayseg/Desktop/EkmekArası/PRIMARY.txt", "r") as p:
    primary_lists = p.readlines()
#ordering primaries
for index, element in enumerate(primary_lists, start=1):
      print(f"{index}. {element}")
print("-----------")

#reading sauces.txt
s = open("C:/Users/ayseg/Desktop/EkmekArası/SAUCES.txt","r")
#creating list for sauces datas 
sauces_lists=[]
#sauces.txt's datas loading to list
with open("C:/Users/ayseg/Desktop/EkmekArası/SAUCES.txt", "r") as s:
    sauces_lists = s.readlines()
#ordering sauces
for index, element in enumerate(sauces_lists, start=1):
      print(f"{index}. {element}")
print("-----------")

#reading beverages.txt
b = open("C:/Users/ayseg/Desktop/EkmekArası/BEVERAGES.txt","r")
#creating list for beverages datas 
beverages_lists=[]
#beverages.txt's datas loading to list
with open("C:/Users/ayseg/Desktop/EkmekArası/BEVERAGES.txt", "r") as b:
    beverages_lists = b.readlines()
for index, element in enumerate(beverages_lists, start=1):
      print(f"{index}. {element}")
print("-----------")


#choose vegetable 
chosen= input("Which vegetable do you prefer? ")
if 1 <= int(chosen) <= len(vegetables_lists):
    chosen_vegetable= vegetables_lists[int(chosen) - 1]
    print(f"Chosen Vegetable: {chosen_vegetable}")
else:
    print("You entered wrong number")


chosen = input("Which primary do you prefer? ")
if 1 <= int(chosen) <= len(primary_lists):
    chosen_primary = primary_lists[int(chosen) - 1]
    print(f"Seçilen sebze: {chosen_primary }")
else:
    print("You entered wrong number")

chosen = input("Which sauce do you prefer? ")
if 1 <= int(chosen) <= len(sauces_lists):
    chosen_sauce = sauces_lists[int(chosen) - 1]
    print(f"Seçilen sos: {chosen_sauce}")
else:
    print("You entered wrong number.")

chosen = input("Which bevearge do you prefer? ")
if 1 <= int(chosen) <= len(beverages_lists):
    chosen_beverage= beverages_lists[int(chosen) - 1]
    print(f"Seçilen icecek: {chosen_beverage}")
else:
    print("You entered wrong number")

menu=[]
#Create a new list and there are chosen meals in it
menu = [chosen_vegetable,chosen_primary,chosen_sauce,chosen_beverage]


print(menu)









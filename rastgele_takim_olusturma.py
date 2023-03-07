# 2 tane liste olsun, 1.de erkekler, 2.de kadınlar olucak.
# bu listelerden rastgele bir seçim yapılacak ve takımlar oluşturulacak.
# her takım farklı olacak şekilde seçim yapılmalıdır.
import random

erkekListe = ["Mert","Erdem","Onur","Emin","Yavuz"]
kadinListe = ["Fatma","Elif","Eylül","Sinem","Ayşe"]

print("1.Takım",random.choice(erkekListe))
print(random.choice(kadinListe))
print("2.Takım",random.choice(erkekListe))
print(random.choice(kadinListe))
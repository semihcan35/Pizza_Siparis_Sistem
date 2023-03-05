import csv
import datetime
class Pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.get_cost


class Margarita(Pizza):
    cost = 60.0
    def __init__(self):
        self.description="Malzemeler : Mozeralla , Domates ve Fesleğen"
        print(self.description)

class Klasik(Pizza):
    cost = 70.0
    def __init__(self):
        self.description = "Malzemeler : Sucuk , Domates ve  Salam "
        print(self.description)

class TurkPizza(Pizza):
    cost = 80.0
    def __init__(self):
        self.description =  "Sucuk, Pastırma , Dana Sosis ve Domates"
        print(self.description)

class SadePizza(Pizza):
    cost = 65.0
    def __init__(self):
        self.description="Sucuk, Domates , Sosis"
        print(self.description)

class Decorator(Pizza):
    def __init__(self,ekstra):
        self.component = ekstra

    def get_cost(self):
        return self.component.get_cost() + \
        Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
        ';' + Pizza.get_description(self)


class Zeytin(Decorator):
    cost = 7.0
    def __init__(self):
        Decorator.__init__(self,ekstra)

class Mantar(Decorator):
    cost = 4.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Peynir(Decorator):
    cost = 7.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Et(Decorator):
    cost = 15.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Sogan(Decorator):
    cost = 6.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Misir(Decorator):
    cost = 4.0
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)

def main():
        dosya = open("Menu.txt", "r")
        oku = dosya.read()
        print(oku)

print("1-Klasik\n"  "2-Margarita\n"  "3-Türk Pizza\n" "4-Sade Pizza \n" "5-Zeytin\n" "6-Mantar\n" "7-Peynir\n" "8-Et\n" "9-Soğan\n" "10-Mısır")
menu={1: Klasik,
      2: Margarita,
      3: TurkPizza,
      4: SadePizza,
      5: Zeytin,
      6: Mantar,
      7: Peynir,
      8: Et,
      9: Sogan,
      10: Misir
      }

print()
kontrol = input("Pizza tabanınızı seçiniz: ")
while kontrol not in ["1","2","3","4"]:
    kontrol = print("Yanlış seçeneği seçtiniz")

order= menu[int(kontrol)]()

while kontrol != "*":
    kontrol = input("Ekstra malzeme seçiniz (Siparişi Onaylamak İçin '*' Tuşuna Basınız): ")
if kontrol in ["5","6","7","8","9","10"]:
    order = menu[int(kontrol)](order)


print("Sipariş Bilgileri:\n")
isim = input("İsminizi giriniz: ")
ID = input("T.C. kimlik numaranızı giriniz: ")
kk_no = input("Kredi kartı numaranızı giriniz: ")
kk_sifre = input("Kredi kartı şifrenizi giriniz: ")
time = datetime.datetime.now()

with open('Orders_Database.csv', 'a') as orders:
    orders = csv.writer(orders, delimiter=',')
    orders.writerow([isim, ID, kk_no, kk_sifre, order.get_description(), time])


print("Siparişiniz onaylandı.")







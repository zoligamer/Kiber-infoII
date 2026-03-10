import datetime


class Gepjarmu:
    def __init__(self,rendszam,ossz_km,kov_szerviz,szakasz_km):
        self.rendszam = rendszam
        self.ossz_km = ossz_km
        self.kov_szerviz = kov_szerviz
        self.szakasz_km = szakasz_km
    def szerviz(self):
        return self.kov_szerviz - datetime.datetime.now().year
    def vissza_km(self):
        return "benzines vagy elektromos"

class Taxi(Gepjarmu):
    def __init__(self,rendszam,ossz_km,kov_szerviz,szakasz_km,fogyasztas,tank_l):
        super().__init__(rendszam,ossz_km,kov_szerviz,szakasz_km)
        self.fogyasztas = fogyasztas
        self.tank_l = tank_l
    def vissza_km(self):
        return round(self.tank_l/self.fogyasztas*100-self.szakasz_km)

class Etaxi(Gepjarmu):
    def __init__(self,rendszam,ossz_km,kov_szerviz,szakasz_km,hatotav):
        super().__init__(rendszam,ossz_km,kov_szerviz,szakasz_km)
        self.hatotav = hatotav
    def vissza_km(self):
        return self.hatotav-self.szakasz_km

vehicle = Gepjarmu('ABC123',80000,2026,200)
taxi_1=Taxi('ABC456',90000,2027,500,7,35)
etaxi_1 = Etaxi('TIX431',800000,2028,400,500)
print(vehicle)
print(taxi_1)
print(etaxi_1)
print(isinstance(taxi_1,Etaxi))
print(vehicle.rendszam)
print(taxi_1.vissza_km())
print(taxi_1.fogyasztas)
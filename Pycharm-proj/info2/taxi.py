import datetime
class Taxi:
    regi_taxi=0
    uj_taxi=0
    def __init__(self,rendszam,ossz_km,kov_szerviz,szakasz_km,fogyasztas,tank_l):
        self.rendszam=rendszam
        self.ossz_km=ossz_km
        self.kov_szerviz=kov_szerviz
        self.szakasz_km=szakasz_km
        self.fogyasztas=fogyasztas
        self.tank_l=tank_l
        if ossz_km < 100000:
            type(self).uj_taxi+=1
        else:
            type(self).regi_taxi+=1
    def vissza_km(self):
        return round(self.tank_l / self.fogyasztas * 100 - self.szakasz_km)
    def szerviz(self):
        return  self.kov_szerviz - datetime.datetime.now().year
    @classmethod
    def flotta_db(cls):
        return cls.uj_taxi + cls.regi_taxi
    @staticmethod
    def flotta_info():
        return "tel:0615684952"

taxi_01=Taxi('ABC123',70000,2027,300,6.5,40)
taxi_02=Taxi('JHV456',90000,2027,500,8.9,70)
print(taxi_01.vissza_km())
print(taxi_02.szerviz())
print(taxi_01.rendszam)
print(Taxi.flotta_db())
print(Taxi.flotta_info())
print(Taxi.regi_taxi)
print(Taxi.uj_taxi)
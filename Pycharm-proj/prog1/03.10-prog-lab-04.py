class Kulcs:
    def __init__(self,serial):
        self.serial=serial
class Vehicle:
    def __init__(self,plate_serial,key_serial):
        self.plate_serial=plate_serial
        self.key_serial=Kulcs(key_serial)

    def __str__(self):
        return f'{self.plate_serial}{self.key_serial}'

veh_01=Vehicle('ABC123','AgGASE334')
print(veh_01)
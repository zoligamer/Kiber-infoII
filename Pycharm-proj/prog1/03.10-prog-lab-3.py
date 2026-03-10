"""from officehelper import retry


class Doboz:
    def __init__(self,tomeg):
        self.tomeg=tomeg
class Lada:
    def __init__(self,kapacitas):
        self.kapacitas=kapacitas
    def usage_examine(self,dobozok):
        tomeg = sum([dobozok.tomeg for doboz in dobozok])
        return tomeg/self.kapacitas*100
lada=Lada(40)
order=[Doboz(10),Doboz(20),Doboz(30),Doboz(40)]
print(f'{lada.usage_examine(order):.0f}%-os usage')"""


class Mechanic:
    def __init__(self,name):
        self.name=name

class Vehicle:
    def __init__(self,machine_id,mechanic_obj=None):
        self.machine_id=machine_id
        self.mechanic_obj=mechanic_obj
    def __str__(self):
        if self.mechanic_obj:
            return f'{self.machine_id} {self.mechanic_obj}'
        else:
            return f'{self.machine_id}'

mech_01=Mechanic('Big Tommy')
vehicle_01=Vehicle('AcSf3513gGk',mech_01.name)
print(vehicle_01)



from AutoV import AutoVehivulo
from moto import Moto



auto = AutoVehivulo('JEEP','4X4',4,2025)
moto = Moto('KAWASAKI','NINGA','DEPORTIVA',2025)
print(auto.descripcion())
print(moto.descripcion())

vehiculos= [
     AutoVehivulo('JEEP','4X4',4,2025),
     Moto('KAWASAKI','NINGA','DEPORTIVA',2025),
     AutoVehivulo('FORD','RAPTOR',4,2025),
     Moto('KAWASAKI','NO NINGA','DEPORTIVA',2025)
]

for vehiculo in vehiculos:
    print(vehiculo.descripcion())
    print()


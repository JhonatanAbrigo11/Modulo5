from empelado import Empleado

class empleadoTiempoCompleto (Empleado):
    def __init__(self, nombre, salario_base):
        super().__init__(nombre, salario_base)
    def calcular_salario(self):
        return self.salario_base + 20
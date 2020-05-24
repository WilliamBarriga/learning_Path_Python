class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludo(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'
    
david = persona('David', 35)
erik = persona('Erik', 36)

print(david.saludo(erik))
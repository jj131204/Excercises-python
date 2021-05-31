"""class Ussers:
    name = "juan"

usuario = Ussers()

print(usuario)
print(usuario.name)
"""

class Usser:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def saludo(self):
        print('Hola!, mi nombre es', self.name, self.lastName)

usser = Usser('Juan', 'Arteta')

usser.saludo()

#print(usser.name, usser.lastName)

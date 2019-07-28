class Persona:
    def __init__(self):
        self.nombre=input("ingrese nombre: ")
        self.apellido=input("ingrese apellido: ")
        self.edad=int(input("ingrese edad: "))
        self.sexo=(input("ingrese M O F: "))

    def mostrar(self):
       print("nombre: ",self.nombre)
       print("apellido: ", self.apellido)
       print("edad: ", self.edad)
       print("sexo: ", self.sexo)

class Alumno(Persona):
    def __init__(self):
        super().__init__()
        self.nota=float(input("ingrese nota: "))

    def mostrar(self):
        print("--------------Alumno: -------------------- ")
        super().mostrar()
        print("nota: ", self.nota)

class Profesor(Persona):
    def __init__(self):
        super().__init__()
        self.codProfesor=int(input("ingrese codigo: "))

    def mostrar(self):
        print("---------------Profesor: -------------------")
        super().mostrar()
        print("codigo: ", self.codProfesor)


persona1 = Persona()
persona1.mostrar()
alumno1 = Alumno()
alumno1.mostrar()
profesor1 = Profesor()
profesor1.mostrar()

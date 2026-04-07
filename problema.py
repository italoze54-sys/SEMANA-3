#Haz un programa en python que te muestre un menu con la primera opcion que te permita
#crear una persona con nombre y dni y la agregue a una lista de personas.
#El menu tendra una 2da opcion donde mostrara todas las personas
#El menu tendra una 3ra opcion que pedira el dni y eliminara a la persona de la lista

class Persona:
    
    def __init__(self, _nombre="", _dni=""):
        self.nombre=_nombre
        self.dni=_dni        
        
    def MostrarTodos(self, personas):
        for p in personas:
            print(f"Nombre: {p.nombre} - DNI: {p.dni}")
            
personas = []


while True:
    print ("================= MENÚ =================")
    opcion = int(input("1. Crear persona \n2. Mostrar personas \n3. Eliminar persona \n4. Salir\nElige una opción: "))
    
    if(opcion==1):
        nombre = input("Ingrese el nombre de la persona: ")
        dni = input("Ingrese el dni de la persona: ")
        persona = Persona(nombre, dni)
        personas.append(persona)
        print(f"Se ha creado a {persona.nombre} con dni {persona.dni}")
    
    elif (opcion ==2):
        persona = Persona()
        persona.MostrarTodos(personas)
    
    elif (opcion == 3):
        dni = input("Ingrese el número de dni para eliminar: ")
        for p in personas:
            if p.dni == dni:
                personas.remove(p)
                print(f"Se ha eliminado a {p.nombre} con dni {p.dni}")
                


    




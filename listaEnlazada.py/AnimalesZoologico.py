class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_tipo(self):
        return self.tipo
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("Esta edad no puede ser negativa.")

    def set_tipo(self, tipo):
        self.tipo = tipo

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad} años, Tipo: {self.tipo}")

class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        if self.existe_animal(animal):
            print(f"El animal {animal.get_nombre()} ya está en la lista.")
            return
        
        nuevo_nodo = Nodo(animal)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  

    def existe_animal(self, animal):
        actual = self.cabeza
        while actual:
            if (actual.animal.get_nombre() == animal.get_nombre() and 
                actual.animal.get_tipo() == animal.get_tipo()):
                return True
            actual = actual.siguiente
        return False  
        
    def mostrar_lista_iterativa(self):
        actual = self.cabeza
        while actual:
            actual.animal.mostrar_informacion()
            actual = actual.siguiente 

    def mostrar_lista_recursiva(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo:
            nodo.animal.mostrar_informacion()
            if nodo.siguiente:  
                self.mostrar_lista_recursiva(nodo.siguiente)



lista_animales = ListaEnlazada()
animal1 = Animal("Simba", 5, "León")
animal2 = Animal("Manny", 19, "Mamut")
animal3 = Animal("Micky", 3, "Ratón") 

lista_animales.agregar_animal(animal1)
lista_animales.agregar_animal(animal2)
lista_animales.agregar_animal(animal3)


print("\nMostrar lista (Iterativa):")
lista_animales.mostrar_lista_iterativa()

print("\nMostrar lista (Recursiva):")
lista_animales.mostrar_lista_recursiva()


        
   


   

    


    

                    




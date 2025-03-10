class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento  
        self.siguiente = None 

    def __str__(self):
        return f"Tarea: {self.descripcion} | Prioridad: {self.prioridad} | Vence: {self.fecha_vencimiento}"

class ListaTareas:
    def __init__(self):
        self.cabeza = None  

    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        
       
        if not self.cabeza or (self.cabeza.prioridad > prioridad or 
                              (self.cabeza.prioridad == prioridad and self.cabeza.fecha_vencimiento > fecha_vencimiento)):
            nueva_tarea.siguiente = self.cabeza
            self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            while (actual.siguiente and 
                  (actual.siguiente.prioridad < prioridad or 
                  (actual.siguiente.prioridad == prioridad and actual.siguiente.fecha_vencimiento <= fecha_vencimiento))):
                actual = actual.siguiente
            nueva_tarea.siguiente = actual.siguiente
            actual.siguiente = nueva_tarea

    def eliminar_tarea(self, descripcion=None, posicion=None):
        if not self.cabeza:
            print("La lista de tareas está vacía.")
            return

        if descripcion:
            actual = self.cabeza
            anterior = None
            while actual and actual.descripcion != descripcion:
                anterior = actual
                actual = actual.siguiente
            if actual:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"Tarea '{descripcion}' eliminada.")
            else:
                print(f"Tarea '{descripcion}' no encontrada.")
        elif posicion is not None:
            if posicion == 0:
                self.cabeza = self.cabeza.siguiente
                print(f"Tarea en la posición {posicion} eliminada.")
            else:
                actual = self.cabeza
                anterior = None
                for _ in range(posicion):
                    if not actual.siguiente:
                        print("Posición fuera de rango.")
                        return
                    anterior = actual
                    actual = actual.siguiente
                anterior.siguiente = actual.siguiente
                print(f"Tarea en la posición {posicion} eliminada.")

    def mostrar_tareas(self):
        actual = self.cabeza
        if not actual:
            print("No hay tareas en la lista.")
            return
        while actual:
            print(actual)
            actual = actual.siguiente

    def buscar_tarea(self, descripcion):
        actual = self.cabeza
        while actual:
            if actual.descripcion == descripcion:
                print("Tarea encontrada:", actual)
                return actual
            actual = actual.siguiente
        print(f"Tarea '{descripcion}' no encontrada.")
        return None

    def marcar_completada(self, descripcion):
        self.eliminar_tarea(descripcion)


lista = ListaTareas()
lista.agregar_tarea("Finalizar informe", 1, "2025-04-10")
lista.agregar_tarea("Comprar insumos", 2, "2025-04-05")
lista.agregar_tarea("Revisión de código", 1, "2025-04-07")
lista.agregar_tarea("Preparar presentación", 3, "2025-04-15")

print("\nLista de tareas:")
lista.mostrar_tareas()

print("\nBuscando una tarea:")
lista.buscar_tarea("Revisión de código")

print("\nMarcando tarea como completada:")
lista.marcar_completada("Revisión de código")
lista.mostrar_tareas()
class Nodo:
    def __init__(self, dato):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.dato = dato
        self.izquierda = None
        self.derecha = None 
def __agregar_recursivo(self, nodo, dato):
    if dato < nodo.dato:
        if nodo.izquierda is None:
            nodo.izquierda = Nodo(dato)
        else:
            self.__agregar_recursivo(nodo.izquierda, dato)
    else:
        if nodo.derecha is None:
            nodo.derecha = Nodo(dato)
        else:
            self.__agregar_recursivo(nodo.derecha, dato)
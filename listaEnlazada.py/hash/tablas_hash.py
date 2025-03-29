from typing import Optional

class Nodo:
    def __init__(self, clave: str, valor: str):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self, capacidad: int = 100):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad
    
    def _hash(self, clave: str) -> int:
        return sum(ord(c) for c in clave) % self.capacidad
    
    def insertar(self, clave: str, valor: str):
        indice = self._hash(clave)
        if self.tabla[indice] is None:
            self.tabla[indice] = Nodo(clave, valor)
        else:
            actual = self.tabla[indice]
            while actual.siguiente:
                if actual.clave == clave:
                    actual.valor = valor
                    return
                actual = actual.siguiente
            if actual.clave == clave:
                actual.valor = valor
            else:
                actual.siguiente = Nodo(clave, valor)
    
    def obtener(self, clave: str) -> Optional[str]:
        indice = self._hash(clave)
        actual = self.tabla[indice]
        while actual:
            if actual.clave == clave:
                return actual.valor
            actual = actual.siguiente
        return "Contacto no encontrado."
    
    def eliminar(self, clave: str) -> str:
        indice = self._hash(clave)
        actual = self.tabla[indice]
        previo = None
        while actual:
            if actual.clave == clave:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.tabla[indice] = actual.siguiente
                return f"Contacto {clave} eliminado exitosamente."
            previo = actual
            actual = actual.siguiente
        return "Contacto no encontrado."
    
    def mostrar(self):
        directorio = {}
        for i in range(self.capacidad):
            actual = self.tabla[i]
            while actual:
                directorio[actual.clave] = actual.valor
                actual = actual.siguiente
        return directorio

class DirectorioTelefonico:
    def __init__(self):
        self.directorio = TablaHash()
    
    def agregar_contacto(self, nombre: str, telefono: str) -> str:
        self.directorio.insertar(nombre, telefono)
        return f"Contacto {nombre} agregado exitosamente."
    
    def obtener_telefono(self, nombre: str) -> Optional[str]:
        return self.directorio.obtener(nombre)
    
    def eliminar_contacto(self, nombre: str) -> str:
        return self.directorio.eliminar(nombre)
    
    def mostrar_directorio(self):
        return self.directorio.mostrar()

directorio = DirectorioTelefonico()
print(directorio.agregar_contacto("Juan", "123-456-7890"))
print(directorio.obtener_telefono("Juan"))
print(directorio.eliminar_contacto("Juan"))
print(directorio.mostrar_directorio())

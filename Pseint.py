class PilaSimple:
    def __init__(self, capacidad=100):
        self.pila = [None] * capacidad  
        self.tope = 0  
        self.capacidad = capacidad

    def push(self, elemento):
        if self.tope < self.capacidad:
            self.pila[self.tope] = elemento
            self.tope += 1
        else:
            print("La pila está llena.")

    def pop(self):
        if self.tope > 0:
            self.tope -= 1
            print("Elemento desapilado:", self.pila[self.tope])
            self.pila[self.tope] = None  
        else:
            print("La pila está vacía.")

    def peek(self):
        if self.tope > 0:
            print("Elemento en la cima:", self.pila[self.tope - 1])
        else:
            print("La pila está vacía.")


def main():
    pila = PilaSimple()
    while True:
        print("\n1. Push (Apilar)  2. Pop (Desapilar)  3. Peek (Cima)  4. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            elemento = input("Ingrese un elemento: ")
            pila.push(elemento)
        elif opcion == 2:
            pila.pop()
        elif opcion == 3:
            pila.peek()
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

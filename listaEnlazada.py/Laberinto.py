class Laberinto:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        self.inicio = self.encontrar_inicio()
        self.pila = []

    def encontrar_inicio(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.laberinto[i][j] == 'S':
                    return (i, j)
        return None

    def es_valido(self, x, y):
        return 0 <= x < self.filas and 0 <= y < self.columnas and self.laberinto[x][y] in ('O', 'E')

    def resolver(self):
        if not self.inicio:
            print("No se encontró el punto de inicio.")
            return False
        
        self.pila.append((self.inicio, [self.inicio]))  
        
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        
        while self.pila:
            (x, y), camino = self.pila.pop()
            
            if self.laberinto[x][y] == 'E':
                print("¡Salida encontrada!")
                print("Camino recorrido:", camino)
                return True
            
            self.laberinto[x][y] = 'V'  
            
            for dx, dy in movimientos:
                nx, ny = x + dx, y + dy
                if self.es_valido(nx, ny):
                    self.pila.append(((nx, ny), camino + [(nx, ny)]))
        
        print("No hay salida en el laberinto.")
        return False


laberinto_matriz = [
    ['S', 'O', 'X', 'X','O'],
    ['X', 'O', 'O', 'X','O'],
    ['X', 'X', 'O', 'O','X'],
    ['O', 'O', 'X', 'O','E'],
    ['X', 'O', 'O', 'O','X'],
]

laberinto = Laberinto(laberinto_matriz)
laberinto.resolver()

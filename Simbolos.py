def verificar_balance(expresion):
    pila = []
    apertura = {'(': ')', '{': '}', '[': ']'}
    cierre = {')': '(', '}': '{', ']': '['}
    errores = []
    
    for i, char in enumerate(expresion):
        if char in apertura:  # Si es un símbolo de apertura
            pila.append((char, i))  # Guardamos el carácter y su posición
        elif char in cierre:  # Si es un símbolo de cierre
            if pila and pila[-1][0] == cierre[char]:
                pila.pop()  # Desapilar si coincide
            else:
                esperado = apertura.get(pila[-1][0], '') if pila else "ninguno"
                errores.append(f"Error en el símbolo \"{char}\" en línea 1 columna {i+1}: Se esperaba \"{esperado}\".")

    # Verificar si quedaron símbolos sin cerrar
    while pila:
        char, pos = pila.pop()
        errores.append(f"Error en el símbolo \"{char}\" en línea 1 columna {pos+1}: Falta el cierre \"{apertura[char]}\".")

    # Mostrar resultados
    if errores:
        return "\n".join(errores)
    else:
        return "Expresión balanceada."

# Ejemplos de uso
expresiones = [
    "{[()]}",
    "{[(])}",
    "([)]",
    "{[a + b] * (c / d)}",
    "[ ( x + y ) * { 2 + 3 }",
    "({[)]}"
]

for exp in expresiones:
    print(f"Expresión: {exp}")
    print(verificar_balance(exp))
    print("-" * 50)
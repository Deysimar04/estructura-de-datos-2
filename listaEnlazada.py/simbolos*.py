def verificar_balance(expresion):
    pila = []
    apertura = {'(': ')', '{': '}', '[': ']'}
    cierre = {')': '(', '}': '{', ']': '['}
    errores = []
    
    for i, char in enumerate(expresion):
        if char in apertura: 
            pila.append((char, i))  
        elif char in cierre:  
            if pila and pila[-1][0] == cierre[char]:
                pila.pop() 
            else:
                esperado = apertura.get(pila[-1][0], '') if pila else "ninguno"
                errores.append(f"Error en el símbolo \"{char}\" en línea 1 columna {i+1}: Se esperaba \"{esperado}\".")

  
    while pila:
        char, pos = pila.pop()
        errores.append(f"Error en el símbolo \"{char}\" en línea 1 columna {pos+1}: Falta el cierre \"{apertura[char]}\".")


    if errores:
        return "\n".join(errores)
    else:
        return "Expresión balanceada."


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
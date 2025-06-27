def es_palindromo(palabra):
    palabra = palabra.lower().strip()  # Limpiamos la palabra
    if palabra == palabra[::-1]:       # Comparamos con su versión invertida
        print(f"✅ '{palabra}' es un palíndromo")
    else:
        print(f"❌ '{palabra}' no es un palíndromo")

es_palindromo("ana")
es_palindromo("oso")
es_palindromo("joel")
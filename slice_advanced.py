def slice_advanced():
    # Código a implementar utilizando input.
    texto= input('Dime una palabra: ')
    texto= texto.lower()
    print(texto[:3])
    print(texto[3:6])
    print(texto[0:4] + texto[-3:])

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`

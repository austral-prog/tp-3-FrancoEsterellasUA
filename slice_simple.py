def slice_simple():
    texto = "Awesome"
    texto= input('Dime una palabra: ')
    texto= texto.lower()
    print(texto[:3])
    print(texto[3:6])
    print(texto[0:4] + texto[-3:])
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`

class NumeroEntero:
    def __init__(self, numero=0):
        self._numero = numero

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        if value > 0:
            self._numero = value
        else:
            raise ValueError("El número debe ser un entero positivo.")

    def __str__(self):
        return str(self._numero)


class CalculadoraMCD:
    def __init__(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2

    @property
    def numero1(self):
        return self._numero1

    @numero1.setter
    def numero1(self, value):
        self._numero1 = value

    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self, value):
        self._numero2 = value

    def calcular_mcd(self):
        a = self._numero1.numero
        b = self._numero2.numero
        while b != 0:
            a, b = b, a % b
        return a


def solicitar_numero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un número entero positivo.")
                continue
            return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")


if __name__ == "__main__":
    num1 = NumeroEntero()
    num2 = NumeroEntero()

    num1.numero = solicitar_numero("Ingrese el primer número entero positivo: ")
    num2.numero = solicitar_numero("Ingrese el segundo número entero positivo: ")

    calculadora = CalculadoraMCD(num1, num2)
    resultado = calculadora.calcular_mcd()

    print(f"El Máximo Común Divisor de {num1} y {num2} es: {resultado}")

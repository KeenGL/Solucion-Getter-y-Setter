class Numero_entero():
    def __init__(self, numero = 0):
        self._numero = numero

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self,value):
        self._numero = value

    def es_primo(self):
        primo = True
        for divisor in range (2, self.numero):
            if self.numero % divisor == 0:
                primo = False
        return primo

if __name__ == "__main__":
    numero = Numero_entero()
    numero.numero = int(input("Ingrese el numero: "))
    if numero.es_primo():
        print(f"El numero {numero.numero} es primo")
    else:
        print(f" EL numero {numero.numero} NO es primo")

class calculadora:
    """
    Calculadora simple.
    Atributos.
    ..........
    num1:
        El primer operando que será utilizado para realizar operaciones matemáticas.
    num2:
        El segundo operando con el que se realizarán operaciones matemáticas.
    Métodos.
    ........
    Suma:
        suma los operandos num1 y num2.
    Resta
        resta los operandos num1 y num2.
    Multiplicación
        multiplica los operandos num1 y num2.
    División
        Divide los operandos num1 y num2.

    Ejemplo:
    .......
    >>>import calculadora
    >>>calculadora=calculadora(2,4)
    >>>calculadora.multiplicar
    """
    def __init__(self,num1,num2):
        self.num1= float(num1)
        self.num2= float(num2)

    def sumar(self):
        """
        Método sumar: Realiza la operación de suma entre los operandos num1 y num2
        inputs: self.num1 y self.num2
        ......
        output: suma = resultado de la operación de suma.
        """
        suma = self.num1+ self.num2
        print
        (f"El resultado de la suma es: {suma}")
        return suma

    def restar(self):
        """
        Método restar: Realiza la operación de resta entre los operandos num1 y num2
        inputs: self.num1 y self.num2
        ......
        output: resta = resultado de la operación de resta.
        """
        resta = self.num1-self.num2
        print(f"El resultado de la resta es: {resta}")
        return resta

    def multiplicar(self):
        """
        Método multiplicar: Realiza la operación de multiplicación entre los operandos num1 y num2
        inputs: self.num1 y self.num2
        ......
        output: multiplicacion = resultado de la operación de multiplicar.
        """
        multiplicacion = self.num1*self.num2
        print(f"El resultado de la multiplicacion es: {multiplicacion}")
        return multiplicacion

    def dividir(self):
        """
        Método dividir: Realiza la operación de división entre los operandos num1 y num2
        inputs: self.num1 y self.num2
        ......
        output: division = resultado de la operación de division.
        """
        division = self.num1-self.num2
        print(f"El resultado de la división es: {division}")
        return division

num1 = float(input("Ingrese el numero 1: "))
num2 = float(input("Ingrese el numero 2: "))

calculadora=calculadora(num1,num2)
print("\n")
calculadora.sumar()
calculadora.restar()
calculadora.multiplicar()
calculadora.dividir()
print("\n")

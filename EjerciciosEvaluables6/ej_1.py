class Printer:

    def __init__(self):
        self.cadena=input("Ingrese cadena  ")


    def get_string(self):
        return self.cadena

    def print_string(self):
        print("Cadena:",self.cadena)



Cadena=Printer()
print(Cadena.get_string())
Cadena.print_string()


class Palabra:
    def __init__(self):
        self.palabra = ''

    def get_string(self):
        self.palabra = input("Ingrese una palabra: ")

    def print_string(self):
        print("obj.palabra --> ", self.palabra.upper())

word = Palabra()
word.get_string()
word.print_string()
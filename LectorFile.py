from util import leer_titulo


class LectorFile:

    def __init__(self, file):
        self.file = file

    def leer_entries(self):
        with open(self.file) as f:
            filas = f.readlines()
        for fila in filas:
            if fila.strip() != "":
                print(fila + " " + leer_titulo(fila))

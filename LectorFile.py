from util import leer_titulo
from tag import leer_tags


class LectorFile:

    def __init__(self, file):
        self.file = file

    def leer_entries(self):
        with open(self.file) as f:
            filas = f.readlines()
        for fila in filas:
            if fila.strip() != "":
                titulo = leer_titulo(fila)
                print('---')
                print(fila)
                print(titulo)
                print(leer_tags((fila, titulo,)))

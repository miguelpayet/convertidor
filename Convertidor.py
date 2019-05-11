from Entry import Entry
import Grabador


class Convertidor:

    def __init__(self, fila):
        self.fila = fila

    def convertir(self):
        entry = Entry(self.fila)
        grabador = Grabador.Blog(entry)
        grabador.grabar()

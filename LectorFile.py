import Grabador
from Entry import EntryFile


class LectorFile:

    def __init__(self, file):
        self.file = file

    def leer_entries(self):
        with open(self.file) as f:
            filas = f.readlines()
        for fila in filas:
            if fila.strip() != "":
                entry = EntryFile(fila)
                grabador = Grabador.File(entry)
                grabador.grabar()

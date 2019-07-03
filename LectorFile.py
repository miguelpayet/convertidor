from util import leer_titulo
from tag import leer_tags
from Entry import EntryFile
import Grabador


class LectorFile:

    def __init__(self, file):
        self.file = file

    def leer_entries(self):
        with open(self.file) as f:
            filas = f.readlines()
        for fila in filas:
            if fila.strip() != "":
                entry = EntryFile(fila)
                grabador = Grabador.Blog(entry)
                grabador.grabar()

from Tipo import Tipo
import re
import util


class Entry:

    def __init__(self, fila):
        self.fila = fila
        self.id = fila.id
        self.patron = []
        self.regex_link = util.regex_link()
        self.regex_url = re.compile("^https?:\\/\\/(.*)$")
        self.texto = None
        self.tipo = None
        self.titulo = None
        self.analizar()

    def analizar(self):
        arr = re.split("\n", self.fila.texto)
        self.tipo = Tipo.LINK
        self.patron = []
        for (linea) in arr:
            if linea.strip() != "":
                if self.regex_link.match(linea):
                    self.patron.append("l")
                    self.set_tipo_link()
                elif self.regex_url.match(linea):
                    self.patron.append("u")
                    self.set_tipo_link()
                else:
                    self.patron.append("o")
                    self.tipo = Tipo.MIXTO

    def set_tipo_link(self):
        if self.tipo != Tipo.MIXTO or self.tipo is None:
            self.tipo = Tipo.LINK

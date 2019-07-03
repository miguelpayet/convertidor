import re

from util import leer_titulo
from util import re_match_url


class Entry:

    def __init__(self, fila):
        self.fila = fila
        self.handle = None
        self.id = fila.id
        self.regex_link = re.compile('\\[(.*)\\]\\((.*\\))')
        self.texto = None
        self.titulo = fila.titulo
        self.crear_handle()
        self.analizar()

    def analizar(self):
        self.texto = ""
        arr = re.split("\n", self.fila.texto)
        for (linea) in arr:
            self.texto += self.mejorar_links(linea)

    def crear_handle(self):
        tmp_handle = self.titulo.lower().replace(" ", "-")
        self.handle = re.sub('[^0-9a-zA-Z\\-]+', '', tmp_handle)

    def mejorar_links(self, linea):
        if linea.strip() == "":
            return "\n"
        match = self.regex_link.match(linea)
        if match is not None:
            match_url = re_match_url(match.group(1))
            if match_url:
                titulo = leer_titulo(match.group(1))
                p1 = linea.find(match.group(1))
                parte1 = linea[:p1]
                p2 = len(linea) - (linea.find(match.group(1)) + len(match.group(1)))
                parte2 = linea[-p2:]
                mi_linea = parte1 + titulo + parte2
            else:
                mi_linea = linea
        else:
            match_url = re_match_url(linea)
            if match_url is not None:
                titulo = leer_titulo(match_url.group(1))
                mi_linea = "[{}]({})".format(titulo, match_url.group(1))
            else:
                mi_linea = linea
        return mi_linea + "\n"

import re

from util import leer_titulo
from tag import leer_tags
from util import re_match_url


def mejorar_links(linea):
    regex_link = re.compile('\\[(.*)\\]\\((.*\\))')
    if linea.strip() == "":
        return "\n"
    match = regex_link.match(linea)
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


class EntryAbstract:

    def __init__(self, titulo):
        self.handle = None
        self.titulo = titulo
        self.crear_handle()

    def crear_handle(self):
        tmp_handle = self.titulo.lower().replace(" ", "-")
        self.handle = re.sub('[^0-9a-zA-Z\\-]+', '', tmp_handle)


class Entry:

    def __init__(self, fila):
        self.texto = None
        self.fila = fila
        self.id = fila.id
        self.tags = leer_tags((self.fila.titulo, self.fila.texto))
        super().__init__(fila.titulo)
        self.analizar()

    def analizar(self):
        self.texto = ""
        arr = re.split("\n", self.fila.texto)
        for (linea) in arr:
            self.texto += mejorar_links(linea)


class EntryFile(EntryAbstract):

    def __init__(self, url):
        self.url = url
        self.titulo = leer_titulo(self.url)
        self.tags = leer_tags((self.url, self.titulo,))
        self.texto = '[%s](%s))' % (self.url, self.titulo)
        super().__init__(self.titulo)

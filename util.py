import re

from LectorTitulo import LectorTitulo


def leer_titulo(url):
    if url != "":
        leedor = LectorTitulo(url)
        titulo = leedor.leer_titulo()
    else:
        titulo = ""
    return titulo


def re_match_url(fila):
    regex_url = re.compile("(https?:\\/\\/.*)")
    return regex_url.match(fila)

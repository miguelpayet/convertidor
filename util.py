import re
from LectorTitulo import LectorTitulo


def leer_titulo(url):
    if url != "":
        leedor = LectorTitulo(url)
        titulo = leedor.leer_titulo()
    else:
        titulo = ""
    return titulo


def limpiar_titulo(handle):
    handle = handle.lower().replace(" ", "-")
    return re.sub('[^0-9a-zA-Z\\-]+', '', handle)


def regex_link():
    return re.compile('^\\[(.*)\\]\\((.*\\))$')

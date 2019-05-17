from LectorTitulo import LectorTitulo


def leer_titulo(url):
    if url != "":
        leedor = LectorTitulo(url)
        titulo = leedor.leer_titulo()
    else:
        titulo = ""
    return titulo

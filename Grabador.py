from BD import BD
from Tipo import Tipo
import re
import util
from LectorTitulo import LectorTitulo


class Blog:

    def __init__(self, entry):
        self.bd_destino = BD('blog', 'blog', 'blog')
        self.clases = {Tipo.LINK: Link, Tipo.MIXTO: Mixto}
        self.entry = entry
        self.regex_link = util.regex_link()
        self.sql_insert = "insert into entry (id, url, handle, descripcion, titulo, tipo, creado, cambiado) " \
                          "values (%s, %s, %s, %s, %s, %s, %s, %s)"

    def ejecutar(self, entry_id, url, handle, descripcion="", titulo="", tipo=0, creado=None, cambiado=None):
        cursor = self.bd_destino.cursor()
        try:
            cursor.execute(self.sql_insert, (entry_id, url, handle, descripcion, titulo, tipo, creado, cambiado))
            self.bd_destino.commit()
        except Exception as variable:
            print(variable)

    def grabar(self):
        clase = self.clases[self.entry.tipo]
        g = clase(self.entry)
        g.grabar()


class Link(Blog):

    def grabar(self):
        arr = re.split("\n", self.entry.fila.texto)
        pos = 0
        for (linea) in arr:
            if linea.strip() != "":
                tipo = self.entry.patron[pos]
                if tipo == "l":
                    match = self.regex_link.match(linea)
                    if match:
                        url = match.group(2)
                elif tipo == "u":
                    url = linea
                titulo = LectorTitulo(url).leer_titulo()
                handle = util.limpiar_titulo(titulo)
                self.ejecutar(self.entry.fila.id, "", handle, linea, titulo, self.entry.tipo.value,
                              self.entry.fila.creation_date, self.entry.fila.modification_date)
                pos += 1


class Mixto(Blog):

    def grabar(self):
        handle = util.limpiar_titulo(self.entry.fila.titulo)
        self.ejecutar(self.entry.fila.id, "", handle, self.entry.fila.texto, self.entry.fila.titulo,
                      self.entry.tipo.value, self.entry.fila.creation_date, self.entry.fila.modification_date)

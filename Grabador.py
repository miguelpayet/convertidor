from BD import BD


class Blog:

    def __init__(self, entry):
        self.bd_destino = BD('blog', 'blog', 'blog')
        self.entry = entry
        self.sql_insert = "insert into entry (identry, handle, descripcion, titulo, creado, cambiado) " \
                          "values (%s, %s, %s, %s, %s, %s)"

    def ejecutar(self, entry_id, handle, descripcion="", titulo="", creado=None, cambiado=None):
        cursor = self.bd_destino.cursor()
        try:
            cursor.execute(self.sql_insert, (entry_id, handle, descripcion, titulo, creado, cambiado))
            self.bd_destino.commit()
        except Exception as variable:
            print(variable)

    def grabar(self):
        self.ejecutar(self.entry.fila.id, self.entry.handle, self.entry.texto, self.entry.titulo,
                      self.entry.fila.creation_date, self.entry.fila.modification_date)

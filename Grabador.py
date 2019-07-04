from BD import BD


class Grabador:

    def __init__(self):
        self.bd_destino = BD('blog', 'blog', 'blog')
        self.sql_insert_entry = "insert into entry (identry, handle, descripcion, titulo, creado, cambiado) " \
                                "values (%s, %s, %s, %s, %s, %s)"
        self.sql_insert_tag = 'insert into tag (identry, tag) values (%s, %s)'

    def ejecutar(self, entry_id, handle, descripcion="", titulo="", creado=None, cambiado=None, tags=None):
        cursor = self.bd_destino.cursor()
        try:
            cursor.execute(self.sql_insert_entry, (entry_id, handle, descripcion, titulo, creado, cambiado))
            self.bd_destino.commit()
            entry_id = cursor.lastrowid
            for tag in tags:
                try:
                    cursor_tag = self.bd_destino.cursor()
                    cursor_tag.execute(self.sql_insert_tag, (entry_id, tag))
                    self.bd_destino.commit()
                except Exception as variable:
                    print('tag: %s' % variable)
        except Exception as variable:
            print('entry: %s' % variable)


class Blog(Grabador):

    def __init__(self, entry):
        super().__init__()
        self.entry = entry

    def grabar(self):
        self.ejecutar(self.entry.fila.id, self.entry.handle, self.entry.texto, self.entry.titulo,
                      self.entry.fila.creation_date, self.entry.fila.modification_date, self.entry.tags)


class File(Grabador):

    def __init__(self, entry):
        super().__init__()
        self.entry = entry

    def grabar(self):
        self.ejecutar(0, self.entry.handle, self.entry.texto, self.entry.titulo, None, None, self.entry.tags)

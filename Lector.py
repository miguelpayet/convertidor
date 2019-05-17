from BD import BD
from Convertidor import Convertidor


class Lector:

    def __init__(self):
        self.bd = BD("cuerpotaxi", "cuerpotaxi", "cuerpotaxi")
        self.sql = ""
        self.init_sql()

    def init_sql(self):
        self.sql = """ select e.id, creation_date, modification_date, d1.handle, d1.value titulo, d2.value texto 
        from sym_entries e
        join sym_entries_data_1 d1 on e.id=d1.entry_id 
        join sym_entries_data_2 d2 on e.id=d2.entry_id"""  # where e.id = 14

    def leer_entries(self):
        cursor = self.bd.cursor(named_tuple=True)
        cursor.execute(self.sql)
        for fila in cursor:
            print(fila.id)
            cnv = Convertidor(fila)
            cnv.convertir()

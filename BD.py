import mysql.connector


class BD(object):

    def __init__(self, esquema, usuario, password):
        self.host = 'uuubuntu'
        self.esquema = esquema
        self.password = password
        self.usuario = usuario
        self.cnx = mysql.connector.connect(user=self.usuario, password=self.password,
                                           host=self.host,
                                           database=self.esquema)

    def commit(self):
        return self.cnx.commit()

    def cursor(self, buffered=None, named_tuple=None):
        return self.cnx.cursor(buffered=buffered, named_tuple=named_tuple)

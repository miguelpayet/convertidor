from Lector import Lector
from LectorFile import LectorFile
import sys

cnv = None
if sys.argv[1] == "bd":
    cnv = Lector()
elif sys.argv[1] == "file":
    cnv = LectorFile(sys.argv[2])
if cnv is not None:
    cnv.leer_entries()

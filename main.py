from Lector import Lector
from LectorFile import LectorFile
import sys

cnv = None
if sys.argv[0] == "bd":
    cnv = Lector()
elif sys.argv[1] == "file":
    cnv = LectorFile(sys.argv[1])
if cnv is not None:
    cnv.leer_entries()

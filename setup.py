import cx_Freeze
import sys
import os
import matplotlib

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base='Win32GUI'

executables = [cx_Freeze.Executable("FaceRec.py",base=None)]

cx_Freeze.setup(
    name = "Pong",
    options = {"build_exe": {"packages":["numpy"]}},
    version = "0.01",
    description = "Trying to get this to work",
    executables = executables)

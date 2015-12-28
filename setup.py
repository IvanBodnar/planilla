# Este es el que funciona (sin la ventana)
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["sqlalchemy.dialects", "PyQt4.QtSql"]}
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

setup(
    name='Planilla',
    version=0.1,
    description='Planilla',
    options={"build_exe": build_exe_options},
    executables=[Executable('callPlanilla.pyw', base=base)]
)
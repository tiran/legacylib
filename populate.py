#!/usr/bin/python3
import collections
import os
import shutil

from setuptools import setup

Module = collections.namedtuple("Module", "name pyfiles cfiles doc deps")

SETUP_PY = """\
from setuptools import setup

setup(
    name="{name}",
    version="3.7.3",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSFL",
    package_dir={{"": "src"}},
    py_modules=["{name}"],
)
"""

SETUP_CFG = """\
[bdist_wheel]
universal = {universal}

[metadata]
license_file = LICENSE
"""


modules = [
    Module(
        name="aifc",
        pyfiles=["Lib/aifc.py"],
        cfiles=[],
        doc="Doc/library/aifc.rst",
        deps=["audioop"],
    ),
    Module(
        name="asynchat",
        pyfiles=["Lib/asynchat.py"],
        cfiles=[],
        doc="Doc/library/asynchat.rst",
        deps=["asyncore"],
    ),
    Module(
        name="asyncore",
        pyfiles=["Lib/asyncore.py"],
        cfiles=[],
        doc="Doc/library/asyncore.rst",
        deps=[],
    ),
    Module(
        name="audioop",
        pyfiles=[],
        cfiles=["Modules/audioop.c"],
        doc="Doc/library/audioop.rst",
        deps=[],
    ),
    Module(
        name="binhex",
        pyfiles=["Lib/binhex.py"],
        cfiles=[],
        doc="Doc/library/binhex.rst",
        deps=[],
    ),
    Module(
        name="cgi",
        pyfiles=["Lib/cgi.py", "Lib/cgitb.py"],
        cfiles=[],
        doc="Doc/library/cgi.rst",
        deps=[],
    ),
    Module(
        name="chunk",
        pyfiles=["Lib/chunk.py"],
        cfiles=[],
        doc="Doc/library/chunk.rst",
        deps=[],
    ),
    Module(
        name="colorsys",
        pyfiles=["Lib/colorsys.py"],
        cfiles=[],
        doc="Doc/library/colorsys.rst",
        deps=[],
    ),
    Module(
        name="crypt",
        pyfiles=["Lib/crypt.py"],
        cfiles=["Modules/_cryptmodule.c"],
        doc="Doc/library/crypt.rst",
        deps=[],
    ),
    Module(
        name="fileinput",
        pyfiles=["Lib/fileinput.py"],
        cfiles=[],
        doc="Doc/library/fileinput.rst",
        deps=[],
    ),
    Module(
        name="formatter",
        pyfiles=["Lib/formatter.py"],
        cfiles=[],
        doc="Doc/library/formatter.rst",
        deps=[],
    ),
    Module(
        name="imghdr",
        pyfiles=["Lib/imghdr.py"],
        cfiles=[],
        doc="Doc/library/imghdr.rst",
        deps=[],
    ),
    Module(
        name="msilib",
        pyfiles=[
            "Lib/msilib/__init__.py",
            "Lib/msilib/schema.py",
            "Lib/msilib/sequence.py",
            "Lib/msilib/text.py",
        ],
        cfiles=["PC/_msi.c"],
        doc="Doc/library/msilib.rst",
        deps=[],
    ),
    Module(
        name="nis",
        pyfiles=[],
        cfiles=["Modules/nismodule.c"],
        doc="Doc/library/nis.rst",
        deps=[],
    ),
    Module(
        name="nntplib",
        pyfiles=["Lib/nntplib.py"],
        cfiles=[],
        doc="Doc/library/nntplib.rst",
        deps=[],
    ),
    Module(
        name="ossaudiodev",
        pyfiles=[],
        cfiles=["Modules/ossaudiodev.c"],
        doc="Doc/library/ossaudiodev.rst",
        deps=[],
    ),
    Module(
        name="pipes",
        pyfiles=["Lib/pipes.py"],
        cfiles=[],
        doc="Doc/library/pipes.rst",
        deps=[],
    ),
    Module(
        name="smtpd",
        pyfiles=["Lib/smtpd.py"],
        cfiles=[],
        doc="Doc/library/smtpd.rst",
        deps=[],
    ),
    Module(
        name="sndhdr",
        pyfiles=["Lib/sndhdr.py"],
        cfiles=[],
        doc="Doc/library/sndhdr.rst",
        deps=[],
    ),
    Module(
        name="spwd",
        pyfiles=[],
        cfiles=["Modules/spwdmodule.c", "Modules/clinic/spwdmodule.c.h"],
        doc="Doc/library/spwd.rst",
        deps=[],
    ),
    Module(
        name="sunau",
        pyfiles=["Lib/sunau.py"],
        cfiles=[],
        doc="Doc/library/sunau.rst",
        deps=["audioop"],
    ),
    Module(
        name="uu", pyfiles=["Lib/uu.py"], cfiles=[], doc="Doc/library/uu.rst", deps=[]
    ),
    Module(
        name="xdrlib",
        pyfiles=["Lib/xdrlib.py"],
        cfiles=[],
        doc="Doc/library/xdrlib.rst",
        deps=[],
    ),
]

for module in modules:
    os.makedirs(f"{module.name}/src", exist_ok=True)
    shutil.copy(f"cpython/LICENSE", f"{module.name}/")
    shutil.copy(f"cpython/{module.doc}", f"{module.name}/README.rst")

    if module.name == "msilib":
        os.makedirs("msilib/src/msilib", exist_ok=True)
        shutil.rmtree("msilib/tools", ignore_errors=True)
        # os.makedirs("msilib/tools", exist_ok=True)
        shutil.copytree("cpython/Tools/msi", "msilib/tools")

    for pyfile in module.pyfiles:
        target = pyfile.replace("Lib/", "")
        shutil.copy(f"cpython/{pyfile}", f"{module.name}/src/{target}")

    for cfile in module.cfiles:
        shutil.copy(f"cpython/{cfile}", f"{module.name}/src/")

    with open(f"{module.name}/setup.cfg", "w") as f:
        f.write(SETUP_CFG.format(universal=1 if not module.cfiles else 0))

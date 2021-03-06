#!/usr/bin/python3
import collections
import os
import shutil

Module = collections.namedtuple(
    "Module",
    "name pyfiles cfiles testfiles doc install_requires tests_require"
)

SETUP_PY = """\
from setuptools import setup

setup(
    name="{name}",
    version="3.10.0a1",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSF license"
    package_dir={{"": "src"}},
    {extra}
    classifiers=[
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved :: Python Software Foundation License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
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
        testfiles=["Lib/test/test_aifc.py"],
        doc="Doc/library/aifc.rst",
        install_requires=["audioop"],
        tests_require=["legacytest"],
    ),
    Module(
        name="asynchat",
        pyfiles=["Lib/asynchat.py"],
        cfiles=[],
        testfiles=["Lib/test/test_asynchat.py"],
        doc="Doc/library/asynchat.rst",
        install_requires=["asyncore"],
        tests_require=[],
    ),
    Module(
        name="asyncore",
        pyfiles=["Lib/asyncore.py"],
        cfiles=[],
        testfiles=["Lib/test/test_asyncore.py"],
        doc="Doc/library/asyncore.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="audioop",
        pyfiles=[],
        cfiles=["Modules/audioop.c"],
        testfiles=["Lib/test/test_audioop.py"],
        doc="Doc/library/audioop.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="binhex",
        pyfiles=["Lib/binhex.py"],
        cfiles=[],
        testfiles=["Lib/test/test_binhex.py"],
        doc="Doc/library/binhex.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="cgi",
        pyfiles=["Lib/cgi.py"],
        cfiles=[],
        testfiles=["Lib/test/test_cgi.py"],
        doc="Doc/library/cgi.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="cgitb",
        pyfiles=["Lib/cgitb.py"],
        cfiles=[],
        testfiles=["Lib/test/test_cgitb.py"],
        doc="Doc/library/cgitb.rst",
        install_requires=["cgi"],
        tests_require=[],
    ),
    Module(
        name="chunk",
        pyfiles=["Lib/chunk.py"],
        cfiles=[],
        testfiles=[],  # XXX: no tests
        doc="Doc/library/chunk.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="crypt",
        pyfiles=["Lib/crypt.py"],
        cfiles=["Modules/_cryptmodule.c"],
        testfiles=["Lib/test/test_crypt.py"],
        doc="Doc/library/crypt.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="fileinput",
        pyfiles=["Lib/fileinput.py"],
        cfiles=[],
        testfiles=["Lib/test/test_fileinput.py"],
        doc="Doc/library/fileinput.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="formatter",
        pyfiles=["Lib/formatter.py"],
        cfiles=[],
        testfiles=[],  # XXX: no tests
        doc="Doc/library/formatter.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="imghdr",
        pyfiles=["Lib/imghdr.py"],
        cfiles=[],
        testfiles=["Lib/test/test_imghdr.py"],
        doc="Doc/library/imghdr.rst",
        install_requires=[],
        tests_require=[],
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
        testfiles=["Lib/test/test_msilib.py"],
        doc="Doc/library/msilib.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="nis",
        pyfiles=[],
        cfiles=["Modules/nismodule.c"],
        testfiles=["Lib/test/test_nis.py"],
        doc="Doc/library/nis.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="nntplib",
        pyfiles=["Lib/nntplib.py"],
        cfiles=[],
        testfiles=["Lib/test/test_nntplib.py"],
        doc="Doc/library/nntplib.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="ossaudiodev",
        pyfiles=[],
        cfiles=["Modules/ossaudiodev.c"],
        testfiles=["Lib/test/test_ossaudiodev.py"],
        doc="Doc/library/ossaudiodev.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="pipes",
        pyfiles=["Lib/pipes.py"],
        cfiles=[],
        testfiles=["Lib/test/test_pipes.py"],
        doc="Doc/library/pipes.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="smtpd",
        pyfiles=["Lib/smtpd.py"],
        cfiles=[],
        testfiles=["Lib/test/test_smtpd.py"],
        doc="Doc/library/smtpd.rst",
        install_requires=[],
        tests_require=["legacytest"],
    ),
    Module(
        name="sndhdr",
        pyfiles=["Lib/sndhdr.py"],
        cfiles=[],
        testfiles=["Lib/test/test_sndhdr.py"],
        doc="Doc/library/sndhdr.rst",
        install_requires=[],
        tests_require=["legacytest"],
    ),
    Module(
        name="spwd",
        pyfiles=[],
        cfiles=["Modules/spwdmodule.c", "Modules/clinic/spwdmodule.c.h"],
        testfiles=["Lib/test/test_spwd.py"],
        doc="Doc/library/spwd.rst",
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="sunau",
        pyfiles=["Lib/sunau.py"],
        cfiles=[],
        doc="Doc/library/sunau.rst",
        testfiles=["Lib/test/test_sunau.py"],
        install_requires=["audioop"],
        tests_require=["legacytest"],
    ),
    Module(
        name="uu",
        pyfiles=["Lib/uu.py"],
        cfiles=[],
        doc="Doc/library/uu.rst",
        testfiles=["Lib/test/test_uu.py"],
        install_requires=[],
        tests_require=[],
    ),
    Module(
        name="xdrlib",
        pyfiles=["Lib/xdrlib.py"],
        cfiles=[],
        testfiles=["Lib/test/test_xdrlib.py"],
        doc="Doc/library/xdrlib.rst",
        install_requires=[],
        tests_require=[],
    ),
    # TODO: test data module
    Module(
        name="legacytest",
        pyfiles=[],
        cfiles=[],
        testfiles=[],
        doc=None,
        install_requires=[],
        tests_require=[],
    ),
]


for module in modules:
    os.makedirs(f"{module.name}/src", exist_ok=True)
    shutil.copy(f"cpython/LICENSE", f"{module.name}/")
    if module.doc is not None:
        basename = os.path.basename(module.doc)
        shutil.copy(f"cpython/{module.doc}", f"docs/{basename}")
        try:
            os.unlink(f"{module.name}/README.rst")
        except FileNotFoundError:
            pass
        os.symlink(f"../docs/{basename}", f"{module.name}/README.rst")

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

    if len(module.testfiles) == 1:
        shutil.copy(f"cpython/{module.testfiles[0]}", f"{module.name}/tests.py")
    else:
        for testfile in module.testfiles:
            shutil.copy(f"cpython/{testfile}", f"{module.name}")

    with open(f"{module.name}/setup.cfg", "w") as f:
        f.write(SETUP_CFG.format(universal=1 if not module.cfiles else 0))

for sphinxext in ['suspicious', 'pyspecific']:
    shutil.copy(f"cpython/Doc/tools/extensions/{sphinxext}.py", "docs/")

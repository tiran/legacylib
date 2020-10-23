import os
import shlex
import sysconfig

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class NISBuildExt(build_ext):
    def build_extensions(self):
        libraries = []
        includes_dirs = []
        library_dirs = []

        lib_search_dirs = self.compiler.library_dirs + [
            "/lib64",
            "/usr/lib64",
            "/lib",
            "/usr/lib",
        ]

        if self.compiler.find_library_file(lib_search_dirs, "nsl"):
            libraries.append("nsl")
        else:
            nsl_dirs = [
                os.path.join(lib_dir, "nsl") for lib_dir in lib_search_dirs
            ]
            libnsl = self.compiler.find_library_file(nsl_dirs, "nsl")
            if libnsl is not None:
                library_dirs.append(os.path.dirname(libnsl))
                libraries.append("nsl")

        if self.compiler.find_library_file(lib_search_dirs, "tirpc"):
            libraries.append("tirpc")

        for inc_dir in self.compiler.include_dirs + ["/usr/include"]:
            nsl_dir = os.path.join(inc_dir, "nsl")
            if os.path.isfile(os.path.join(nsl_dir, "rpcsvc/yp_prot.h")):
                includes_dirs.append(nsl_dir)
            tirpc_dir = os.path.join(inc_dir, "tirpc")
            if os.path.isfile(os.path.join(tirpc_dir, "rpc/rpc.h")):
                includes_dirs.append(tirpc_dir)

        for ext in self.extensions:
            ext.libraries[:] = libraries
            ext.library_dirs[:] = library_dirs
            ext.include_dirs[:] = includes_dirs

        super().build_extensions()


setup(
    name="nis",
    version="3.8.0a4",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSF license",
    package_dir={"": "src"},
    cmdclass={"build_ext": NISBuildExt},
    ext_modules=[Extension("nis", sources=["src/nismodule.c"])],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved :: Python Software Foundation License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
)

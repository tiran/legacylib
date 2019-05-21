from setuptools import setup, Extension

setup(
    name="spwd",
    version="3.8.0a4",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSFL",
    package_dir={"": "src"},
    ext_modules=[Extension("spwd", sources=["src/spwdmodule.c"])],
)

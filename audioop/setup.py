from setuptools import setup, Extension

setup(
    name="audioop",
    version="3.7.3",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSFL",
    package_dir={"": "src"},
    ext_modules=[Extension("audioio", sources=["src/audioop.c"])],
)

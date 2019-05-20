from setuptools import setup

setup(
    name="asynchat",
    version="3.7.3",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSFL",
    package_dir={"": "src"},
    py_modules=["asynchat"],
    install_requires=["asynchat"],
)

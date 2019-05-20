from setuptools import setup

setup(
    name="aifc",
    version="3.7.3",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSFL",
    package_dir={"": "src"},
    py_modules=["aifc"],
    install_requires=["audioop"],
)

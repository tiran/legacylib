from setuptools import setup

setup(
    name="smtpd",
    version="3.8.0a4",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSFL",
    package_dir={"": "src"},
    py_modules=["smtpd"],
    tests_require=["asyncore"],
)

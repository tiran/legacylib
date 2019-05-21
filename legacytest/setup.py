from setuptools import setup

setup(
    name="legacytest",
    version="3.8.0a4",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSFL",
    package_dir={"": "src"},
    packages=["legacytest"],
    include_package_data=True,
)

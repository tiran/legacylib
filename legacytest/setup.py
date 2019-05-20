from setuptools import setup

setup(
    name="legacytest",
    version="3.7.3",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSFL",
    package_dir={"": "src"},
    packages=["legacytest"],
    include_package_data=True,
)

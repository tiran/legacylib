from setuptools import setup

setup(
    name="sndhdr",
    version="3.8.0a4",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSF license",
    package_dir={"": "src"},
    py_modules=["sndhdr"],
    tests_require=["legacytest"],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved :: Python Software Foundation License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
)

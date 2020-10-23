from setuptools import setup

setup(
    name="asynchat",
    version="3.9.0",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSF license",
    package_dir={"": "src"},
    py_modules=["asynchat"],
    install_requires=["asynchat"],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved :: Python Software Foundation License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
)

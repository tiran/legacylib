from setuptools import setup, Extension

setup(
    name="ossaudiodev",
    version="3.9.0",
    author="CPython",
    author_email="python-dev@python.org",
    url="https://www.python.org/",
    license="PSF license",
    package_dir={"": "src"},
    ext_modules=[Extension("ossaudiodev", sources=["src/ossaudiodev.c"])],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved :: Python Software Foundation License",
        "Natural Language :: English",
        "Programming Language :: C",
        "Topic :: Software Development",
    ],
)

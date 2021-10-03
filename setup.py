from setuptools import setup

with open("README.md") as f:
    long_description = f.read()


setup(
    name="languagecodes",
    version="1.1.1",
    description="A library that normalises language codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="names languages iso ",
    author="Friedrich Lindenberg",
    author_email="friedrich@pudo.org",
    url="http://github.com/alephdata/languagecodes",
    license="MIT",
    packages=["languagecodes"],
    namespace_packages=[],
    include_package_data=True,
    package_data={"languagecodes": ["py.typed", "iso-639-3.tab"]},
    zip_safe=False,
    test_suite="nose.collector",
    install_requires=["banal >= 1.0.0, < 2.0.0"],
    extras_require={
        "dev": [
            "wheel>=0.29.0",
            "twine",
            "mypy",
            "flake8>=2.6.0",
            "nose",
            "coverage>=4.1",
        ]
    },
)

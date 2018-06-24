from setuptools import setup, find_packages

setup(
    name='languagecodes',
    version='1.0.3',
    description="A library that normalises language codes",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='names languages iso ',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    url='http://github.com/alephdata/languagecodes',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[],
    extras_require={
        'dev': [
            'wheel>=0.29.0',
            'twine',
            'flake8>=2.6.0',
            'nose',
            'coverage>=4.1'
        ]
    }
)

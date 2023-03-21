from setuptools import setup, find_packages


setup(name = 'pytest-course-project',
        version = '1.0',
        description = 'A project developed during a pytest course',
        author = 'Mane',
        author_email = 'mane.poghosian@gmail.com',
        packages = find_packages(),
        install_requires = [
            "pytest == 7.2.1",
            "python == 3.10.6",
            "requests == 2.28.2",
            "pytest-html == 3.2.0"
        ]
    )

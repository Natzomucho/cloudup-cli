from setuptools import setup
setup(
    name = 'ccli',
    version = '0.1.0',
    packages = ['ccli'],
    entry_points = {
        'console_scripts': [
            'ccli=ccli.__main__:main'
        ]
    })

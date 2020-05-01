from setuptools import setup
setup(
    name = 'cloudup-cli',
    version = '0.1.0',
    packages = ['cloudup-cli'],
    entry_points = {
        'console_scripts': [
            'cldup = cloudup-cli.__main__:main'
        ]
    })

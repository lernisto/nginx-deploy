from setuptools import setup

setup(
    name='nsite',
    version='0.1',
    py_modules=['nsite'],
    install_requires=[
        'Click',
        'Jinja2',
    ],
    entry_points='''
        [console_scripts]
        newsite=nsite.cli:newsite
    ''',
)

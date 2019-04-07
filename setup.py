from setuptools import setup

setup(
    name='AudiOk',
    version='0.1',
    py_modules=['aok'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        aok=aok:aok
    '''
)
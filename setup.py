from setuptools import setup, find_packages

setup(
    name='yourscript',
    version='0.1',
    packages = find_packages(),

    install_requires=[
        'Click',
    ],
    entry_points= '''
        [console_scripts]
        yourscript=task.scripts.yourscript:cli

        ''',

)

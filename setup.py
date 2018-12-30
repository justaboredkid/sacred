from setuptools import setup

setup(
    name='sacred_tui',
    version='0.1',
    description='Python library for ASCII art import and TUI development',
    url='https://github.com/justaboredkid/sacred',
    author='justaboredkid',
    author_email='29010153+justaboredkid@users.noreply.github.com',
    license='GNU GPLv3',
    packages=['sacred'],
    install_requires=[
        'blessed',
    ],
    zip_safe=False)

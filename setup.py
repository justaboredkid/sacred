from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sacred_tui',
    version='0.2',
    description='Python library for ASCII art import and TUI development',
    url='https://github.com/justaboredkid/sacred',
    author='justaboredkid',
    author_email='29010153+justaboredkid@users.noreply.github.com',
    license='GNU GPLv3',
    packages=['sacred'],
    install_requires=[
        'blessed',
    ],
    classifiers=[
        'OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': ['asciigen = asciigen:main'],
    })

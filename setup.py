from setuptools import setup, find_packages

setup(
    name='db4e-systemd',
    version='1.0',
    packages=find_packages(),
    author='Nadim-Daniel Ghaznavi',
    license='GPLv3',
    description='Lightweight systemd wrapper for Python tools',
    url='https://github.com/NadimGhaznavi/db4e-systemd',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
    ]
)


from setuptools import setup, find_packages

setup(
    name='db4e-systemd',
    version='1.2.3',
    author='Nadim-Daniel Ghaznavi',
    description='A lightweight systemctl wrapper for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NadimGhaznavi/db4e-systemd',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.7',
)


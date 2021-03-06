try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

config = {
    'description': 'A suite of tools for processing and analysing NMR spectra in Python.',
    'author': 'Johann Eicher',
    'author_email': 'johanneicher@gmail.com',
    'url': 'fake.address.com',
    #'download_url': 'Where to download it.',
    'version': '0.1',
    'install_requires': requirements,
    'packages': ['nmrpy'],
    'license': 'New BSD',
    #'scripts': [],
    'name': 'nmrpy'
}

setup(**config)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timefred', 'timefred.action']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.1.0,<2.0.0', 'click>=7.1.2,<8.0.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'timefred',
    'version': '0.1.0',
    'description': 'Not a silly simple time tracker',
    'long_description': None,
    'author': 'Gilad Barnea',
    'author_email': 'giladbrn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

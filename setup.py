# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lotr', 'lotr.responses']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.0,<4.0', 'backoff>=2.0,<3.0', 'requests>=2.0,<3.0']

setup_kwargs = {
    'name': 'lotr-sdk',
    'version': '1.0.0',
    'description': 'SDK for Lord of The Rings',
    'long_description': '',
    'author': '',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

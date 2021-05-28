# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gpt3_api']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0', 'asyncinit>=0.2.4,<0.3.0', 'ujson>=4.0.2,<5.0.0']

setup_kwargs = {
    'name': 'gpt3-api',
    'version': '0.1.0',
    'description': 'Wrapper for OpenAI GPT-3 API.',
    'long_description': None,
    'author': 'OpenGPT',
    'author_email': 'opengpt@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

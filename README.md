[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![PyPI](https://img.shields.io/pypi/v/freshworks?color=darkred)](https://pypi.org/project/freshworks/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/freshworks?label=Python%20Version&logo=python&logoColor=yellow)](https://pypi.org/project/freshworks/)
[![PyPI - License](https://img.shields.io/pypi/l/freshworks?color=green)](https://github.com/AceofSpades5757/freshworks/blob/main/LICENSE)

[![Tests](https://github.com/AceofSpades5757/freshworks/actions/workflows/test.yml/badge.svg)](https://github.com/AceofSpades5757/freshworks/actions/workflows/test.yml)

[![Read the Docs](https://img.shields.io/readthedocs/freshworks)](https://freshworks.readthedocs.io/en/latest/)

# Description

Python client library for interacting with Freshworks products.

# Installation

`pip install freshworks`

This will install all available packages for working with those Freshworks products.

- `freshdesk`
- `freshcaller`

# Usage

## Basic

```python
from freshdesk import Client


fd = Client(domain='mydomain', api_key='MY_API_KEY')
```

## Different Plan

```python
from freshdesk import Client
from freshdesk import Plan


fd = Client(
    domain='mydomain',
    api_key='MY_API_KEY',
    plan=Plan.ESTATE,
)
```

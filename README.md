# Quick Start

Ecosystem Plugin for Taraxa support in Ape

## Dependencies

* [python3](https://www.python.org/downloads) version 3.8 or greater, python3-dev

## Installation

### via `ape`

You can install this plugin using `ape`:

```bash
ape plugins install taraxa
```

or via config file:

```yaml
# ape-config.yaml
plugins:
  - name: taraxa
```

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-taraxa
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/nhaga/ape-taraxa.git
cd ape-taraxa
python3 setup.py install
```

## Quick Usage

Installing this plugin adds support for the Taraxa ecosystem:

```bash
ape console --network taraxa:mainnet
```

## Development

Comments, questions, criticisms and pull requests are welcomed.

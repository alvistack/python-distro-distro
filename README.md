Distro - an OS platform information API
=======================================

[![CI Status](https://github.com/python-distro/distro/workflows/CI/badge.svg)](https://github.com/python-distro/distro/actions/workflows/ci.yaml)
[![PyPI version](http://img.shields.io/pypi/v/distro.svg)](https://pypi.python.org/pypi/distro)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/distro.svg)](https://img.shields.io/pypi/pyversions/distro.svg)
[![Code Coverage](https://codecov.io/github/python-distro/distro/coverage.svg?branch=master)](https://codecov.io/github/python-distro/distro?branch=master)
[![Is Wheel](https://img.shields.io/pypi/wheel/distro.svg?style=flat)](https://pypi.python.org/pypi/distro)
[![Latest Github Release](https://readthedocs.org/projects/distro/badge/?version=stable)](http://distro.readthedocs.io/en/latest/)
[![Join the chat at https://gitter.im/python-distro/distro](https://badges.gitter.im/python-distro/distro.svg)](https://gitter.im/python-distro/distro?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

`distro` provides information about the
OS distribution it runs on, such as a reliable machine-readable ID, or
version information.

It is the recommended replacement for Python's original
[`platform.linux_distribution`](https://docs.python.org/3.7/library/platform.html#platform.linux_distribution)
function (removed in Python 3.8). It also provides much more functionality
which isn't necessarily Python bound, like a command-line interface.

Distro currently supports Linux and BSD based systems but [Windows and OS X support](https://github.com/python-distro/distro/issues/177) is also planned.

For Python 2.6 support, see https://github.com/python-distro/distro/tree/python2.6-support

## Installation

Installation of the latest released version from PyPI:

```shell
pip install distro
```

Installation of the latest development version:

```shell
pip install https://github.com/python-distro/distro/archive/master.tar.gz
```


## Usage

```bash
$ distro
Name: Antergos Linux
Version: 2015.10 (ISO-Rolling)
Codename: ISO-Rolling

$ distro -j
{
    "codename": "ISO-Rolling",
    "id": "antergos",
    "like": "arch",
    "version": "16.9",
    "version_parts": {
        "build_number": "",
        "major": "16",
        "minor": "9"
    }
}


$ python
>>> import distro
>>> distro.linux_distribution(full_distribution_name=False)
('centos', '7.1.1503', 'Core')
```


## Documentation

On top of the aforementioned API, several more functions are available. For a complete description of the
API, see the [latest API documentation](http://distro.readthedocs.org/en/latest/).

## Background

An alternative implementation became necessary because Python 3.5 deprecated
this function, and Python 3.8 removed it altogether. Its predecessor function
[`platform.dist`](https://docs.python.org/3.7/library/platform.html#platform.dist)
was already deprecated since Python 2.6 and removed in Python 3.8. Still, there
are many cases in which access to that information is needed. See [Python issue
1322](https://bugs.python.org/issue1322) for more information.

The `distro` package implements a robust and inclusive way of retrieving the
information about a distribution based on new standards and old methods,
namely from these data sources (from high to low precedence):

* The os-release file `/etc/os-release` if present, with a fall-back on `/usr/lib/os-release` if needed.
* The output of the `lsb_release` command, if available.
* The distro release file (`/etc/*(-|_)(release|version)`), if present.
* The `uname` command for BSD based distrubtions.


## Python and Distribution Support

`distro` is supported and tested on Python 3.6+ and PyPy and on any
distribution that provides one or more of the data sources covered.

This package is tested with test data that mimics the exact behavior of the data sources of [a number of Linux distributions](https://github.com/python-distro/distro/tree/master/tests/resources/distros).


## Testing

```shell
git clone git@github.com:python-distro/distro.git
cd distro
pip install tox
tox
```


## Contributions

Pull requests are always welcome to deal with specific distributions or just
for general merriment.

See [CONTRIBUTIONS](https://github.com/python-distro/distro/blob/master/CONTRIBUTING.md) for contribution info.

Reference implementations for supporting additional distributions and file
formats can be found here:

* https://github.com/saltstack/salt/blob/develop/salt/grains/core.py#L1172
* https://github.com/chef/ohai/blob/master/lib/ohai/plugins/linux/platform.rb
* https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/facts/system/distribution.py
* https://github.com/puppetlabs/facter/blob/master/lib/src/facts/linux/os_linux.cc

## Package manager distributions

* https://src.fedoraproject.org/rpms/python-distro
* https://www.archlinux.org/packages/community/any/python-distro/
* https://launchpad.net/ubuntu/+source/python-distro
* https://packages.debian.org/stable/python3-distro
* https://packages.gentoo.org/packages/dev-python/distro
* https://pkgs.org/download/python3-distro
* https://slackbuilds.org/repository/14.2/python/python-distro/

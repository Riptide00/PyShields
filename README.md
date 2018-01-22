# PYSHIELDS

![](http://img.shields.io/badge/py-shields-lightgrey.svg?) ![](http://img.shields.io/badge/python3-supported-green.svg?) ![](http://img.shields.io/badge/python2-supported-green.svg?)

## Description

Unofficial python wrapper for the [shields.io](https://shields.io) public API.

## Usage

**in the command line:**

    python shield.py [-h] subject status color

    positional arguments:
      subject     Shield text left.
      status      Shield text right.
      color       Shield color right.

    optional arguments:
      -h, --help  show this help message and exit

**in a script:**

	import shield
    
    new_shield = shield.Static("foo", "bar", "FF00FF")
    print(new_shield.generate())

## Changelog

- v1.0.0: Initial release.

## Credits

- The wonderfull maker(s) of [shields.io](https://shields.io)
# PYSHIELDS

![](http://img.shields.io/badge/py-shields-lightgrey.svg?) ![](http://img.shields.io/badge/python3-supported-green.svg?) ![](http://img.shields.io/badge/python2-supported-green.svg?)

## Description

Unofficial python wrapper for the [shields.io](https://shields.io) public API.

## Usage

**in the command line:**

	python3 pyshields <subject> <status> <color> 

**in a script:**

	import shield
    
    new_shield = shield.Static("foo", "bar", "FF00FF")
    print(new_shield.generate())

## Changelog

- v1.0.0: Initial release.

## Credits

- The wonderfull maker(s) of [shields.io](https://shields.io)
# PYSHIELDS

![](http://img.shields.io/badge/py-shields-lightgrey.svg?) ![](http://img.shields.io/badge/python3-supported-green.svg?) ![](http://img.shields.io/badge/python2-supported-green.svg?) ![](https://img.shields.io/badge/dynamic/json.svg?uri=https://raw.githubusercontent.com/Riptide00/PyShields/master/test.json&label=version&query=$.version&colorB=10ADED)

## Description

Unofficial python wrapper for the [shields.io](https://shields.io) public API.

## Usage

**in the command line:**

      usage: shield.py [-h] [--style STYLE] [--label LABEL] [--logo LOGO]
                   [--logoWidth LOGOWIDTH] [--linkA LINKA] [--linkB LINKB]
                   [--colorA COLORA] [--colorB COLORB] [--maxAge MAXAGE]
                   subject status color

      positional arguments:
        subject               Shield text left.
        status                Shield text right.
        color                 Right side color.

      optional arguments:
        -h, --help            show this help message and exit
        --style STYLE         Shield style.
        --label LABEL         Left text override.
        --logo LOGO           Left side logo.
        --logoWidth LOGOWIDTH
                              Logo space width.
        --linkA LINKA         Left side link.
        --linkB LINKB         Right side link.
        --colorA COLORA       Left side color override.
        --colorB COLORB       Right side color override.
        --maxAge MAXAGE       Cache time in seconds.
  
**in a script:**

    import shield

    static_shield = shield.Static("foo", "bar", "FF00FF")
    print(static_shield.generate())

    test_url = "https://raw.githubusercontent.com/Riptide00/PyShields/master/test.json"
    dynamic_shield = shield.Dynamic(test_url, "version", "$.version", "10ADED")
    print(dynamic_shield.generate())




## Roadmap

- [x] Static shields.
- [x] Dynamic shields.
- [ ] Add dynamic shield generation from the cli.


## Changelog

- v1.0.0: Initial release.

## Credits

- The wonderfull maker(s) of [shields.io](https://shields.io)
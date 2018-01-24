# PYSHIELDS

![](http://img.shields.io/badge/py-shields-lightgrey.svg?) ![](http://img.shields.io/badge/python3-supported-green.svg?) ![](http://img.shields.io/badge/python2-supported-green.svg?) ![](https://img.shields.io/badge/dynamic/json.svg?uri=https://raw.githubusercontent.com/Riptide00/PyShields/master/test.json&label=version&query=$.version&colorB=10ADED)

## Description

Unofficial python wrapper for the [shields.io](https://shields.io) public API.

## Usage

**in the command line:**

        usage: shield.py [-h] [--style STYLE] [--label LABEL] [--logo LOGO]
                   [--logoWidth LOGOWIDTH] [--linkA LINKA] [--linkB LINKB]
                   [--colorA COLORA] [--colorB COLORB] [--maxAge MAXAGE]
                   [--source SOURCE] [--type TYPE]
                   subject status_query color

        positional arguments:
        subject               text left.
        status_query          text right.
        color                 color right.

        optional arguments:
        -h, --help            show this help message and exit
        --style STYLE         badge style
        --label LABEL         text left
        --logo LOGO           logo
        --logoWidth LOGOWIDTH
                              logo space width
        --linkA LINKA         link left
        --linkB LINKB         link right
        --colorA COLORA       color left
        --colorB COLORB       color right
        --maxAge MAXAGE       cache time in seconds
        --source SOURCE       source
        --type TYPE           type (default: json)

        > python shield.py foo bar green
        http://img.shields.io/badge/foo-bar-green.svg

        > python shield.py version $.version 10ADED --source=https://raw.githubusercontent.com/Riptide00/PyShields/master/test.json
        http://img.shields.io/badge/dynamic/json.svg?uri=https://raw.githubusercontent.com/Riptide00/PyShields/master/test.json&label=version&query=$.version&colorB=10ADED
  
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
- [x] Add dynamic shield generation from the cli.


## Changelog

- v1.0.0: Initial release.

## Credits

- The wonderfull maker(s) of [shields.io](https://shields.io)
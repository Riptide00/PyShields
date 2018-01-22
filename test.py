#!/usr/bin/env


import shield


def main():
    # Output links to test in a browser or markdown editor.
    print("Simple static shield:")
    test_static()
    print("Test all available styles:")
    test_styles()
    print("Test all available named colors:")
    test_colors()
    print("Test a hex code color:")
    test_color_hex()
    print("Test all available named logos:")
    test_logos()
    print("Test colorA style parameter:")
    test_colorA()
    print("Test colorB style parameter:")
    test_colorB()
    print("Test label style parameter:")
    test_label()
    print("Test multiple style parameters:")
    test_multiple()
    print('\n\nTesting Exceptions:')
    # TODO: Add unittesting for exceptions.


def test_static():
    new_shield = shield.Static("foo", "bar", "red")
    print("![](%s)" % new_shield.generate())


def test_styles():
    for style in shield.Styles:
        new_shield = shield.Static("foo", "bar", "green", style=style)
        print("![](%s)" % new_shield.generate())


def test_colors():
    for color in shield.Colors:
        new_shield = shield.Static("foo", "bar", color)
        print("![](%s)" % new_shield.generate())


def test_color_hex():
    new_shield = shield.Static("foo", "bar", "FF00FF")
    print("![](%s)" % new_shield.generate())


def test_logos():
    for logo in shield.Logos:
        new_shield = shield.Static("foo", "bar", "red", logo=logo)
        print("![](%s)" % new_shield.generate())


def test_colorA():
    new_shield = shield.Static("foo", "bar", "red", colorA="FF00FF")
    print("![](%s)" % new_shield.generate())


def test_colorB():
    new_shield = shield.Static("foo", "bar", "red", colorB="FF00FF")
    print("![](%s)" % new_shield.generate())


def test_label():
    new_shield = shield.Static("foo", "bar", "red", label="bar")
    print("![](%s)" % new_shield.generate())

def test_multiple():
    new_shield = shield.Static("foo", "bar", "red", colorA="FF00FF", colorB="FF00FF", label="bar", logo="github")
    print("![](%s)" % new_shield.generate())


if __name__ == '__main__':
    main()

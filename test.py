#!/usr/bin/env


import unittest
import shield


def main():
    # Output links to test in a browser or markdown editor.
    print("Static shields")
    print("--------------")
    print("No options:")
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
    print("Dynamic shields")
    print("---------------")
    print("No options:")
    test_dynamic()


def test_dynamic():
    test_uri = "https://raw.githubusercontent.com/Riptide00/PyShields/master/test.json"
    new_shield = shield.Dynamic(test_uri, "pyshields", "$version", "lightgrey")
    print("![](%s)" % new_shield.generate())


def test_static():
    new_shield = shield.Static("py", "shields", "lightgrey")
    print("![](%s)" % new_shield.generate())


def test_styles():
    for style in shield.Styles:
        new_shield = shield.Static("style", style, "lightgrey", style=style)
        print("![](%s)" % new_shield.generate())


def test_colors():
    for color in shield.Colors:
        new_shield = shield.Static("color", color, color)
        print("![](%s)" % new_shield.generate())


def test_color_hex():
    new_shield = shield.Static("hex", "FF00FF", "FF00FF")
    print("![](%s)" % new_shield.generate())


def test_logos():
    for logo in shield.Logos:
        new_shield = shield.Static("logo", logo, "lightgrey", logo=logo)
        print("![](%s)" % new_shield.generate())


def test_colorA():
    new_shield = shield.Static("color", "a", "lightgrey", colorA="FF00FF")
    print("![](%s)" % new_shield.generate())


def test_colorB():
    new_shield = shield.Static("color", "b", "lightgrey", colorB="FF00FF")
    print("![](%s)" % new_shield.generate())


def test_label():
    new_shield = shield.Static("foo", "bar", "lightgrey", label="label")
    print("![](%s)" % new_shield.generate())


def test_multiple():
    new_shield = shield.Static("git", "hub", "lightgrey", colorA="FF00FF",
                               colorB="FF00FF", label="bar", logo="github")
    print("![](%s)" % new_shield.generate())


class ExceptionTest(unittest.TestCase):
    """Check exceptions."""
    def test_color(self):
        new_shield = shield.Static("foo", "bar", "redr")
        self.assertRaises(ValueError, new_shield.generate)

    def test_hex(self):
        new_shield = shield.Static("foo", "bar", "FFFF")
        self.assertRaises(ValueError, new_shield.generate)

    def test_logo(self):
        new_shield = shield.Static("foo", "bar", "red", logo="foobar")
        self.assertRaises(ValueError, new_shield.generate)

    def test_style(self):
        new_shield = shield.Static("foo", "bar", "red", style="foobar")
        self.assertRaises(ValueError, new_shield.generate)


if __name__ == '__main__':
    print("\nCheck for malformed urls in a markdown editor...\n\n")
    main()
    print("\n\nChecking exceptions...\n\n")
    unittest.main()

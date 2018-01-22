#!/usr/bin/env


import re


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", help="Shield text left.", type=str)
    parser.add_argument("status", help="Shield text right.", type=str)
    parser.add_argument("color", help="Shield color right.", type=str)
    args = parser.parse_args()
    new_shield = Static(args.subject, args.status, args.color)
    print(new_shield.generate())

# Available badge styles.
Styles = ["plastic", "flat", "flat-square", "for-the-badge", "social"]
# Available badge colors.
Colors = ["brightgreen", "green", "yellowgreen", "yellow", "orange", "red", "lightgrey", "blue"]
# Available badge named logos.
Logos = ["appveyor", "bitcoin", "bithound", "discord", "dockbit", "eclipse", "github", "gitter-white",
         "gratipay", "paypal", "postgresql", "scrutinizer", "slack", "sourcegraph", "telegram", "tfs", "travis", "twitter"]


class Static(object):
    """Generate a static shield."""
    def __init__(self, subject, status, color, style=None, label=None,
                 logo=None, logoWidth=None, linkA=None, linkB=None, colorA=None, colorB=None, maxAge=None):
        super(Static, self).__init__()
        # Left column text.
        self.subject = subject
        # Right column text.
        self.status = status
        # Right column color.
        self.color = color
        # Configure other hosts.
        self.url = "http://img.shields.io"
        # Shield style.
        self.style = style
        # Override left label.
        self.label = label
        # Insert a logo.
        self.logo = logo
        # Logo width.
        self.logoWidth = logoWidth
        # Left side link.
        self.linkA = linkA
        # Right side link.
        self.linkB = linkB
        # Override left side color.
        self.colorA = colorA
        # Overide right side color.
        self.colorB = colorB
        # Set the HTTP cache lifetime in secs.
        self.maxAge = maxAge
        # URL format.
        self._str = "%s/badge/%s-%s-%s.svg%s"

    def generate(self):
        """Generate static shield url."""
        _check_color(self.color)
        st = _get_style(self.style, self.label, self.logo, self.logoWidth,
                        self.linkA, self.linkB, self.colorA, self.colorB, self.maxAge)
        return self._str % (self.url, self.subject, self.status, self.color, st)


class Dynamic(object):
    """Generate a dynamic shield."""
    def __init__(self, arg):
        super(Dynamic, self).__init__()
        self.arg = arg


def _get_style(style, label, logo, logoWidth, linkA, linkB, colorA, colorB, maxAge):
    """Generate a parameter string for styling."""
    param = []
    if style:
        _check_style(style)
        param.append("style=%s" % style)
    if label:
        param.append("label=%s" % label)
    if logo:
        _check_logo(logo)
        param.append("logo=%s" % logo)
    if logoWidth:
        param.append("logoWidth=%s" % logoWidth)
    if linkA:
        param.append("link=%s" % linkA)
    if linkB:
        param.append("link=%s" % linkB)
    if colorA:
        param.append("colorA=%s" % colorA)
    if colorB:
        param.append("colorB=%s" % colorB)
    if maxAge:
        param.apped("maxAge=%s" % maxAge)
    if param:
        return "?%s" % "&".join(param)
    else:
        return ''

# Check as many errors before they hit the server.

def _check_style(style):
    """Check if named logo is valid."""
    if not style in Styles:
        raise ValueError("Invalid style: %s" % style)


def _check_color(color):
    """Check if a valid color is passed."""
    if not color in Colors:
        if not _check_hex(color):
            raise ValueError("Invalid color: %s" % color)


def _check_logo(logo):
    # TODO: Add custom logo support.
    if not _check_named_logo(logo):
            raise ValueError("Invalid logo: %s" % logo)


def _check_hex(color):
    """Check if string is a hex color code."""
    if re.search(r'^([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', color):                      
        return True
    else:
        return False    


def _check_custom_logo(logo):
    return False # TODO: Add custom logo support.


def _check_named_logo(logo):
    # Check if a passed named logo is valid.
    if logo in Logos:
        return True
    else:
        return False

if __name__ == '__main__':
    main()

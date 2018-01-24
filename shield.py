#!/usr/bin/env


import re


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", help="text left.", type=str)
    parser.add_argument("status", help="text right.", type=str)
    parser.add_argument("color", help="color right.", type=str)
    parser.add_argument("--style", help="badge style", type=str)
    parser.add_argument("--label", help="text left", type=str)
    parser.add_argument("--logo", help="logo", type=str)
    parser.add_argument("--logoWidth", help="logo space width", type=int)
    parser.add_argument("--linkA", help="link left", type=str)
    parser.add_argument("--linkB", help="link right", type=str)
    parser.add_argument("--colorA", help="color left", type=str)
    parser.add_argument("--colorB", help="color right", type=str)
    parser.add_argument("--maxAge", help="cache time in seconds", type=int)
    args = parser.parse_args()
    new_shield = Static(args.subject, args.status, args.color)
    if args.style:
        new_shield.style = args.style
    if args.label:
        new_shield.label = args.label
    if args.logo:
        new_shield.logo = args.logo
    if args.logoWidth:
        new_shield.logoWidth = args.logoWidth
    if args.linkA:
        new_shield.linkA = args.linkA
    if args.linkB:
        new_shield.linkB = args.linkB
    if args.colorA:
        new_shield.colorA = args.colorA
    if args.colorB:
        new_shield.colorB = args.colorB
    if args.maxAge:
        new_shield.maxAge = args.maxAge
    print(new_shield.generate())


# Available badge styles.
Styles = ["plastic", "flat", "flat-square", "for-the-badge", "social"]
# Available badge colors.
Colors = ["brightgreen", "green", "yellowgreen", "yellow",
          "orange", "red", "lightgrey", "blue"]
# Available badge named logos.
Logos = ["appveyor", "bitcoin", "bithound", "discord", "dockbit", "eclipse",
         "github", "gitter-white", "gratipay", "paypal", "postgresql",
         "scrutinizer", "slack", "sourcegraph", "telegram", "tfs",
         "travis", "twitter"]


_dynamic = '%s/badge/dynamic/%s.svg?uri=%s&label=%s&query=%s&colorB=%s%s'
_static = "%s/badge/%s-%s-%s.svg%s"


class Static(object):
    """Generate a static shield."""
    def __init__(self, subject, status, color, style=None,
                 label=None, logo=None, logoWidth=None, linkA=None,
                 linkB=None, colorA=None, colorB=None, maxAge=None):
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

    def generate(self):
        """Generate static shield url."""
        _check_color(self.color)
        format_subject = _check_text(self.subject)
        format_status = _check_text(self.status)
        return _static % (self.url, format_subject,
                          format_status, self.color,
                          self._get_style())

    def _get_style(self):
        """Generate a parameter string for styling."""
        param = []
        if self.style:
            _check_style(self.style)
            param.append("style=%s" % self.style)
        if self.label:
            self.label = _check_text(self.label)
            param.append("label=%s" % self.label)
        if self.logo:
            _check_logo(self.logo)
            param.append("logo=%s" % self.logo)
        if self.logoWidth:
            param.append("logoWidth=%s" % self.logoWidth)
        if self.linkA:
            param.append("link=%s" % self.linkA)
        if self.linkB:
            param.append("link=%s" % self.linkB)
        if self.colorA:
            _check_color(self.colorA)
            param.append("colorA=%s" % self.colorA)
        if self.colorB:
            _check_color(self.colorB)
            param.append("colorB=%s" % self.colorB)
        if self.maxAge:
            param.apped("maxAge=%s" % self.maxAge)
        if param:
            return "?%s" % "&".join(param)
        else:
            return ''


class Dynamic(object):
    """Generate a dynamic shield."""
    def __init__(self, uri, label, query, colorB, datatype="json",
                 colorA=None, style=None, prefix=None, suffix=None,
                 logo=None, logoWidth=None, linkA=None, linkB=None,
                 maxAge=None):
        super(Dynamic, self).__init__()
        # Configure for other host options.
        self.url = "https://img.shields.io"
        # Data object format.
        self.datatype = datatype
        # Data object location.
        self.uri = uri
        # Right side label.
        self.label = label
        # Query on the data object.
        self.query = query
        # Left side color.
        self.colorA = colorA
        # Right side color.
        self.colorB = colorB
        # Shield style.
        self.style = style
        # Right side label prefix.
        self.prefix = prefix
        # Right side label suffix.
        self.suffix = suffix
        self.logo = logo
        self.logoWidth = logoWidth
        self.linkA = linkA
        self.linkB = linkB
        self.maxAge = maxAge

    def generate(self):
        """Generate a dynamic shield url."""
        _check_color(self.colorB)
        format_label = _check_text(self.label)
        return _dynamic % (self.url, self.datatype,
                           self.uri, format_label,
                           self.query, self.colorB,
                           self.get_style())

    def get_style(self):
        """Generate a styling option string."""
        param = []
        if self.style:
            _check_style(self.style)
            param.append("style=%s" % self.style)
        if self.logo:
            _check_logo(self.logo)
            param.append("logo=%s" % self.logo)
        if self.logoWidth:
            param.append("logoWidth=%s" % self.logoWidth)
        if self.linkA:
            param.append("link=%s" % self.linkA)
        if self.linkB:
            param.append("link=%s" % self.linkB)
        if self.colorA:
            _check_color(self.colorA)
            param.append("colorA=%s" % self.colorA)
        if self.maxAge:
            param.apped("maxAge=%s" % self.maxAge)
        if self.prefix:
            param.apped("prefix=%s" % self.prefix)
        if self.suffix:
            param.apped("suffix=%s" % self.suffix)
        if param:
            return "&%s" % "&".join(param)
        else:
            return ''

# Check as many errors before they hit the service.


def _check_text(text):
    """Format text."""
    text = text.replace("-", "--")
    text = text.replace("_", "__")
    text = text.replace(" ", "_")
    return text


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
    """Check if a valid named logo or location was passed."""
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
    return False
    # TODO: Add custom logo support.


def _check_named_logo(logo):
    """Check if a passed named logo is valid."""
    if logo in Logos:
        return True
    else:
        return False

if __name__ == '__main__':
    main()

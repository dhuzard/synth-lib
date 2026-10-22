"""Text helpers of synth-lib."""

import re

_NON_SLUG_RUN = re.compile(r"[^a-z0-9]+")


def slugify(text):
    """Return a lowercase ASCII hyphen-separated slug for ``text``."""
    if not isinstance(text, str):
        raise TypeError("slugify() expects a str")
    return _NON_SLUG_RUN.sub("-", text.lower()).strip("-")

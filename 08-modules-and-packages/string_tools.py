"""
string_tools - a tiny example MODULE.

Any .py file is a module. examples.py imports this one with:
    import string_tools
"""

DEFAULT_SEPARATOR = "-"   # module-level "constant"


def slugify(text, separator=DEFAULT_SEPARATOR):
    """Turn "Hello World!" into "hello-world"."""
    cleaned = ""
    for ch in text.lower():
        if ch.isalnum():
            cleaned += ch
        elif ch.isspace() or ch in "-_":
            cleaned += " "
    return separator.join(cleaned.split())


def truncate(text, length):
    """Shorten text to `length` characters, adding "..." if it was cut."""
    if len(text) <= length:
        return text
    return text[: length - 3] + "..."


def _helper():
    """The leading underscore says: internal, don't import me."""
    return "private-ish"


# This block runs ONLY when you execute this file directly:
#   python string_tools.py
# It does NOT run when another file imports string_tools.
if __name__ == "__main__":
    print("Running string_tools directly!")
    print(slugify("Hello World, From Python!"))
    print(truncate("A very long sentence indeed", 10))

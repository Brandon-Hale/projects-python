"""
shapes - a tiny example PACKAGE (a folder of modules).

This __init__.py runs the first time anything imports `shapes`.
It can be empty. Here we use it to re-export the most useful names,
so users can write `from shapes import circle_area` instead of
`from shapes.circle import area`.
"""
from shapes.circle import area as circle_area
from shapes.square import area as square_area

__all__ = ["circle_area", "square_area"]   # what `from shapes import *` gives you

"""
shapes_package
A reusable package containing multiple class modules for geometric shapes.
"""

# Expose key classes at the package level so they can be imported directly
# from the package name instead of from individual submodules.
from .circle import Circle
from .rectangle import Rectangle
from .square import Square
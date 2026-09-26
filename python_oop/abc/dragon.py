#!/usr/bin/env python3
"""Module demonstrating mixin classes with Dragon."""


class SwimMixin:
    """Mixin class providing swimming capability."""

    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying capability."""

    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon composed using mixins."""

    def roar(self):
        """Print dragon roar sound."""
        print("The dragon roars!")

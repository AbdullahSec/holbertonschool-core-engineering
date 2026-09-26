#!/usr/bin/env python3
"""Module that extends the built-in list with notifications."""


class VerboseList(list):
    """Custom list class that notifies on item addition and removal."""

    def append(self, item):
        """Append item to list and print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list with items and print notification."""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Print notification and remove item from list."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print notification and pop item at specified index."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)

#!/usr/bin/python3
"""Multiple Inheritance demonstration module."""


class Fish:
    """Represents fish behaviors."""
    def swim(self):
        """Standard swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Standard water habitat."""
        print("The fish lives in water")


class Bird:
    """Represents bird behaviors."""
    def fly(self):
        """Standard flying."""
        print("The bird is flying")

    def habitat(self):
        """Standard sky habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Combines traits from Fish and Bird classes."""
    def fly(self):
        """Enhanced flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Enhanced swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Dual habitat behavior."""
        print("The flying fish lives both in water and the sky!")

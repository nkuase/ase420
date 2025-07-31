"""
Framework package for Factory Method Pattern

This package contains the abstract classes that define the Factory Method pattern:
- Factory: Abstract factory class that defines the creation process
- Product: Abstract product class that defines the product interface

This represents the "framework" level of the Factory Method pattern.
"""

from .factory import Factory
from .product import Product

__all__ = ['Factory', 'Product']

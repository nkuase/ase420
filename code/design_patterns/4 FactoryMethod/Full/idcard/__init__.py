"""
IDCard package for Factory Method Pattern

This package contains concrete implementations of the Factory Method pattern:
- IDCard: Concrete product representing an ID card
- IDCardFactory: Concrete factory that creates ID cards

This represents the concrete implementation level of the Factory Method pattern.
"""

from .id_card import IDCard
from .id_card_factory import IDCardFactory

__all__ = ['IDCard', 'IDCardFactory']

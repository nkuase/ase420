from abc import ABC, abstractmethod

# Factory (Template Method style)
class Factory(ABC):
    def create_product(self, owner):
        """Template method: fixed creation pipeline"""
        self._validate(owner)          # fixed step
        parts = self._prepare_parts()  # overridable step
        product = self._make(owner, parts)  # factory method
        self._register(product)        # fixed step
        return product

    def _validate(self, owner):
        print(f"Validating owner {owner}")

    @abstractmethod
    def _prepare_parts(self):
        pass

    @abstractmethod
    def _make(self, owner, parts):
        pass

    def _register(self, product):
        print(f"Registering product: {product.__class__.__name__}")
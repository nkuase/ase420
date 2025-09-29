from abstract_factory import Factory
from concrete_product import BasicProduct, PremiumProduct

# Concrete Factories
class BasicFactory(Factory):
    def _prepare_parts(self):
        print("Preparing basic parts")
        return ["basic-part"]

    def _make(self, owner, parts):
        print(f"Assembling Basic Product for {owner} with {parts}")
        return BasicProduct()

class PremiumFactory(Factory):
    def _prepare_parts(self):
        print("Preparing premium parts")
        return ["premium-part"]

    def _make(self, owner, parts):
        print(f"Assembling Premium Product for {owner} with {parts}")
        return PremiumProduct()
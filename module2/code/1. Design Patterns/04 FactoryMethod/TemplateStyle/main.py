from concrete_factory import PremiumFactory

factory = PremiumFactory()
product = factory.create_product("Alice")
product.use()
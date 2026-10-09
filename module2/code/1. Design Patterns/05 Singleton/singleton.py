class Singleton:
  _instance = None
  _initialized = False

  def __new__(cls, *args, **kwargs): # when an instance is created
    if cls._instance is None:
      print("An instance is created.")
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self, value=None): # initialization
    if not self._initialized:
      # initialization 
      self.value = value  # variables added
      Singleton._initialized = True

  @classmethod
  def get_instance(cls, value=None):
    return cls(value)

  def some_business_method(self):
      return f"Singleton instance {id(self)} with value={self.value} performing business logic"

  def __str__(self):
      return f"Singleton instance (id: {id(self)}, value: {self.value})"

  def __repr__(self):
      return f"Singleton(id={id(self)}, value={self.value})"

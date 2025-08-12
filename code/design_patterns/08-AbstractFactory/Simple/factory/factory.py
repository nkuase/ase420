from abc import ABC, abstractmethod
from factory.link import Link
from factory.tray import Tray
from factory.page import Page
import importlib


class Factory(ABC):
  
  @staticmethod
  def get_factory(classname):
    try:
      module_path, class_name = classname.rsplit('.', 1)
      
      module = importlib.import_module(module_path)
      factory_class = getattr(module, class_name)
      
      return factory_class()
      
    except (ImportError, AttributeError) as e:
      print(f"Class '{classname}' was not found: {e}")
      return None
    except Exception as e:
      print(f"Error creating factory: {e}")
      return None
  
  @abstractmethod
  def create_link(self, caption, url):
    pass
  
  @abstractmethod
  def create_tray(self, caption):
    pass
  
  @abstractmethod
  def create_page(self, title, author):
    pass

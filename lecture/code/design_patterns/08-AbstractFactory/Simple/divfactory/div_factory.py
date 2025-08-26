from factory.factory import Factory
from factory.link import Link
from factory.tray import Tray
from factory.page import Page
from divfactory.div_link import DivLink
from divfactory.div_tray import DivTray
from divfactory.div_page import DivPage


class DivFactory(Factory):
  
  def create_link(self, caption, url):
    return DivLink(caption, url)
  
  def create_tray(self, caption):
    return DivTray(caption)
  
  def create_page(self, title, author):
    return DivPage(title, author)

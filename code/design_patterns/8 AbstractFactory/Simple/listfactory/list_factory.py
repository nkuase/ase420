from factory.factory import Factory
from factory.link import Link
from factory.tray import Tray
from factory.page import Page
from listfactory.list_link import ListLink
from listfactory.list_tray import ListTray
from listfactory.list_page import ListPage


class ListFactory(Factory):
  
  def create_link(self, caption, url):
    return ListLink(caption, url)
  
  def create_tray(self, caption):
    return ListTray(caption)
  
  def create_page(self, title, author):
    return ListPage(title, author)

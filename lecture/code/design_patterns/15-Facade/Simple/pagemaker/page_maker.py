from pagemaker.database import Database
from pagemaker.html_writer import HtmlWriter


class PageMaker:
  
  def __init__(self):
    pass
  
  @staticmethod
  def make_welcome_page(mailaddr, filename):
    try:
      mail_properties = Database.get_properties("maildata")
      username = mail_properties.get(mailaddr, "Unknown User")
      
      with open(filename, 'w', encoding='utf-8') as f:
        writer = HtmlWriter(f)
        
        writer.title(f"{username}'s web page")
        writer.paragraph(f"Welcome to {username}'s web page!")
        writer.paragraph("Nice to meet you!")
        writer.mailto(mailaddr, username)
        writer.close()
      
      print(f"{filename} is created for {mailaddr} ({username})")
      
    except IOError as e:
      print(f"Error creating welcome page: {e}")
    except Exception as e:
      print(f"Unexpected error: {e}")

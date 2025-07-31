"""
Facade Pattern - PageMaker Facade
This class provides a simplified interface to the complex page creation subsystem.
"""

from pagemaker.database import Database
from pagemaker.html_writer import HtmlWriter


class PageMaker:
    """
    Facade class that provides a simple interface for creating welcome pages.
    This class hides the complexity of the underlying subsystem components
    (Database, HtmlWriter) and provides a unified, easy-to-use interface.
    """
    
    def __init__(self):
        """Private constructor - this class only has static methods."""
        pass
    
    @staticmethod
    def make_welcome_page(mailaddr: str, filename: str):
        """
        Create a welcome page for a user.
        This method encapsulates all the complex operations needed to create
        a personalized welcome page.
        
        Args:
            mailaddr (str): The email address of the user
            filename (str): The name of the HTML file to create
        """
        try:
            # Step 1: Get user data from database
            mail_properties = Database.get_properties("maildata")
            username = mail_properties.get(mailaddr, "Unknown User")
            
            # Step 2: Create HTML writer
            with open(filename, 'w', encoding='utf-8') as f:
                writer = HtmlWriter(f)
                
                # Step 3: Generate HTML content
                writer.title(f"{username}'s web page")
                writer.paragraph(f"Welcome to {username}'s web page!")
                writer.paragraph("Nice to meet you!")
                writer.mailto(mailaddr, username)
                writer.close()
            
            # Step 4: Confirm creation
            print(f"{filename} is created for {mailaddr} ({username})")
            
        except IOError as e:
            print(f"Error creating welcome page: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

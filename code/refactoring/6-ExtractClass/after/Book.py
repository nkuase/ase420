class Author:
    """Author class (extracted from Book)"""
    
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
        
    def get_name(self):
        return self.name
        
    def get_mail(self):
        return self.mail
        
    def set_name(self, name):
        self.name = name
        
    def set_mail(self, mail):
        self.mail = mail


class Book:
    """Book class using composition with Author (after refactoring)"""
    
    def __init__(self, title, isbn, price, author_name, author_mail):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.author = Author(author_name, author_mail)
        
    def get_title(self):
        return self.title
        
    def get_isbn(self):
        return self.isbn
        
    def get_price(self):
        return self.price
        
    def get_author_name(self):
        return self.author.get_name()
        
    def get_author_mail(self):
        return self.author.get_mail()
        
    def set_author_name(self, name):
        self.author.set_name(name)
        
    def set_author_mail(self, mail):
        self.author.set_mail(mail)
        
    def to_xml(self):
        author = self.tag("author", 
                         self.tag("name", self.author.get_name()) + 
                         self.tag("mail", self.author.get_mail()))
        book = self.tag("book", 
                       self.tag("title", self.title) + 
                       self.tag("isbn", self.isbn) + 
                       self.tag("price", self.price) + 
                       author)
        return book
        
    def tag(self, element, content):
        return f"<{element}>{content}</{element}>"

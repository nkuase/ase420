class Book:
    """Book class with embedded author information (before refactoring)"""
    
    def __init__(self, title, isbn, price, author_name, author_mail):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.author_name = author_name
        self.author_mail = author_mail
        
    def get_title(self):
        return self.title
        
    def get_isbn(self):
        return self.isbn
        
    def get_price(self):
        return self.price
        
    def get_author_name(self):
        return self.author_name
        
    def get_author_mail(self):
        return self.author_mail
        
    def set_author_name(self, name):
        self.author_name = name
        
    def set_author_mail(self, mail):
        self.author_mail = mail
        
    def to_xml(self):
        author = self.tag("author", 
                         self.tag("name", self.author_name) + 
                         self.tag("mail", self.author_mail))
        book = self.tag("book", 
                       self.tag("title", self.title) + 
                       self.tag("isbn", self.isbn) + 
                       self.tag("price", self.price) + 
                       author)
        return book
        
    def tag(self, element, content):
        return f"<{element}>{content}</{element}>"

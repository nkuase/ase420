class InvalidCommandException(Exception):
    """Exception for invalid robot commands"""
    
    def __init__(self, message: str = ""):
        super().__init__(message)
        self.message = message

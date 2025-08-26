from banner import Banner
from print_class import Print


class PrintBanner(Print):
    def __init__(self, string: str):
        self._banner = Banner(string)
    
    def print_weak(self):
        self._banner.show_with_paren()
    
    def print_strong(self):
        self._banner.show_with_aster()
    
    def get_banner(self):
        return self._banner
    
    def __str__(self) -> str:
        return f"PrintBanner containing {self._banner}"

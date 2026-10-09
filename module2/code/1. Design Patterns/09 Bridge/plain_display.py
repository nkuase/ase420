from display import Display
from string_display_impl import StringDisplayImpl


class PlainDisplay(Display):
  def __init__(self, impl):
    super().__init__(impl)


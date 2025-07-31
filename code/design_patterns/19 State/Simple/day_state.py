from state import State

class DayState(State):
  _instance = None
  
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance
  
  @staticmethod
  def get_instance():
    if DayState._instance is None:
      DayState._instance = DayState()
    return DayState._instance
  
  def do_clock(self, context, hour):
    if hour < 9 or hour >= 17:
      from night_state import NightState
      context.change_state(NightState.get_instance())
  
  def do_use(self, context):
    context.record_log("Safe used (Daytime)")
  
  def do_alarm(self, context):
    context.call_security_center("Emergency alarm (Daytime)")
  
  def do_phone(self, context):
    context.call_security_center("Normal call (Daytime)")
  
  def __str__(self):
    return "[Daytime]"

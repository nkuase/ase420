from state import State

class NightState(State):
  _instance = None
  
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance
  
  @staticmethod
  def get_instance():
    if NightState._instance is None:
      NightState._instance = NightState()
    return NightState._instance
  
  def do_clock(self, context, hour):
    if 9 <= hour < 17:
      from day_state import DayState
      context.change_state(DayState.get_instance())
  
  def do_use(self, context):
    context.call_security_center("EMERGENCY: Nighttime safe usage!")
  
  def do_alarm(self, context):
    context.call_security_center("Emergency alarm (Nighttime)")
  
  def do_phone(self, context):
    context.record_log("Nighttime call recorded")
  
  def __str__(self):
    return "[Nighttime]"

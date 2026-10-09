from underline_pen import UnderlinePen
from message_box import MessageBox

def main():
    print("=== Prototype Pattern Demo ===\n")
  
    upen = UnderlinePen('-')
    mbox = MessageBox('*')
    
    u = upen.clone()
    m = mbox.clone()
    
    
    u.use("Hello, world.")
    m.use("Hello, world.")
    

if __name__ == "__main__":
  main()

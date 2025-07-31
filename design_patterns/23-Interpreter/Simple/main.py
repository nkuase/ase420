import os
from context import Context
from program_node import ProgramNode
from parse_exception import ParseException

class TurtleInterpreter:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.direction = 0
    self.path = [(self.x, self.y)]
    
  def execute_program(self, program_node):
    print(f"Starting execution at position ({self.x}, {self.y})")
    self._execute_command_list(program_node.command_list_node)
    print(f"Execution completed at position ({self.x}, {self.y})")
    
  def _execute_command_list(self, command_list_node):
    for command in command_list_node.get_commands():
      self._execute_command(command.get_node())
  
  def _execute_command(self, command_node):
    from primitive_command_node import PrimitiveCommandNode
    from repeat_command_node import RepeatCommandNode
    
    if isinstance(command_node, PrimitiveCommandNode):
      self._execute_primitive(command_node)
    elif isinstance(command_node, RepeatCommandNode):
      self._execute_repeat(command_node)
  
  def _execute_primitive(self, primitive_node):
    command = primitive_node.get_name()
    
    if command == "go":
      if self.direction == 0:
        self.y += 1
      elif self.direction == 1:
        self.x += 1
      elif self.direction == 2:
        self.y -= 1
      elif self.direction == 3:
        self.x -= 1
      
      self.path.append((self.x, self.y))
      print(f"  go -> moved to ({self.x}, {self.y})")
      
    elif command == "right":
      self.direction = (self.direction + 1) % 4
      directions = ["North", "East", "South", "West"]
      print(f"  right -> now facing {directions[self.direction]}")
      
    elif command == "left":
      self.direction = (self.direction - 1) % 4
      directions = ["North", "East", "South", "West"]
      print(f"  left -> now facing {directions[self.direction]}")
  
  def _execute_repeat(self, repeat_node):
    count = repeat_node.get_number()
    print(f"  repeat {count} times:")
    
    for i in range(count):
      print(f"    iteration {i + 1}:")
      self._execute_command_list(repeat_node.get_command_list())
  
  def get_path(self):
    return self.path.copy()
  
  def reset(self):
    self.x = 0
    self.y = 0
    self.direction = 0
    self.path = [(self.x, self.y)]

def demonstrate_parsing():
  print("=== Parsing Demonstration ===")
  
  test_programs = [
    "program end",
    "program go end",
    "program go right go end",
    "program repeat 3 go right end end",
    "program repeat 2 go repeat 2 right end end end"
  ]
  
  for i, program_text in enumerate(test_programs, 1):
    print(f"\n{i}. Parsing: \"{program_text}\"")
    
    try:
      context = Context(program_text)
      program_node = ProgramNode()
      program_node.parse(context)
      print(f"   Result: {program_node}")
      print("   ✅ Parsing successful")
    except ParseException as e:
      print(f"   ❌ Parsing failed: {e}")

def demonstrate_execution():
  print("\n=== Execution Demonstration ===")
  
  interpreter = TurtleInterpreter()
  
  execution_programs = [
    ("Simple movement", "program go go right go end"),
    ("Square pattern", "program repeat 4 go right end end"),
    ("Complex pattern", "program repeat 3 go right go right go left end end")
  ]
  
  for name, program_text in execution_programs:
    print(f"\n--- {name} ---")
    print(f"Program: {program_text}")
    
    try:
      context = Context(program_text)
      program_node = ProgramNode()
      program_node.parse(context)
      print(f"Parsed AST: {program_node}")
      
      interpreter.reset()
      print("\nExecution trace:")
      interpreter.execute_program(program_node)
      
      path = interpreter.get_path()
      print(f"Final path: {path}")
      
    except ParseException as e:
      print(f"❌ Error: {e}")

def parse_file_programs():
  print("\n=== File-based Program Parsing ===")
  
  try:
    if os.path.exists("program.txt"):
      with open("program.txt", "r") as f:
        lines = f.readlines()
      
      for line_num, line in enumerate(lines, 1):
        program_text = line.strip()
        if not program_text:
          continue
          
        print(f"\nLine {line_num}: \"{program_text}\"")
        
        try:
          context = Context(program_text)
          program_node = ProgramNode()
          program_node.parse(context)
          print(f"Parsed: {program_node}")
        except ParseException as e:
          print(f"❌ Parse error: {e}")
    else:
      print("program.txt file not found. Creating it...")
      
  except Exception as e:
    print(f"Error reading file: {e}")

def demonstrate_error_handling():
  print("\n=== Error Handling Demonstration ===")
  
  invalid_programs = [
    ("Missing 'end'", "program go"),
    ("Invalid command", "program jump end"),
    ("Missing number", "program repeat go end end"),
    ("Wrong token", "program go left right"),
    ("Incomplete repeat", "program repeat 3 go")
  ]
  
  for name, program_text in invalid_programs:
    print(f"\n{name}: \"{program_text}\"")
    
    try:
      context = Context(program_text)
      program_node = ProgramNode()
      program_node.parse(context)
      print(f"Unexpected success: {program_node}")
    except ParseException as e:
      print(f"Expected error caught: {e}")

def main():
  print("=== Interpreter Pattern Demo ===\n")
  
  print("The Interpreter pattern defines a representation for a language's grammar")
  print("and provides an interpreter that uses the representation to interpret")
  print("sentences in the language.\n")
  
  print("Mini Language Grammar:")
  print("  <program> ::= program <command list>")
  print("  <command list> ::= <command>* end")
  print("  <command> ::= <repeat command> | <primitive command>")
  print("  <repeat command> ::= repeat <number> <command list>")
  print("  <primitive command> ::= go | right | left")
  print()
  
  demonstrate_parsing()
  demonstrate_execution()
  parse_file_programs()
  demonstrate_error_handling()
  
  print(f"\n{'='*60}")
  print("Interpreter Pattern Benefits Demonstrated:")
  print(f"{'='*60}")
  print("✅ Grammar Representation: Each grammar rule has its own class")
  print("✅ Extensibility: Easy to add new grammar rules and commands")
  print("✅ Separation of Concerns: Parsing logic separated from execution")
  print("✅ Recursive Structure: Complex expressions built from simple ones")
  print("✅ Error Handling: Clear error messages for invalid syntax")
  print("✅ AST Construction: Builds abstract syntax tree for later processing")
  
  print("\nInterpreter Pattern Use Cases:")
  print("- Domain-specific languages (DSLs)")
  print("- Configuration file parsers")
  print("- Simple scripting languages")
  print("- Regular expression engines")
  print("- SQL query processors")
  print("- Mathematical expression evaluators")
  
  print("\nKey Points:")
  print("- One class per grammar rule (easy to maintain and extend)")
  print("- Recursive descent parsing for nested structures")
  print("- Context manages parsing state and token navigation")
  print("- AST can be interpreted, compiled, or transformed")
  print("- Best for simple languages (complex ones need parser generators)")
  print("- Provides foundation for more sophisticated language processors")

if __name__ == "__main__":
  main()

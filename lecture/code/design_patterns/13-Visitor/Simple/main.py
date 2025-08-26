from directory import Directory
from file import File
from list_visitor import ListVisitor
from size_visitor import SizeVisitor

def create_file_system():
  print("Making root entries...")
  
  root_dir = Directory("root")
  bin_dir = Directory("bin")
  tmp_dir = Directory("tmp")
  usr_dir = Directory("usr")
  
  root_dir.add(bin_dir)
  root_dir.add(tmp_dir)
  root_dir.add(usr_dir)
  
  bin_dir.add(File("vi", 10000))
  bin_dir.add(File("latex", 20000))
  
  tmp_dir.add(File("tmp1", 10))
  tmp_dir.add(File("tmp2", 20))
  
  usr_dir.add(File("a", 100))
  usr_dir.add(File("b", 200))
  
  return root_dir

def main():
  
  print("=== Visitor Pattern Demo ===\n")
  
  rootdir = create_file_system()
  
  print("\nFile system structure:")
  rootdir.accept(ListVisitor())
  print()
  
  print("\nUsing the file system structure to get size:")
  size = rootdir.accept(SizeVisitor())
  print(f"\nFile total size {size}")
  
  size = rootdir.get_size()
  print(f"\nFile total size {size}")
  
if __name__ == "__main__":
  main()

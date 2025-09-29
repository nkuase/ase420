from entry import Entry
from file import File
from directory import Directory


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


def demonstrate_uniform_treatment(root_dir):
  print("=== Demonstrating Uniform Treatment ===")
  
  all_entries = []
  
  def collect_entries(entry):
    all_entries.append(entry)
    if isinstance(entry, Directory):
      for child in entry:
        collect_entries(child)
  
  collect_entries(root_dir)
  
  print(f"\nFound {len(all_entries)} total entries:")
  print("All entries treated uniformly:")
  
  for entry in all_entries[:10]:
    print(f"  {entry.get_name()}: {entry.get_size()} bytes")
  
  if len(all_entries) > 10:
    print(f"  ... and {len(all_entries) - 10} more entries")
  
  print()


def demonstrate_recursive_operations(root_dir):
  print("=== Demonstrating Recursive Operations ===")
  
  print(f"Total size of entire file system: {root_dir.get_size()} bytes")
  print(f"Total number of files: {root_dir.get_total_files()}")
  
  print("\nSize breakdown by directory:")
  for entry in root_dir:
    if isinstance(entry, Directory):
      print(f"  {entry.get_name()}: {entry.get_size()} bytes ({entry.get_total_files()} files)")
  
  print()

def main():
  
  print("=== Composite Pattern Example ===\n")
  
  root_dir = create_file_system()
  
  root_dir.print_list()
  print()
  
  demonstrate_uniform_treatment(root_dir)
  
  demonstrate_recursive_operations(root_dir)

  print()

if __name__ == "__main__":
  main()

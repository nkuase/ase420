from directory import Directory
from file import File
from size_visitor import SizeVisitor

def create_simple_structure():
    """Create a simple directory structure for demonstration"""
    root = Directory("root")
    root.add(File("file1.txt", 100))
    root.add(File("file2.log", 200))
    
    subdir = Directory("subdir")
    subdir.add(File("file3.txt", 50))
    subdir.add(File("file4.log", 75))
    
    root.add(subdir)
    return root

def demonstrate_difference():
    print("=== Demonstrating the Difference ===\n")
    
    root = create_simple_structure()
    
    # Method 1: Using built-in get_size() (not visitor pattern)
    print("1. Using Directory.get_size() (not visitor pattern):")
    total_size_builtin = root.get_size()
    print(f"   Total size: {total_size_builtin}")
    print("   ↳ Directory controls the traversal\n")
    
    # Method 2: Using SizeVisitor (proper visitor pattern)
    print("2. Using SizeVisitor (proper visitor pattern):")
    visitor = SizeVisitor()
    total_size_visitor = root.accept(visitor)
    print(f"   Total size: {total_size_visitor}")
    print("   ↳ Visitor controls the traversal\n")
    
    print(f"Both give the same result: {total_size_builtin == total_size_visitor}")
    print("\nBUT the key difference is WHO controls the traversal and calculation!")

# Demonstration of why visitor pattern is more flexible
class SelectiveSizeVisitor(SizeVisitor):
    """A visitor that only counts .txt files to show flexibility"""
    
    def visit_file(self, file):
        if file.get_name().endswith('.txt'):
            print(f"{self.current_dir}/{file} (COUNTED)")
            return file.size
        else:
            print(f"{self.current_dir}/{file} (SKIPPED - not .txt)")
            return 0  # Don't count non-.txt files
    
    def visit_directory(self, directory):
        print(f"{self.current_dir}/{directory}")
        
        saved_dir = self.current_dir
        self.current_dir = f"{self.current_dir}/{directory.get_name()}"
        
        total_size = 0
        for entry in directory:
            total_size += entry.accept(self)
        
        self.current_dir = saved_dir
        return total_size

def demonstrate_visitor_flexibility():
    print("\n=== Demonstrating Visitor Pattern Flexibility ===\n")
    
    root = create_simple_structure()
    
    print("Regular SizeVisitor (counts all files):")
    regular_visitor = SizeVisitor()
    total_all = root.accept(regular_visitor)
    print(f"Total size: {total_all}\n")
    
    print("SelectiveSizeVisitor (only counts .txt files):")
    selective_visitor = SelectiveSizeVisitor()
    total_txt_only = root.accept(selective_visitor)
    print(f"Total size of .txt files only: {total_txt_only}\n")
    
    print("This flexibility is WHY we use the visitor pattern!")
    print("You can't achieve this with Directory.get_size()")

if __name__ == "__main__":
    demonstrate_difference()
    demonstrate_visitor_flexibility()

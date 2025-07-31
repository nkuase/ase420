"""
Main module for Composite Pattern Example

This demonstrates the Composite pattern where objects are composed into tree
structures to represent part-whole hierarchies. The pattern lets clients
treat individual objects and compositions of objects uniformly.

Key concepts demonstrated:
1. Component (Entry) - defines interface for objects in composition
2. Leaf (File) - represents leaf objects with no children
3. Composite (Directory) - stores child components and implements child-related operations
4. Client code treats all objects uniformly through the Component interface

The file system metaphor perfectly illustrates this pattern:
- Files are leaves (no children)
- Directories are composites (can contain files and other directories)
- Both can be treated uniformly as "entries"
"""

from entry import Entry
from file import File
from directory import Directory


def create_file_system() -> Directory:
    """
    Create a sample file system hierarchy.
    
    Returns:
        Directory: The root directory of the file system
    """
    print("Making root entries...")
    
    # Create root directory and main subdirectories
    root_dir = Directory("root")
    bin_dir = Directory("bin")
    tmp_dir = Directory("tmp")
    usr_dir = Directory("usr")
    
    # Build the directory structure
    root_dir.add(bin_dir)
    root_dir.add(tmp_dir)
    root_dir.add(usr_dir)
    
    # Add files to bin directory
    bin_dir.add(File("vi", 10000))
    bin_dir.add(File("latex", 20000))
    
    return root_dir, usr_dir


def add_user_directories(usr_dir: Directory) -> None:
    """
    Add user directories and files to the file system.
    
    Args:
        usr_dir (Directory): The usr directory to add users to
    """
    print("Making user entries...")
    
    # Create user directories
    youngjin = Directory("youngjin")
    gildong = Directory("gildong")
    dojun = Directory("dojun")
    
    # Add user directories to usr
    usr_dir.add(youngjin)
    usr_dir.add(gildong)
    usr_dir.add(dojun)
    
    # Add files to user directories
    youngjin.add(File("diary.html", 100))
    youngjin.add(File("Composite.java", 200))
    
    gildong.add(File("memo.tex", 300))
    
    dojun.add(File("game.doc", 400))
    dojun.add(File("junk.mail", 500))


def demonstrate_uniform_treatment(root_dir: Directory) -> None:
    """
    Demonstrate how the Composite pattern allows uniform treatment of objects.
    
    Args:
        root_dir (Directory): The root directory
    """
    print("=== Demonstrating Uniform Treatment ===")
    
    # Collect all entries (both files and directories) in a single list
    all_entries = []
    
    def collect_entries(entry: Entry) -> None:
        """Recursively collect all entries."""
        all_entries.append(entry)
        if isinstance(entry, Directory):
            for child in entry:
                collect_entries(child)
    
    collect_entries(root_dir)
    
    print(f"\nFound {len(all_entries)} total entries:")
    print("All entries treated uniformly:")
    
    # Treat all entries uniformly - both files and directories
    for entry in all_entries[:10]:  # Show first 10 for brevity
        print(f"  {entry.get_name()}: {entry.get_size()} bytes")
    
    if len(all_entries) > 10:
        print(f"  ... and {len(all_entries) - 10} more entries")
    
    print()


def demonstrate_recursive_operations(root_dir: Directory) -> None:
    """
    Demonstrate recursive operations on the composite structure.
    
    Args:
        root_dir (Directory): The root directory
    """
    print("=== Demonstrating Recursive Operations ===")
    
    print(f"Total size of entire file system: {root_dir.get_size()} bytes")
    print(f"Total number of files: {root_dir.get_total_files()}")
    
    # Show size breakdown by major directories
    print("\nSize breakdown by directory:")
    for entry in root_dir:
        if isinstance(entry, Directory):
            print(f"  {entry.get_name()}: {entry.get_size()} bytes ({entry.get_total_files()} files)")
    
    print()


def demonstrate_directory_operations(root_dir: Directory) -> None:
    """
    Demonstrate various directory operations.
    
    Args:
        root_dir (Directory): The root directory
    """
    print("=== Demonstrating Directory Operations ===")
    
    # Find and work with specific directories
    usr_dir = root_dir.find("usr")
    if isinstance(usr_dir, Directory):
        print(f"Found usr directory with {len(usr_dir)} entries")
        
        # List user directories
        user_dirs = usr_dir.get_directories()
        print("User directories:")
        for user_dir in user_dirs:
            files = user_dir.get_files()
            print(f"  {user_dir.get_name()}: {len(files)} files, {user_dir.get_size()} bytes")
    
    # Demonstrate adding and removing entries
    print("\nAdding a new file and directory:")
    if isinstance(usr_dir, Directory):
        # Add a new user
        newuser = Directory("newuser")
        newuser.add(File("readme.txt", 150))
        newuser.add(File("config.ini", 75))
        
        usr_dir.add(newuser)
        print(f"Added newuser directory with {len(newuser)} files")
        print(f"usr directory now has {len(usr_dir)} entries")
        
        # Remove a file
        youngjin = usr_dir.find("youngjin")
        if isinstance(youngjin, Directory):
            removed = youngjin.remove_by_name("diary.html")
            print(f"Removed diary.html: {removed}")
            print(f"youngjin directory now has {len(youngjin)} files")
    
    print()


def demonstrate_pattern_benefits() -> None:
    """Demonstrate the key benefits of the Composite pattern."""
    print("=== Composite Pattern Benefits ===")
    
    print("1. Uniform Treatment:")
    print("   - Client code treats files and directories the same way")
    print("   - Same operations (getName, getSize) work on both")
    
    print("\n2. Recursive Composition:")
    print("   - Directories can contain other directories")
    print("   - Creates tree structures naturally")
    
    print("\n3. Simplified Client Code:")
    print("   - No need to distinguish between leaf and composite objects")
    print("   - Polymorphism handles the differences")
    
    print("\n4. Easy to Add New Types:")
    print("   - New types of entries can be added easily")
    print("   - Existing code doesn't need to change")
    
    print("\n5. Recursive Operations:")
    print("   - Operations like size calculation work recursively")
    print("   - Complex hierarchies handled automatically")
    
    print()


def create_complex_hierarchy() -> Directory:
    """Create a more complex file system hierarchy for advanced demonstration."""
    print("=== Creating Complex Hierarchy ===")
    
    # Create a project directory structure
    project = Directory("MyProject")
    
    # Source code directory
    src = Directory("src")
    main = Directory("main")
    test = Directory("test")
    
    src.add(main)
    src.add(test)
    
    # Add source files
    main.add(File("main.py", 1500))
    main.add(File("utils.py", 800))
    main.add(File("config.py", 300))
    
    test.add(File("test_main.py", 1200))
    test.add(File("test_utils.py", 900))
    
    # Documentation directory
    docs = Directory("docs")
    docs.add(File("README.md", 2000))
    docs.add(File("INSTALL.md", 1500))
    docs.add(File("API.md", 3000))
    
    # Build directory
    build = Directory("build")
    build.add(File("main.exe", 50000))
    build.add(File("setup.msi", 120000))
    
    # Assemble the project
    project.add(src)
    project.add(docs)
    project.add(build)
    project.add(File("requirements.txt", 250))
    project.add(File("setup.py", 800))
    
    print(f"Created project with {project.get_total_files()} files")
    print(f"Total project size: {project.get_size()} bytes")
    
    return project


def main():
    """Main function demonstrating the Composite pattern."""
    
    print("=== Composite Pattern Example ===\n")
    
    # Create the basic file system (similar to Java version)
    root_dir, usr_dir = create_file_system()
    
    # Print initial structure
    root_dir.print_list()
    print()
    
    # Add user directories and files
    add_user_directories(usr_dir)
    
    # Print complete structure
    root_dir.print_list()
    print()
    
    # Demonstrate uniform treatment
    demonstrate_uniform_treatment(root_dir)
    
    # Demonstrate recursive operations
    demonstrate_recursive_operations(root_dir)
    
    # Demonstrate directory operations
    demonstrate_directory_operations(root_dir)
    
    # Show pattern benefits
    demonstrate_pattern_benefits()
    
    # Create and demonstrate complex hierarchy
    project = create_complex_hierarchy()
    print("Project structure:")
    project.print_list()
    print()
    
    print("="*60)
    print("Pattern Analysis:")
    print("="*60)
    
    print("\n1. Composite Pattern Structure:")
    print("   - Component (Entry): Defines interface for objects in composition")
    print("   - Leaf (File): Represents leaf objects in composition")
    print("   - Composite (Directory): Defines behavior for components with children")
    print("   - Client: Manipulates objects through Component interface")
    
    print("\n2. Key Implementation Details:")
    print("   - Abstract base class defines common interface")
    print("   - Leaf objects implement simple operations")
    print("   - Composite objects delegate to children")
    print("   - Recursive operations handle tree traversal")
    
    print("\n3. Python-Specific Features:")
    print("   - Abstract Base Classes (ABC) for interfaces")
    print("   - List comprehensions for filtering operations")
    print("   - Iterator protocol for directory traversal")
    print("   - Type hints for better code documentation")
    
    print("\n4. Real-World Applications:")
    print("   - File systems (as demonstrated)")
    print("   - GUI component hierarchies")
    print("   - Document structure (chapters, sections, paragraphs)")
    print("   - Organization charts")
    print("   - Mathematical expressions")
    
    print("\n5. Benefits Demonstrated:")
    print("   - Uniform treatment of primitive and composite objects")
    print("   - Recursive composition creates complex structures")
    print("   - Easy to add new component types")
    print("   - Client code is simplified")


if __name__ == "__main__":
    main()

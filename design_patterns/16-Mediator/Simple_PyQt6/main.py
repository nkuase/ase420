import sys
from PyQt6.QtWidgets import QApplication
from login_frame import LoginFrame


def main():
    """
    Demonstrates the Mediator Design Pattern using PyQt6.
    
    The Mediator pattern defines how a set of objects interact with each other.
    Instead of objects communicating directly, they communicate through a mediator.
    """
    
    print("=== Mediator Pattern Demo (PyQt6) ===\n")
    
    print("Creating login dialog with mediator coordination...")
    print("\nUI Component Interactions managed by the Mediator:")
    print("- When 'Guest' is selected: username/password fields are disabled, OK is enabled")
    print("- When 'Login' is selected: username field is enabled")
    print("- When username is entered: password field is enabled")
    print("- When both username and password are entered: OK button is enabled")
    print("- Cancel button is always enabled")
    
    print("\nWithout Mediator Pattern:")
    print("- Each component would need to know about all other components")
    print("- Complex web of dependencies between UI elements")
    print("- Difficult to modify interaction logic")
    print("- Hard to reuse components in different contexts")
    
    print("\nWith Mediator Pattern:")
    print("- Components only know about the mediator")
    print("- Mediator centralizes all interaction logic")
    print("- Easy to modify behavior by changing only the mediator")
    print("- Components are reusable and loosely coupled")
    
    print(f"\n{'='*50}")
    print("Opening Login Dialog...")
    print("Try the following interactions:")
    print("1. Switch between Guest and Login options")
    print("2. Enter username to enable password field")
    print("3. Enter password to enable OK button")
    print("4. Notice how components coordinate automatically")
    print(f"{'='*50}")
    
    # Create PyQt6 application
    app = QApplication(sys.argv)
    
    try:
        # Create and show the login dialog
        login_dialog = LoginFrame("Mediator Pattern Demo - PyQt6")
        login_dialog.show()
        
        # Run the application event loop
        sys.exit(app.exec())
        
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error running demo: {e}")
        print("Note: This demo requires PyQt6 to be installed")
        print("Install with: pip install PyQt6")
        sys.exit(1)
    finally:
        print("\nKey Points:")
        print("- Mediator defines how a set of objects interact with each other")
        print("- Promotes loose coupling by preventing objects from referring to each other explicitly")
        print("- Centralizes complex communications and control logic")
        print("- Makes interaction behavior easier to understand and maintain")
        print("- Individual components become more reusable")


if __name__ == "__main__":
    main()

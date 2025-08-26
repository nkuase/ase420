from AddressFile import AddressFile

def main():
    try:
        file = AddressFile("address.txt")
        # Using exposed database - this shows the problem
        file.get_database().set("Hiroshi Yuki", "hyuki@example.com")
        file.get_database().set("Tomura", "tomura@example.com") 
        file.get_database().set("Hanako Sato", "hanako@example.com")
        file.get_database().update()
        
        # Iterating through names
        for name in file.names():
            mail = file.get_database().get(name)
            print(f"name={name}, mail={mail}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

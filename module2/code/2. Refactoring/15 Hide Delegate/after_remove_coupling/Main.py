from AddressFile import AddressFile

def main():
    try:
        file = AddressFile("address.txt")
        # Using Database.keys() method instead of getProperties().propertyNames()
        file.set("Hiroshi Yuki", "hyuki@example.com")
        file.set("Tomura", "tomura@example.com") 
        file.set("Hanako Sato", "hanako@example.com")
        file.update()
        
        # Iterating through names
        for name in file.names():
            mail = file.get(name)
            print(f"name={name}, mail={mail}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

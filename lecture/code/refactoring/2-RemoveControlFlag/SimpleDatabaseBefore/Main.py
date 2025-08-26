from SimpleDatabase import SimpleDatabase

def main():
    try:
        with open("dbfile.txt", "r") as f:
            db = SimpleDatabase(f)
            
        for key in db.iterator():
            print(f'KEY: "{key}"')
            print(f'VALUE: "{db.get_value(key)}"')
            
    except IOError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

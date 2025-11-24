def login(cursor, conn):
    while True:
        print("\n==== LOGIN SYSTEM ====")
        print("1. Login")
        print("2. Register")
        choice = input("Choose option: ")
        
        if choice == "1":
            username = input("Username: ")
            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            if cursor.fetchone():
                return True
            return False
        elif choice == "2":
            username = input("Create Username: ")
            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            if cursor.fetchone():
                print("Username already exists!")
            else:
                cursor.execute("INSERT INTO users VALUES(?, '')", (username,))
                conn.commit()
                print("Registration successful! Please login.")
        else:
            print("Invalid choice!")
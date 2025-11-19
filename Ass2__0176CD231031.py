# Student Management System

students = {}  
current_user = None  


def register():
    print("-- Student Registration ---")
    username = input("Enter username: ")
    if username in students:
        print("Username already exists. Use different name ")
        return

    password = input("Enter password: ")
    name = input("Enter full name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    course = input("Enter course name: ")
    year = input("Enter year of study: ")
    college = input("Enter college name: ")

    students[username] = {
        "password": password,
        "name": name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "address": address,
        "course": course,
        "year": year,
        "college": college
    }

    print(f"Registration successful! Welcome, {name}.")


def login():
    global current_user
    print("  Login ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in students and students[username]["password"] == password:
        current_user = username
        print(f"Welcome back, {students[username]['name']}")
    else:
        print("Invalid username or password.")


def show_profile():
    if current_user is None:
        print("Please login first.")
        return

    print("  Student Profile   ")
    for key, value in students[current_user].items():
        if key != "password":
            print(f"{key.capitalize()}: {value}")


def update_profile():
    if current_user is None:
        print("Please login first.")
        return

    print("   Update Profile    ")
    print("Leave the field if you don’t want to change it.")

    user = students[current_user]
    for key in user.keys():
        if key != "password":
            new_value = input(f"Update {key} ({user[key]}): ")
            if new_value.strip() != "":
                user[key] = new_value

    print("Profile updated successfully!")

def change_password():
    if current_user is None:
        print("Please login first.")
        return

    old_pass = input("Enter your current password: ")
    if old_pass != students[current_user]["password"]:
        print("Incorrect current password!")
        return

    new_pass = input("Enter new password: ")
    confirm_pass = input("Confirm new password: ")

    if new_pass == confirm_pass:
        students[current_user]["password"] = new_pass
        print("Password changed successfully!")
    else:
        print("Passwords do not match!")

def cancel_registration():
    global current_user
    if current_user is None:
        print("Please login first.")
        return

    confirm = input("Want to cancel registeration (yes/no): ").lower()
    if confirm == "yes":
        del students[current_user]
        print("Your registration has been cancelled.")
        current_user = None
    else:
        print("Account deletion cancelled.")

def show_registered_users():
    if not students:
        print("No users registered yet.")
    else:
        print("\n--- Registered Users ---")
        for username in students.keys():
            print(f"- {username}")

def logout():
    global current_user
    if current_user:
        print(f"Goodbye, {students[current_user]['name']}")
        current_user = None
    else:
        print("No user is currently logged in.")


def main():
    while True:
        print("----- Student Management System -----")
        print("1. Register")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Logout")
        print("6. Change password")
        print("7. Cancel registration")
        print("8. Show registered users")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            show_profile()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            logout()
        elif choice == "6":
            change_password()
        elif choice == "7":
            cancel_registration()
        elif choice == "8":
            show_registered_users()
        elif choice == "9":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")

main()
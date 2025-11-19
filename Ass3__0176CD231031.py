#----STUDENT MANAGEMENT SYSTEM----#

import random
import os

USER_FILE = "userdata.txt"
QUIZ_FILE = "quiz.txt"

def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 8:
                    username = parts[0]
                    users[username] = {
                        "username": parts[0],
                        "password": parts[1],
                        "name": parts[2],
                        "email": parts[3],
                        "contact": parts[4],
                        "course": parts[5],
                        "college": parts[6],
                        "city": parts[7]
                    }
    return users

def save_users(users):
    with open(USER_FILE, "w") as f:
        for u in users.values():
            f.write('|'.join([u["username"], u["password"], u["name"], u["email"], 
                              u["contact"], u["course"], u["college"], u["city"]]))

def register(users):
    print("----STUDENT REGISTRATION ---")
    username = input("Enter username: ").lower()
    if username in users:
        print("Username already exists!")
        return

    password = input("Enter password: ")
    name = input("Enter full name: ")
    email = input("Enter email: ")
    contact = input("Enter contact number: ")
    course = input("Enter course name: ")
    college = input("Enter college name: ")
    city = input("Enter city: ")

    users[username] = {"username": username, "password": password, "name": name, 
                       "email": email, "contact": contact, "course": course, 
                       "college": college, "city": city}

    save_users(users)
    print("Registration successful!")

def login(users):
    print("----STUDENT LOGIN ----")
    username = input("Enter username: ").lower()
    password = input("Enter password: ")

    if username in users and users[username]["password"] == password:
        print(f"Welcome {users[username]['name']}!")
        return username
    else:
        print("Invalid username or password!")
        return None

def show_profile(users, username):
    user = users[username]
    print("---- STDENT PROFILE ----")
    for key, value in user.items():
        print(f"{key.capitalize()}: {value}")

def update_profile(users, username):
    user = users[username]
    print("--- UPDATE PROFILE ---")
    field = input("Enter field to update (name/email/contact/course/college/city): ").lower()
    if field in user and field not in ["username", "password"]:
        user[field] = input(f"Enter new {field}: ")
        save_users(users)
        print("Profile updated successfully!")
    else:
        print("Invalid field!")

def quiz():
    print("--- QUIZ SECTION ---")
    subject = input("Enter subject (DSA/DBMS/OOPM): ").upper()
    if not os.path.exists(QUIZ_FILE):
        print("Quiz file not found!")
        return

    with open(QUIZ_FILE, "r") as f:
        questions = [line.strip().split('|') for line in f if line.strip().startswith(subject)]

    if not questions:
        print("No questions found for this subject!")
        return

    random.shuffle(questions)
    score = 0
    for q in questions[:5]:
        print(f"Q: {q[1]}")
        for i in range(2, 6):
            print(f"{i-1}. {q[i]}")
        ans = input("Your answer (1-4): ")
        if ans.isdigit() and q[int(ans)+1] == q[6]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer: {q[6]}")

    print(f"You scored {score}/5")

def main():
    users = load_users()
    logged_user = None

    while True:
        if not logged_user:
            print("====== STUDENT SYSTEM ======")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose: ")

            if choice == '1':
                register(users)
            elif choice == '2':
                logged_user = login(users)
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        else:
            print("--- Dashboard ---")
            print("1. Attempt Quiz")
            print("2. Show Profile")
            print("3. Update Profile")
            print("4. Logout")
            choice = input("Choose: ")

            if choice == '1':
                quiz()
            elif choice == '2':
                show_profile(users, logged_user)
            elif choice == '3':
                update_profile(users, logged_user)
            elif choice == '4':
                logged_user = None
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    main()
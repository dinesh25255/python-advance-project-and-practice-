from cryptography.fernet import Fernet

# Function to generate the key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Call this function once to generate the key
write_key()  # Uncomment this line to generate the key, then comment it again after running the script once.

# Load the key from the key.key file
def load_key():
    try:
        with open("key.key", "rb") as file:
            key = file.read()
        return key
    except FileNotFoundError:
        print("Key file not found. Please run 'write_key()' first to generate a key.")
        exit()

# Initialize the Fernet object with the loaded key
key = load_key()
fer = Fernet(key)

# View stored passwords
def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
    except FileNotFoundError:
        print("Passwords file not found. Please add some passwords first.")

# Add a new password
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Main loop to add or view passwords
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")

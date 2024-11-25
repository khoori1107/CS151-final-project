from tkinter import *

# Initialize a list to store only encrypted passwords
encrypted_storage = []
manager_password = None  # Variable to store the manager password


#For netlify serverless function
def handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello, world!"
    }

# Function to assign the manager password
def assign_password():
    global manager_password
    manager_password = store_entry.get().strip()
    if manager_password:
        store_text.delete("1.0", END)
        store_text.insert(END, "Manager password assigned!")
        # Hide the assign password entry and button
        store_entry.pack_forget()
        store_button.pack_forget()
        store_label.pack_forget()
    else:
        store_text.delete("1.0", END)
        store_text.insert(END, "Please enter a valid password!")


# Function to encrypt the text and store it in the list
def encrypt_text():
    user_phrase = key_entry.get().strip()
    if not user_phrase:
        plaintext_text.delete("1.0", END)
        plaintext_text.insert(END, "Please enter a phrase to encrypt!")
        return

    # Encryption dictionary
    replacement = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': '-', 's': '$', 'c': '54', 'k': '/_'}
    encryption = ''.join(replacement.get(char, char) for char in user_phrase.lower())

    encrypted_storage.append(encryption)  # Store only encrypted items

    plaintext_text.delete("1.0", END)
    plaintext_text.insert(END, encryption)


# Function to decrypt the text
def decrypt_text():
    user_phrase = key_entry.get().strip()
    if not user_phrase:
        plaintext_text.delete("1.0", END)
        plaintext_text.insert(END, "Please enter a phrase to decrypt!")
        return

    # Decryption dictionary
    deplacement = {'@': 'a', '3': 'e', '1': 'i', '0': 'o', '-': 'u', '$': 's', '54': 'c', '/_': 'k'}
    decrypted = user_phrase
    for key, value in deplacement.items():
        decrypted = decrypted.replace(key, value)

    plaintext_text.delete("1.0", END)
    plaintext_text.insert(END, decrypted)


# Function to view stored encrypted passwords
def view_passwords():
    entered_password = password_entry.get().strip()
    if manager_password and entered_password == manager_password:
        store_text.delete("1.0", END)
        if encrypted_storage:
            store_text.insert(END, "\n".join(encrypted_storage))
        else:
            store_text.insert(END, "No encrypted items stored yet!")
    else:
        store_text.delete("1.0", END)
        store_text.insert(END, "Invalid manager password!")


# Function to hide stored passwords
def hide_passwords():
    entered_password = password_entry.get().strip()
    if manager_password and entered_password == manager_password:
        store_text.delete("1.0", END)
        store_text.insert(END, "Passwords hidden!")
    else:
        store_text.delete("1.0", END)
        store_text.insert(END, "Invalid manager password!")


# Function to reset the fields
def reset_fields():
    key_entry.delete(0, END)
    plaintext_text.delete("1.0", END)
    password_entry.delete(0, END)
    store_text.delete("1.0", END)
    global encrypted_storage, manager_password
    encrypted_storage = []  # Clear only encrypted storage
    manager_password = None

    # Bring back the assign password entry and button
    store_label.pack(pady=10)
    store_entry.pack(pady=10)
    store_button.pack(pady=10)


# Main window setup
root = Tk()
root.title("Encrypt/Decrypt with Manager Access")
root.geometry("800x600")

# Key entry field
key_label = Label(root, text="Enter a phrase:", font=("Arial", 14))
key_label.pack(pady=10)

key_entry = Entry(root, font=("Arial", 14), width=30)
key_entry.pack(pady=10)

# Text area for displaying encryption/decryption results
plaintext_text = Text(root, font=("Arial", 14), height=5, width=50)
plaintext_text.pack(pady=10)

# Manager password assignment field
store_label = Label(root, text="Assign manager password:", font=("Arial", 14))
store_label.pack(pady=10)

store_entry = Entry(root, font=("Arial", 14), width=30)
store_entry.pack(pady=10)

store_button = Button(root, text="Assign Password", font=("Arial", 14), command=assign_password)
store_button.pack(pady=10)

# Manager password verification field
password_label = Label(root, text="Enter manager password:", font=("Arial", 14))
password_label.pack(pady=10)

password_entry = Entry(root, font=("Arial", 14), width=30)
password_entry.pack(pady=10)

# Text area for displaying stored passwords
store_text = Text(root, font=("Arial", 14), height=5, width=50)
store_text.pack(pady=10)

# Buttons for encryption, decryption, viewing, hiding, and resetting
button_frame = Frame(root)
button_frame.pack(pady=20)

encrypt_button = Button(button_frame, text="Encrypt", font=("Arial", 14), command=encrypt_text)
encrypt_button.pack(side=LEFT, padx=10)

decrypt_button = Button(button_frame, text="Decrypt", font=("Arial", 14), command=decrypt_text)
decrypt_button.pack(side=LEFT, padx=10)

view_button = Button(button_frame, text="View", font=("Arial", 14), command=view_passwords)
view_button.pack(side=LEFT, padx=10)

hide_button = Button(button_frame, text="Hide", font=("Arial", 14), command=hide_passwords)
hide_button.pack(side=LEFT, padx=10)

reset_button = Button(button_frame, text="Reset", font=("Arial", 14), command=reset_fields)
reset_button.pack(side=LEFT, padx=10)

exit_button = Button(button_frame, text="Exit", font=("Arial", 14), command=root.quit)
exit_button.pack(side=LEFT, padx=10)

root.mainloop()

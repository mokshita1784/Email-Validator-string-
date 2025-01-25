import tkinter as tk
from tkinter import messagebox

# Function to validate the email
def validate_email():
    email = email_entry.get()  # Get the input from the email entry field

    if len(email) >= 6:
        if email[0].isalpha():
            if "@" in email and email.count("@") == 1 and 0 < email.index("@") < len(email) - 1:
                if "." in email[email.index("@"):] and email[email.index("@") + 1:].count(".") >= 1:
                    if " " not in email:
                        messagebox.showinfo("Success", "Valid Email")  # Show success message
                    else:
                        messagebox.showerror("Error", "Email should not contain spaces")  # Error message
                else:
                    messagebox.showerror("Error", "'.' must come after '@' and not be the last character")
            else:
                messagebox.showerror("Error", "'@' is missing or incorrectly placed")
        else:
            messagebox.showerror("Error", "First character must be a letter")
    else:
        messagebox.showerror("Error", "Email must be at least 6 characters long")

# Create the main application window
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x300")
root.configure(bg="orange")  # Set the background color to orange

# Create a label for the email field
email_label = tk.Label(root, text="Enter your Email:", bg="orange", font=("Arial", 12, "bold"))
email_label.pack(pady=10)

# Create an entry field for email input
email_entry = tk.Entry(root, width=30, font=("Arial", 12))
email_entry.pack(pady=5)

# Create a button to validate the email
validate_button = tk.Button(root, text="Validate", command=validate_email, font=("Arial", 12), bg="yellow", fg="black")
validate_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

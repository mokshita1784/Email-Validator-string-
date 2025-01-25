

---

## 1. **Introduction**
### 1.1 **Purpose**
The purpose of this project is to create a simple **Email Validator** using Tkinter, a Python GUI library. The application will validate email inputs based on basic email format rules, providing feedback to the user.

### 1.2 **Scope**
This project is a standalone desktop application designed to help users validate email addresses. It will check if the email meets basic formatting requirements such as length, the presence of `@` and `.`, and ensure no spaces are present. The system will display appropriate messages based on the validation outcome.

### 1.3 **Definitions, Acronyms, and Abbreviations**
- **Tkinter**: A standard Python library used to create graphical user interfaces.
- **GUI**: Graphical User Interface.
- **Email Validation**: The process of checking if an email address follows common formatting rules.

---

## 2. **System Overview**
The Email Validator is a simple Python desktop application with a graphical interface. Users will input their email into a text field, and the system will validate it against the following criteria:
- The email must be at least 6 characters long.
- The first character of the email must be an alphabet letter.
- The email must contain exactly one `@` symbol and one or more `.` characters after `@`.
- The email must not contain any spaces.

---

## 3. **Functional Requirements**
### 3.1 **Email Input**
- **Description**: The user will input their email in a text box.
- **Input**: Text entered by the user.
- **Output**: None (The user input is validated when the button is clicked).

### 3.2 **Validate Email**
- **Description**: The system will validate the entered email.
  - Check if the length is at least 6 characters.
  - Ensure the first character is an alphabet letter.
  - Ensure exactly one `@` symbol is present.
  - Ensure at least one `.` character appears after `@`.
  - Ensure no spaces are present.
- **Input**: The email entered by the user.
- **Output**: A message box indicating whether the email is valid or providing an error message with specific details.

### 3.3 **Error Handling**
- **Description**: If the email fails validation, an error message will appear indicating the specific issue (e.g., first character is not a letter, invalid placement of `@`, etc.).
- **Input**: Invalid email input.
- **Output**: Appropriate error message displayed in a pop-up.

---

## 4. **Non-Functional Requirements**
### 4.1 **Performance**
- The application should respond quickly, with email validation occurring immediately after the button is clicked.

### 4.2 **Usability**
- The interface should be simple and intuitive, with clearly labeled buttons and input fields.
- The design should be aesthetically pleasing, with an orange background and easy-to-read text.

### 4.3 **Compatibility**
- The application will run on systems with Python and Tkinter installed.

---

## 5. **User Interface Requirements**
### 5.1 **Main Window**
- **Title**: "Email Validator"
- **Background color**: Orange
- **Widgets**:
  - **Label**: "Enter your Email:" positioned at the top of the window.
  - **Text Entry**: A single-line input field for the email.
  - **Button**: A "Validate" button to trigger the validation process.
  - **Message Box**: Display messages (success or error) based on email validation.

---

## 6. **System Design**
- **GUI Framework**: Tkinter for creating the window and handling user interactions.
- **Email Validation Logic**: Python code will be used to perform checks on the email format, such as the length, starting character, `@`, `.`, and spaces.

---

## 7. **Assumptions and Dependencies**
- The system assumes that the user will input a valid email address (not necessarily real) that fits the validation criteria.
- The system depends on Python's Tkinter library for creating the GUI.

---

## 8. **Glossary**
- **Email Address**: A string used for identifying a user or system in electronic communication (e.g., user@example.com).
- **Tkinter**: A Python library used for creating graphical user interfaces.
- **Message Box**: A pop-up window used to display messages to the user.

---


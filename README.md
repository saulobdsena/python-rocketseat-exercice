# 📒 Contact Manager

A contact manager developed in **Python** and executed through the terminal. The project allows users to add, view, edit, favorite, and delete contacts using an interactive menu.

## 📌 About the Project

The **Contact Manager** was created to practice fundamental Python concepts, such as:

* Lists;
* Dictionaries;
* Functions;
* Conditional statements;
* Loops;
* Exception handling;
* The `match case` statement;
* Terminal input and output.

Each contact is stored in a dictionary containing the following information:

```python
{
    "name": "Contact name",
    "number": "Contact number",
    "email": "Contact email",
    "is_fav": False
}
```

The dictionaries are added to the main contact list:

```python
contact_list = []
```

## ⚙️ Features

The system provides the following features:

1. **Add a New Contact**

   * Requests the contact's name, phone number, and email address.
   * Adds the contact to the list.

2. **View All Contacts**

   * Displays all registered contacts.
   * Shows each contact's position in the list.
   * Indicates which contacts are marked as favorites.

3. **Edit a Contact**

   * Allows the user to update the name, phone number, and email address of an existing contact.

4. **Favorite or Unfavorite a Contact**

   * Toggles the favorite status of the selected contact.

5. **View Favorite Contacts**

   * Displays only the contacts marked as favorites.

6. **Delete a Contact**

   * Removes the selected contact from the list.

7. **Exit the Program**

   * Ends the Contact Manager execution.

## 🖥️ System Menu

When the program is executed, the following menu is displayed:

```text
Contact Manager Menu

1. Add New Contact
2. View Contact List
3. Edit Contact
4. Favorite/Unfavorite Contact
5. Favorite Contact List
6. Delete Contact
7. Exit
```

The user must enter the number corresponding to the desired operation.

## 🚀 How to Run

### Requirements

You must have **Python 3.10 or a newer version** installed because the project uses the `match case` statement.

To check the installed Python version, run:

```bash
python --version
```

Or:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone REPOSITORY_URL
```

Enter the project directory:

```bash
cd contact-manager
```

Run the program:

```bash
python main.py
```

On some systems, you may need to use:

```bash
python3 main.py
```

## 📂 Project Structure

```text
contact-manager/
│
├── main.py
└── README.md
```

## 🔧 Functions

### `add_contact()`

Adds a new contact to the list.

```python
add_contact(contact_list, contact_name, contact_number, contact_email)
```

### `view_contacts()`

Displays all registered contacts.

```python
view_contacts(contact_list)
```

### `edit_contact()`

Updates the information of a selected contact.

```python
edit_contact(contact_list, contact_index, new_name, new_number, new_email)
```

### `favorite_contact()`

Toggles a contact between favorite and non-favorite.

```python
favorite_contact(contact_list, contact_index)
```

### `view_favorite_contacts()`

Displays only the contacts marked as favorites.

```python
view_favorite_contacts(contact_list)
```

### `delete_contact()`

Removes a contact from the list.

```python
delete_contact(contact_list, contact_index)
```

## 📝 Usage Example

```text
Contact Manager Menu
1. Add New Contact
2. View Contact List
3. Edit Contact
4. Favorite/Unfavorite Contact
5. Favorite Contact List
6. Delete Contact
7. Exit

Enter: 1

Contact name: John
Contact number: 99999-9999
Contact email: john@email.com

Contact John added to the contact manager
```

When viewing the contact list:

```text
1. | | Name: John, Number: 99999-9999, Email: john@email.com
```

When the contact is marked as a favorite:

```text
1. |★| Name: John, Number: 99999-9999, Email: john@email.com
```

## 🛠️ Technologies Used

* Python 3;
* Terminal;
* Git;
* GitHub.

## 🎯 Purpose

This project was developed for educational purposes to practice Python programming fundamentals and the organization of a program based on functions.


contact_list = []

def add_contact(contact_list, contact_name, contact_number, contact_email):

    contacts = {"name": contact_name, "number": contact_number, "email": contact_email, "is_fav": False}
    contact_list.append(contacts)
    print(f"Contact {contact_name} added to the contact menager")
    return 


def view_contacts(contact_list):

    for i, contacts in enumerate(contact_list, start=1):
        favorite = "|★|" if contacts["is_fav"] else "| |"
        print(f"{i}. {favorite} Name: {contacts["name"]}, Number: {contacts["number"]}, Email: {contacts["email"]}")

def edit_contact(contact_list, contact_index, new_name, new_number, new_email):

    try:
        contact_list[(int(contact_index) - 1)]["name"] = new_name
        contact_list[(int(contact_index) - 1)]["number"] = new_number
        contact_list[(int(contact_index) - 1)]["email"] = new_email
        print(f"Contact {contact_index} updated to {new_name}, {new_number}, {new_email}")

    except IndexError as e:
        print("Error: your index is out of range")

    return

def favorite_contact(contact_list, contact_index):
    
    try:
        if contact_list[(int(contact_index) - 1)]["is_fav"] == False:
            contact_list[(int(contact_index) - 1)]["is_fav"] = True
            print(f"Contact {contact_index} is favorite now")

        elif contact_list[(int(contact_index) - 1)]["is_fav"] == True:
            contact_list[(int(contact_index) - 1)]["is_fav"] = False
            print(f"Contact {contact_index} is not favorite now")
        
    except IndexError as e:
        print(f"Error: your index is out of range")


def view_favorite_contacts(contact_list):

    for i, contacts in enumerate(contact_list, start=1):
        if contacts["is_fav"] == True:
            favorite = "|★|" if contacts["is_fav"] else "| |"
            print(f"{i}. {favorite} Name: {contacts["name"]}, Number: {contacts["number"]}, Email: {contacts["email"]}")

def delete_contact(contact_list, contact_index):

    try:
        contact_list.remove(contact_list[(int(contact_index) - 1)])
        print(f"Contact removed")

    except IndexError as e:
        print(f"Error: your index is out of range")



while True:

    print("\n Contact Manager Menu")
    print("1. Add New Contact")
    print("2. View Contact List")
    print("3. Edit Contact")
    print("4. Favorite/Unfavorite Contact")
    print("5. Favorite Contact List")
    print("6. Delete Contact")
    print("7. Exit")

    response = int(input("Enter "))

    match response:

        case 1:
            name = input("Contact name: ")
            number = input("Contact number: ")
            email = input("Contact email: ")
            add_contact(contact_list, name, number, email)
        
        case 2:
            view_contacts(contact_list)

        case 3:
            view_contacts(contact_list)
            contact_index = input("Which contact do you wanna edit? ")
            new_name = input("What is the new name? ")
            new_number = input("What is the new phone? ")
            new_email = input("What is the new email? ")
            edit_contact(contact_list, contact_index, new_name, new_number, new_email)

        case 4:
            view_contacts(contact_list)
            contact_index = input("Who is the contact do you wanna favorite? ")
            favorite_contact(contact_list,contact_index)

        case 5:
            view_favorite_contacts(contact_list)

        case 6:
            view_contacts(contact_list)
            contact_index = input("Who is the contact do you wanna delete? ")
            delete_contact(contact_list, contact_index)

        case 7:
            break

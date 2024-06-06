import time

# Creating an empty dictionary to store a new user detail entry
new_user = {}

# Creating a list where new_user will be added as a list element
users = {} 
# Function to switch between adding, updating and searching user details
def main():
    while True:
        user_response = str(input("Hello, what do you want to do?\n| Add | Search | Update | Show | Exit | \n")) 
        response = user_response.lower()
        
        if response == "add":
            add()
            time.sleep(1)
            main()
        elif response == "search":
            search() 
            time.sleep(1)
            main()
        elif response == "update":
            update() 
            time.sleep(1)
            main()      
        elif response == "show":
            show()
            time.sleep(1)
            main()              
        elif response == "exit":
            break
            time.sleep(1) 
        else:
            print("Please choose from the options.\n")
            time.sleep(1)
            main()
        break
        
                    
#  Function to add a new user
def add():
    # name, phone, username variables request user input                
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    username = input("Enter your desired user name: ")
    
    #a dictionary named new_user is created containing two key value pairs, with keys 'name' and 'phone'
    new_user[name] = name
    new_user[phone] = phone
    
    #a new dictionary named users is created, uaing username as key and new_user as its corresponding value
    users[username] = new_user
    
    #confirming that the entry of user details is successful
    print(f"{name} added successfully.\n")

# Function to search for a contact
def search():
    #request user input, the username to be searched
    search_username = input("Enter the username to search for: ")
    
    #conditional statement checking if the search_username is in the recorded users
    if search_username in users.keys():
        print(f"{search_username}'s phone number: {users[search_username][phone]}\n")
    else:
        print(f"{search_username} not found.\n")     

# Function to update a contact        
def update():
    username = input("Enter the username to search for: ")
    if username in users.keys():
        new_phone = input(f"Please enter {username}'s new phone number: ") 
        users[username]['phone'] = new_phone
        print(f"{username}'s contact updated successfully.\n") 

# Function to show thw whole contact list        
def show():
    print("Users\n")
    if users == {}:
        print("No users yet\n")
    else:     
   	 for username, new_user in users.items():
            print(f"{username} | {users[username][name]} | {users[username][ phone]}" )


main()        
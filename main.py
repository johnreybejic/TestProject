import time

# Creates a dictionary where user inputs about the user's name and phone number will be stored
new_user = {}

# Creates a another list where the created new_user dictionary will stored
users = {} 

# main function that controls which function shall be called based on user entry
def main():
    while True:
        # gets user input then converts it to lowercase
        user_response = str(input("Hello, what do you want to do?\n| Add | Search | Update | Show | Exit | \n")) 
        response = user_response.lower()
        
        # conditional statement that calls the add function. Calls the main function to maintain the loop after the execution of the function
        if response == "add":
            add()
            time.sleep(1)
            main()

        # conditional statement that calls the search function. Calls the main function to maintain the loop after the execution of the function
        elif response == "search":
            search() 
            time.sleep(1)
            main()

        # conditional statement that calls the update function. Calls the main function to maintain the loop after the execution of the function
        elif response == "update":
            update() 
            time.sleep(1)
            main()      
        
        # conditional statement that calls the show function. Calls the main function to maintain the loop after the execution of the function
        elif response == "show":
            show()
            time.sleep(1)
            main()            

        # conditional statement that causes to break out of the function. 
        elif response == "exit":
            break

        # conditional statement that activates when the user entry doe not match any of these: | Add | Search | Update | Show | Exit.  
        # Calls the main function to maintain the loop after the execution of the function
        else:
            print("Please choose from the options.\n")
            time.sleep(1)
            main()
            
        # break the while loop
        break
           
# Function to add a new user
def add():

    # name, phone, username variables that requests and stores user input                
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    username = input("Enter your desired user name: ")
    
    #a dictionary named new_user is created containing two key value pairs, with keys 'name' and 'phone'
    new_user = {'name':name, 'phone':phone}
   
    #a new dictionary named users is created, uaing username as key and new_user as its corresponding value
    users[username] = new_user
    
    #confirmation message that user entry is added in the user dictionary
    print(f"{name} added successfully.\n")

# Function to search for a contact
def search():

    #requests user input, the username to be searched and stores it in the variable search_username
    search_username = input("Enter the username to search for: ")
    
    # conditional statement comparing the value of search_username matches any of the keys in users dictionary.
    # if it matches a key, it accesses the dictionary paired to it and gets the value
    # if no keys match, it prints a string message
    if search_username in users.keys():
        print(f"{search_username}'s phone number: {users[search_username]['phone']}\n")
    else:
        print(f"{search_username} not found.\n")     

# Function to update a user detail        
def update():

    # conditional statement comparing the value of update_username matches any of the keys in users dictionary.
    # if no keys match, it prints a string message
    update_username = input("Enter the username to search for: ")

    # if it matches a key, it accesses the dictionary paired to it. new_phone stores user input and replaces the current value inside the accessed dictionary
    if update_username in users.keys():
        new_phone = input(f"Please enter {update_username}'s new phone number: ") 
        users[update_username]['phone'] = new_phone
        print(f"{update_username}'s contact updated successfully.\n") 

    # if no keys match, it prints a string message
    else:
        print(f"{update_username} is not yet registered.")

# Function to show thw whole contact list        
def show():
    print("Users\n")

    # if the users dictionary is empty, it prints a string message
    if users == {}:
        print("No users yet\n")
    # if the dictionary has atleast one entry, it prints the contents in the specified string message using a forr loop
    else:     
   	 for username, new_user in users.items():
            print(f"{username} | {users[username]['name']} | {users[username]['phone']}" )


main()        
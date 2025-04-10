# Step 1: Create a list named 'contacts' with at least 4 contacts
contacts = [
    ['Alice', '555-1234', 'alice@email.com'],
    ['Bob', '555-5678', 'bob@email.com'],
    ['Charlie', '555-8765', 'charlie@email.com'],
    ['Diana', '555-4321', 'diana@email.com']
]

# Step 2: Print the details of the second contact
print("Second contact details:", contacts[1]) 

# Step 3: Update the phone number of the third contact
contacts[2][1] = '555-9999' 

# Step 4: Add a new contact to the list
contacts.append(['Ethan', '555-5555', 'ethan@email.com']) 

# Step 5: Print the updated contact list
print("Updated contact list:")
for contact in contacts:
    print(contact)

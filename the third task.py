contacts = {
    "mahmoud":"555-0199",
    "mostafa":"555-0142",
    "mohamed":"555-0177",
}
print("----contact list----")
for name in contacts:
    print(name)
print("\n--------------------")
search_name = input("Enter a name to search for their phone number: ")
if search_name in contacts:
    print(f"{search_name}'s phone number is: {contacts[search_name]}")
else:
    print(f"{search_name} is not in the contact list.")
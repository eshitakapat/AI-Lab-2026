# wap to create a list and insert delete and search ops

my_list = []

while True:
    print("\nMenu:")
    print("1. Insert an element")
    print("2. Delete an element")
    print("3. Search for an element")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        element = input("Enter the element to insert: ")
        my_list.append(element)
        print("Element inserted successfully.")
    elif choice == '2':
        element = input("Enter the element to delete: ")
        if element in my_list:
            my_list.remove(element)
            print("Element deleted successfully.")
        else:
            print("Element not found in the list.")
    elif choice == '3':
        element = input("Enter the element to search for: ")
        if element in my_list:
            print("Element found in the list.")
        else:
            print("Element not found in the list.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

    print("Current list:", my_list)
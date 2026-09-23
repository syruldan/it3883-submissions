# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Arvin Van
# Assignment Number: Lab 1
# Due Date: 09/22/2026
# Purpose: This program creates a text-based menu that allows the user to append data
#          to an input buffer, clear the buffer, display the buffer, or exit the program.
# Resources Used: Python documentation, class notes.

# Initialize an empty input buffer
input_buffer = ""

# Loop until the user chooses to exit
while True:
    # Display the menu
    print("\n--- Text Menu ---")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Get user choice
    choice = input("Enter your choice (1-4): ")

    # Option 1: Append data
    if choice == "1":
        user_text = input("Enter text to append: ")
        input_buffer += user_text
        print("Data appended.")

    # Option 2: Clear buffer
    elif choice == "2":
        input_buffer = ""
        print("Input buffer cleared.")

    # Option 3: Display buffer
    elif choice == "3":
        print("Current buffer contents:")
        print(input_buffer if input_buffer else "[Buffer is empty]")

    # Option 4: Exit
    elif choice == "4":
        print("Exiting program...")
        break

    # Invalid input
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

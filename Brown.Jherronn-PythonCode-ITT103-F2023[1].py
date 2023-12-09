#Author: Jherronn Brown
#Date Created: Dec 5, 2023
#Course:Programming Techniques ITT103
#Purpose:This program manages seat reservations for UCC Signature Express, allowing users to 
#reserve a seat on 1 of 3 classes of bus and checking availability before assigning it. 
#It takes into account the differences in availability between bus types.



class Seat:
    # Class attribute to track availability of seats
    availability = True

# Initialize variables
selectedClass = "none"
totalReservations = 0
firstClassSeats = 27
businessClassSeats = 38
economyClassSeats = 56
fName="None"
lName="None"
telN=0000
email="None"

def choose():
    #handles the processing of user decision
    global choice
    if choice in "Ff":
        reserveSeat('First Class', firstClassSeats)
    elif choice in "Bb":
        reserveSeat('Business Class', businessClassSeats)
    elif choice in "Ee":
        reserveSeat('Economy Class', economyClassSeats)
    elif choice in "Qq":
        summary()
    else:
        choice="none"
        # Display an error message and display the menu
        print("Invalid choice!")
        choose()

def bookAgain():
    #prompt user to book another seat
    again = input("Reserve another seat? Y/N\n ")
    if again in "Yy":
        choose()
    elif again in "Nn":
        summary()
    else:
        print("Invalid Choice")

def summary():
    # Display the reservation summary
        global fname , lname
        print("-----RESERVATION-----\n")
        print("Client:",fName, lName)
        print("Contact Info:",telN,"\n", email)
        print("Reservation type:", selectedClass)
        print("Total number of seats:", totalReservations)

        
# Create a 2-dimensional array to represent seats per class and seat availability
totalSeats = {
    'First Class': [[Seat() for i in range(4)] for i in range(firstClassSeats // 4)],
    'Business Class': [[Seat() for i in range(4)] for i in range(businessClassSeats // 4)],
    'Economy Class': [[Seat() for i in range(4)] for i in range(economyClassSeats // 4)]
}
def telPrompt():
    global telN
    telN=input("Please enter your contact number\n")

def busSeatSystem():
    global fName , lName , telN , email
    print("\nWELCOME TO \n"
        "UCC Signature Express Limited\n")
    print("We need some preliminary information in order to reserve your seat\n")
    fName=input("Please enter your first name\n")
    lName=input("Please enter your last name\n")
    telPrompt()
    if not telN.isdigit():
        print("Contact number must be made up of only digits")
        telPrompt()
    email=input("Please enter your email address\n")
    menu()

# Create a function that displays the menu, prompts the user for input, and processes that input
def menu():
    global selectedClass, choice
    # Print the menu and use line breaks for each new line
    print("\nUCC Signature Express Limited\n"
          "-Getting you there in style-\n"
          "Reservation Options:\n"
          "-First Class(F/f)\n"
          "-Business Class(B/b)\n"
          "-Economy Class(E/e)\n"
          "-Quit or Cancel(Q/q)\n")
    # Prompt the user to input their choice, read that choice, and if it is valid, call the reserveSeat function with their choice as the parameter
    choice = input("Please select an option: ")
    if choice in "FfBbEe":
        choose()
    else:
        # Display an error message and prompt the user again
        print("Invalid choice!")
        menu()
    

# Create a function that reserves a seat
def reserveSeat(classType, x):
    global totalReservations, selectedClass
    selectedClass = classType.capitalize()
    # Check if there are no more seats and warn the user
    if totalReservations >= x:
        print("No more available seats!")
        exit()
    # Prompt the user for the row number and convert it to an integer
    row = input("Enter the row number: ")
    #check if input is a number
    if not row.isdigit():
        print("Invalid input")
        choose()
    rowNum = int(row)
    if rowNum <= 0 or rowNum > x // 4:
        print("Number must be between 1 and ",x // 4)
        exit()
    # Prompt the user for the seat type (window or aisle) and convert it to an integer
    column = input("Enter the column you want to sit in. Columns 1 & 4 are window seats. Columns 2 & 3 are aisle seats: ")
    if not column.isdigit():
        print("invalid input")
        choose()
    columnNum = int(column)
    if columnNum < 1 or columnNum > 4:
        print("Number must be 1, 2, 3, or 4")
        choose()
    # Check if the seat is available and reserve it if it isl
    seat = totalSeats[classType][rowNum - 1][columnNum - 1]
    if seat.availability:
        seat.availability = False
        totalReservations += 1
        print(f"Reserving seat: {selectedClass} class, row {rowNum}, column {columnNum}")
        bookAgain()

    else:
        print("Seat not available")
        choose()

busSeatSystem()

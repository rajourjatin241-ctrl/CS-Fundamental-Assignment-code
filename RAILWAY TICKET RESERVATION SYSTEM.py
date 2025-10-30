#NAME:Jatin Rajour
#TITLE:Railway Ticket Reservation System
#Computer Science Career Pathways and Fundamentals


# Initialize train data
trains = {
    "101": {"route": "Delhi to Mumbai", "seats": 5, "fare": 1200},
    "202": {"route": "Kolkata to Chennai", "seats": 3, "fare": 1500},
    "303": {"route": "Bangalore to Pune", "seats": 4, "fare": 800}
}

# Create an empty list to store booked tickets
bookings = []

# Define function to book a ticket
def book_ticket():
    print("Available trains:")
    for train_no, details in trains.items():
        print(train_no, "-", details["route"], "| Seats:", details["seats"], "| Fare:", details["fare"])

    train_no = input("Enter train number: ")

    if train_no in trains and trains[train_no]["seats"] > 0:
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        gender = input("Enter passenger gender (M/F): ")

        # Update seat count
        trains[train_no]["seats"] -= 1

        # Generate PNR dynamically
        pnr = "PNR" + train_no + str(len(bookings) + 100)

        # Store booking data
        booking = {
            "PNR": pnr,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Train": trains[train_no]["route"],
            "Fare": trains[train_no]["fare"]
        }
        bookings.append(booking)

        print(f"Ticket booked successfully! PNR: {pnr}")
    else:
        print("Invalid train number or no seats available.")

# Define function to view all bookings
def view_bookings():
    if not bookings:
        print("No bookings available.")
    else:
        for b in bookings:
            print(f"{b['PNR']} | {b['Name']} | {b['Train']} | ₹{b['Fare']}")

# Define function to cancel booking
def cancel_booking():
    pnr = input("Enter PNR to cancel: ")
    for b in bookings:
        if b["PNR"] == pnr:
            bookings.remove(b)
            print("Booking cancelled successfully.")
            return
    print("PNR not found.")

# Main menu
def main():
    while True:
        print("--- RAILWAY TICKET RESERVATION SYSTEM ---")
        print("1. Book Ticket")
        print("2. View Bookings")
        print("3. Cancel Ticket")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            print("Thank you for using Indian Railways Reservation System.")
            break
        else:
            print("Invalid input! Please try again.")

# Program starts here
main()

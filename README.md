Railway Ticket Reservation System


1. Train Data Initialization
- A dictionary trains stores train numbers as keys and details like route, available seats, and fare as values.
2. Booking Storage
- An empty list bookings is created to store all ticket reservations.
3. Booking a Ticket
- Function: book_ticket()
- Displays available trains with seat count and fare.
- Takes user input for train number and passenger details (name, age, gender).
- Checks seat availability.
- Reduces seat count by 1 upon successful booking.
- Generates a unique PNR using train number and booking count.
- Stores booking info in the bookings list.
- Displays confirmation with the generated PNR.
4. Viewing Bookings
- Function: view_bookings()
- Checks if any bookings exist.
- If yes, displays PNR, passenger name, train route, and fare for each booking.
5. Cancelling a Booking
- Function: cancel_booking()
- Asks for PNR to cancel.
- Searches for the matching booking.
- If found, removes it from the list and confirms cancellation.
- If not found, shows an error message.
6. Main Menu Loop
- Function: main()
- Displays a menu with options:
- Book Ticket
- View Bookings
- Cancel Ticket
- Exit
- Executes the corresponding function based on user choice.
- Loops until the user chooses to exit.

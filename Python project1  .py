python

```python

# ==========================================
# BUS / TRAIN TICKET BOOKING SYSTEM
# Python 3
# ==========================================

TOTAL_SEATS = 10
TICKET_FARE = 500
REFUND_PERCENTAGE = 80

# List of available seats
available_seats = list(range(1, TOTAL_SEATS + 1))

# Dictionary to store bookings
bookings = {}


# 1. VIEW AVAILABLE SEATS

def view_seats():
    print("\n========== AVAILABLE SEATS ==========")

    if not available_seats:
        print("Bus is now full.")
    else:
        print("Available Seats:", available_seats)

    print("Seats left:", len(available_seats))


# 2. BOOK A SEAT

def book_seat():
    print("\n========== BOOK TICKET ==========")

    if not available_seats:
        print("Bus is full. No seats available.")
        return

    try:
        seat = int(input("Enter seat number (1-10): "))
    except ValueError:
        print("Invalid input! Enter a valid seat number.")
        return

    if seat < 1 or seat > TOTAL_SEATS:
        print("Invalid seat. Choose a seat from 1 to 10.")
        return

    if seat not in available_seats:
        print(f"Seat {seat} is already booked.")
        return

    name = input("Enter passenger name: ").strip()

    if not name:
        print("Passenger name cannot be empty.")
        return

    bookings[seat] = name
    available_seats.remove(seat)

    print(f"\nSeat {seat} booked for {name}. Fare: {TICKET_FARE}")
    print("Seats left:", len(available_seats))

    if not available_seats:
        print("Bus is now full.")


# 3. VIEW ALL BOOKINGS

def view_bookings():
    print("\n========== BOOKING DETAILS ==========")

    if not bookings:
        print("No bookings available.")
        return

    print("Seat Number\tPassenger Name")
    print("------------------------------------")

    for seat, name in sorted(bookings.items()):
        print(f"{seat}\t\t{name}")

    print("------------------------------------")
    print("Total Bookings:", len(bookings))
    print("Seats left:", len(available_seats))


# 4. CANCEL A BOOKING

def cancel_booking():
    print("\n========== CANCEL BOOKING ==========")

    if not bookings:
        print("No bookings available to cancel.")
        return

    try:
        seat = int(input("Enter seat number to cancel: "))
    except ValueError:
        print("Invalid input! Enter a valid seat number.")
        return

    if seat < 1 or seat > TOTAL_SEATS:
        print("Invalid seat. Choose a seat from 1 to 10.")
        return

    if seat not in bookings:
        print(f"Seat {seat} is not booked.")
        return

    passenger = bookings.pop(seat)

    refund = (TICKET_FARE * REFUND_PERCENTAGE) // 100

    available_seats.append(seat)
    available_seats.sort()

    print("\nBooking cancelled successfully!")
    print(f"Passenger: {passenger}")
    print(f"Seat {seat} booking cancelled.")
    print(f"Refund: {refund}")
    print("Seats left:", len(available_seats))


# 5. MAIN MENU

def display_menu():
    print("\n======================================")
    print("       BUS TICKET BOOKING SYSTEM")
    print("======================================")
    print("1. View Seats")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Cancel Booking")
    print("5. Exit")
    print("======================================")


# MAIN PROGRAM

def main():
    print("\nWelcome to Bus/Train Ticket Booking System!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            view_seats()

        elif choice == "2":
            book_seat()

        elif choice == "3":
            view_bookings()

        elif choice == "4":
            cancel_booking()

        elif choice == "5":
            print("\nThank you for using our system!")
            print("Have a safe journey!")
            break

        else:
            print("Invalid choice! Please select between 1 and 5.")


if __name__ == "__main__":
    main()
```
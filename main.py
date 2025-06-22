print("Welcome to our Cinema Booking Program!")
print("These seats are reserved:")
booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

while True:
    print("\n--- Menu ---")
    print("1. Show all booked seats")
    print("2. Book a new seat")
    print("3. Cancel a booking")
    print("4. Show all bookings sorted")
    print("5. Show statistics")
    print("6. Exit")

    choice = input("Choose an option (1–6): ").strip()

    match choice:
        case "1":
            for row, seat in booked_seats:
                print(f"Row {row}, Seat {seat}")

        case "2":
            while True:
                row = int(input("Enter row: "))
                seat = int(input("Enter seat: "))
                if (row, seat) in booked_seats:
                    print("Sorry, this seat is already booked.")
                else:
                    booked_seats.append((row, seat))
                    print("Seat booked successfully!")
                    break

        case "3":
            row = int(input("Enter row to cancel: "))
            seat = int(input("Enter seat to cancel: "))
            if (row, seat) in booked_seats:
                booked_seats.remove((row, seat))
                print("Booking cancelled.")
            else:
                print("This reservation doesn't exist.")

        case "4":
            for row, seat in sorted(booked_seats):
                print(f"Row {row}, Seat {seat}")

        case "5":
            print(f"Total booked seats: {len(booked_seats)}")
            max_row = max(row for row, seat in booked_seats)
            row_counts = [0] * max_row
            for row, seat in booked_seats:
                row_counts[row - 1] += 1
            for i in range(max_row):
                print(f"Row {i + 1}: {row_counts[i]} seats are booked")

        case "6":
            print("Exiting program.")
            break

        case _:
            print("Invalid choice. Please select a number between 1 and 6.")

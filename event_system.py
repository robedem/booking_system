import os

class Ticket:
    def __init__(self, event, seat_number):
        self.event = event
        self.seat_number = seat_number

    def generate_ticket(self):
        print("\nTicket Details:")
        print(f"Event: {self.event.name}")
        print(f"Venue: {self.event.venue}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Price: ${self.event.price}")


class Event:
    def __init__(self, name, venue, date, available_seats, price):
        self.name = name
        self.venue = venue
        self.date = date
        self.available_seats = [int(seat) for seat in available_seats]
        self.price = price

    def display_details(self):
        print(f"\nEvent Name: {self.name}")
        print(f"Venue: {self.venue}")
        print(f"Date: {self.date}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Price: ${self.price}")


class Customer:
    def __init__(self, name):
        self.name = name
        self.tickets = []

    def view_available_events(self, events):
        print("\nAvailable Events:")
        for i, event in enumerate(events, start=1):
            print(f"{i}. {event.name} - Venue: {event.venue}, Price: ${event.price}")

    def reserve_ticket(self, event, seat_number):
        if seat_number in event.available_seats:
            event.available_seats.remove(seat_number)
            ticket = Ticket(event, seat_number)
            self.tickets.append(ticket)
            print(f"{self.name} reserved seat {seat_number} for {event.name}.")
        else:
            print(f"Seat {seat_number} is not available for {event.name}.")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets reserved.")
        else:
            print(f"\n{self.name}'s Tickets:")
            for ticket in self.tickets:
                ticket.generate_ticket()

    def checkout(self):
        total_price = sum(ticket.event.price for ticket in self.tickets)
        print(f"\nTotal Price: ${total_price}")

        # Payment process goes here...
        print("Payment processed. Tickets confirmed.")


def print_event_list(events):
    print("\nEvent List:")
    for i, event in enumerate(events, start=1):
        print(f"{i}. {event.name} - Venue: {event.venue}, Price: ${event.price}")


ADMIN_PASSWORD_FILE = "admin_password.txt"
DEFAULT_ADMIN_PASSWORD = "admin123"

def load_admin_password():
    try:
        with open(ADMIN_PASSWORD_FILE, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return DEFAULT_ADMIN_PASSWORD

def save_admin_password(password):
    with open(ADMIN_PASSWORD_FILE, "w") as file:
        file.write(password)


# Load events from file or start with an empty list
EVENTS_FILE = "events.txt"

def load_events():
    events = []
    try:
        with open(EVENTS_FILE, "r") as file:
            for line in file:
                event_data = line.strip().split(",")
                event = Event(event_data[0], event_data[1], event_data[2], event_data[3].split(","), float(event_data[4]))
                events.append(event)
    except FileNotFoundError:
        events = []
    return events

def save_events(events):
    with open(EVENTS_FILE, "w") as file:
        for event in events:
            event_data = f"{event.name},{event.venue},{event.date},{','.join(map(str, event.available_seats))},{event.price}\n"
            file.write(event_data)


def main():
    admin_password = load_admin_password()
    events = load_events()

    while True:
        print("\n--- Event Ticket System ---")
        print("1. Browse as Admin")
        print("2. Browse as Customer")
        print("3. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":  # Admin
            password = input("Enter the admin password: ")

            if password == admin_password:
                while True:
                    print("\n--- Admin Options ---")
                    print("1. Add New Event")
                    print("2. Show All Events")
                    print("3. Change Login Password")
                    print("4. Quit as Admin")

                    admin_choice = input("\nEnter your choice: ")

                    if admin_choice == "1":
                        event_name = input("\nEnter the event name: ")
                        event_venue = input("Enter the event venue: ")
                        event_date = input("Enter the event date: ")
                        event_seats = input("Enter the available seats (comma-separated): ").split(",")
                        event_price = float(input("Enter the event price: "))

                        event = Event(event_name, event_venue, event_date, event_seats, event_price)
                        events.append(event)
                        print(f"\nNew event '{event.name}' added successfully.")

                    elif admin_choice == "2":
                        print_event_list(events)

                    elif admin_choice == "3":
                        new_password = input("\nEnter the new password: ")
                        admin_password = new_password
                        save_admin_password(admin_password)
                        print("Password changed successfully.")

                    elif admin_choice == "4":
                        save_events(events)
                        break

                    else:
                        print("Invalid option. Please choose again.")

            else:
                print("Incorrect password. Access denied.")

        elif choice == "2":  # Customer
            customer_name = input("\nEnter the customer name: ")
            customer = Customer(customer_name)

            print_event_list(events)
            event_choice = int(input("\nChoose an event (Enter the event number): "))
            selected_event = events[event_choice - 1] if 0 < event_choice <= len(events) else None

            if selected_event is not None:
                selected_event.display_details()
                num_seats = int(input("\nEnter the number of seats to reserve: "))

                for _ in range(num_seats):
                    seat_number = int(input("\nEnter the seat number: "))
                    customer.reserve_ticket(selected_event, seat_number)
            else:
                print("Invalid event selection.")

            customer.view_tickets()
            customer.checkout()

        elif choice == "3":
            save_events(events)
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()

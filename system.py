class Ticket:
    def __init__(self, event, seat_number):
        self.event = event
        self.seat_number = seat_number

    def generate_ticket(self):
        print("\n Ticket Details:")
        print(f"\n Event: {self.event.name}")
        print(f"\n Venue: {self.event.venue}")
        print(f"\n Seat Number: {self.seat_number}")
        print(f"\n Price: ${self.event.price}")


class Event:
    def __init__(self, name, venue, date, available_seats, price):
        self.name = name
        self.venue = venue
        self.date = date
        self.available_seats = available_seats
        self.price = price

    def display_details(self):
        print(f"\nEvent Name: {self.name}")
        print(f"\nVenue: {self.venue}")
        print(f"\nDate: {self.date}")
        print(f"\nAvailable Seats: {self.available_seats}")
        print(f"Price: ${self.price}")


class Customer:
    def __init__(self, name):
        self.name = name
        self.tickets = []

    def view_available_events(self, events):
        print("Available Events:")
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
            print(f"{self.name}'s Tickets:")
            for ticket in self.tickets:
                ticket.generate_ticket()

    def checkout(self):
        total_price = sum(ticket.event.price for ticket in self.tickets)
        print(f"Total Price: ${total_price}")

        # Payment process goes here...
        print("Payment processed. Tickets confirmed.")
        print("ticket number is:","ygjehudebeubeubewub",1+1*2,"egyedhdgeyg" )


def print_event_list(events):
    print("Event List:")
    for i, event in enumerate(events, start=1):
        print(f"{i}. {event.name} - Venue: {event.venue}, Price: ${event.price}")




# Example usage:
event1 = Event("Concert", "Stadium", "2023-06-10", [1, 2, 3, 4, 5], 50)
event2 = Event("Theater Show", "Theater", "2023-06-15", [6, 7, 8, 9, 10], 30)

events = {1: event1, 2: event2}

customer_name = input("\nEnter the customer name: ")
customer = Customer(customer_name)

print_event_list(events.values())

event_choice = int(input("\nChoose an event (Enter the event number): "))
selected_event = events.get(event_choice)

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

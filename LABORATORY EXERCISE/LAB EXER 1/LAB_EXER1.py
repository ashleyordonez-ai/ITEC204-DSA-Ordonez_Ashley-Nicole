tickets = [
    {
        "incident_id": "INC1392939",
        "bot": "BOT-Inventory",
        "description": "Failed to generate the daily report"
    },
    {
        "incident_id": "INC1392940",
        "bot": "BOT-Email",
        "description": "Failed to send the scheduled notification"
    },
    {
        "incident_id": "INC1392941",
        "bot": "BOT-DataSync",
        "description": "Encountered an error during data transfer"
    },
    {
        "incident_id": "INC1392942",
        "bot": "BOT-Invoice",
        "description": "Failed to process an invoice"
    },
    {
        "incident_id": "INC1392943",
        "bot": "BOT-Report",
        "description": "Failed to generate the weekly report"
    },
    {
        "incident_id": "INC1392944",
        "bot": "BOT-FileTransfer",
        "description": "Failed to upload the required file"
    },
    {
        "incident_id": "INC1392945",
        "bot": "BOT-DataEntry",
        "description": "Encountered an error while entering records"
    },
    {
        "incident_id": "INC1392946",
        "bot": "BOT-Backup",
        "description": "Failed to complete the scheduled backup"
    },
    {
        "incident_id": "INC1392947",
        "bot": "BOT-Validation",
        "description": "Failed to validate the submitted records"
    },
    {
        "incident_id": "INC1392948",
        "bot": "BOT-Notification",
        "description": "Failed to send the system alert"
    }
]


# 1. Add a new incident ticket
def add_ticket():
    incident_id = input("Enter Incident ID: ")
    bot = input("Enter Bot: ")
    description = input("Enter Short Description: ")

    ticket = {
        "incident_id": incident_id,
        "bot": bot,
        "description": description
    }

    tickets.append(ticket)
    print("\nTicket added successfully!")


# 2. Display all active incident tickets
def display_tickets():
    if len(tickets) == 0:
        print("\nNo active incident tickets.")
        return

    print("\n" + "-" * 105)
    print(f"| {'Incident ID':<15} | {'Bot':<20} | {'Short Description':<60} |")
    print("-" * 105)

    for ticket in tickets:
        print(
            f"| {ticket['incident_id']:<15} "
            f"| {ticket['bot']:<20} "
            f"| {ticket['description']:<60} |"
        )

    print("-" * 105)


# 3. Search for a ticket using Incident ID
def search_ticket():
    incident_id = input("Enter Incident ID to search: ")

    for ticket in tickets:
        if ticket["incident_id"] == incident_id:
            print("\nTicket found!")
            print("Incident ID:", ticket["incident_id"])
            print("Bot:", ticket["bot"])
            print("Description:", ticket["description"])
            return

    print("\nTicket not found.")


# 4. Remove a resolved incident ticket
def remove_ticket():
    incident_id = input("Enter Incident ID to remove: ")

    for ticket in tickets:
        if ticket["incident_id"] == incident_id:
            tickets.remove(ticket)
            print("\nTicket removed successfully!")
            return

    print("\nTicket not found.")


# 5. Display total number of active tickets
def count_tickets():
    print("\nTotal active incident tickets:", len(tickets))


# Main menu
while True:
    print("\n==============================================")
    print("       IT AUTOMATION INCIDENT TICKET MANAGER")
    print("==============================================")
    print("1. Add New Incident Ticket")
    print("2. Display All Active Tickets")
    print("3. Search for a Ticket")
    print("4. Remove a Resolved Ticket")
    print("5. Count Active Tickets")
    print("6. Exit")
    print("==============================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_ticket()

    elif choice == "2":
        display_tickets()

    elif choice == "3":
        search_ticket()

    elif choice == "4":
        remove_ticket()

    elif choice == "5":
        count_tickets()

    elif choice == "6":
        print("\nThank you for using the IT Automation Incident Ticket Manager!")
        break

    else:
        print("\nInvalid choice. Please try again.")
tickets = [
    {
        "id" : 1,
        "title" : "PC won't turn on",
        "description" : "PC won't turn on using the power button",
        "submitted_by" : "John Doe",
        "status" : "Open",
        "priority" : "Medium"
    },

    {
        "id" : 2,
        "title" : "Monitor not working",
        "description" : "Monitor turns on but doesn't display anything",
        "submitted_by" : "Jane Doe",
        "status" : "In Progress",
        "priority" : "Low"
    }
]

for ticket in tickets:
    print(f"Ticket: {ticket['title']} | Status: {ticket['status']}")
    

def create_ticket():
    title = input("Title: ")
    description = input("Description: ")
    submitted_by = input("Name: ")
    priority = input("Priority: ")
    
    return {
        "id" : id,
        "title" : title,
        "description" : description,
        "submitted_by" : submitted_by,
        "priority" : priority,
        "status": status
    }

new_ticket = create_ticket()
tickets.append(new_ticket)
print(tickets)

def update_status(ticket_id, new_status):
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            ticket["status"] = new_status
            
update_status(1, "Closed")
print(tickets)

while True:
    print("1. View tickets")
    print("2. Create ticket")
    print("3. Update ticket status")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        for ticket in tickets:
            print(tickets)
    elif choice == "2":
        tickets.append(new_ticket)
    elif choice == "3":
        
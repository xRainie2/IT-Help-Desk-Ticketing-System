import json

#A class with objects for a ticket

class Ticket: 
    def __init__(self, id, title, description, submitted_by, priority):
        self.id = id
        self.title = title
        self.description = description
        self.submitted_by = submitted_by
        self.status = "Open"
        self.priority = priority
        self.assigned_technician = None #Is set to "None" because a ticket isn't automatically assigned to a technician by default
        self.upload = None
        
    def close(self):
        self.status = "Closed"
        
    def update_status(self, new_status):
        self.status = new_status
    
    def assign_technician(self, technician):
        self.assigned_technician = technician
        
        
        
    #converts objects in tickets into a dictionary so that it's storable in a JSON text file  
        
    def convert_to_dict(self):
        if self.assigned_technician is None:
            tech_data = None
        else:
            tech_data = self.assigned_technician.convert_to_dict()
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "submitted_by": self.submitted_by,
            "status": self.status,
            "priority": self.priority,
            "technician" : tech_data,
            "upload" : self.upload
        } 

#A class with objects for technicians assigned (or not currently assigned) to tickets

class Technician:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    
    def __str__(self):
        return self.name
    
    def convert_to_dict(self):
        return{
            "id" : self.id,
            "name" : self.name,
        }


#empty list for tickets

tickets = []

#Function that creates a new ticket
        
def create_ticket():
    id = len(tickets) + 1
    title = input("Title: ")
    description = input("description: ")
    submitted_by = input("Name: ")
    priority = input("Priority: ")
    
    return Ticket(id, title, description, submitted_by, priority)


#Saves tickets to JSON text file by converting and adding the dictionary into a list    
    
def save_tickets():
    dict_list = []
    for ticket in tickets:
        dict_list.append(ticket.convert_to_dict())
    with open("tickets.json", "w") as file:
        json.dump(dict_list, file)

#Converts the dictionary from JSON file back into ticket objects

def dict_to_ticket(data):
    ticket = Ticket(data["id"], data["title"], data["description"], data["submitted_by"], data["priority"])
    
    ticket.upload = data["upload"]

    if data["technician"] is not None:
        technician = dict_to_technician(data["technician"])
        ticket.assign_technician(technician)
        
    return ticket

def dict_to_technician(data):
    return Technician(data["id"], data["name"])
        

#Reads tickets from JSON text file then returns the data from dictionary list back into an empty list of tickets
#Try and excepts if JSON text file doesn't exist, prevents program from failing. 

def loads_tickets():
    try:
        with open("tickets.json", "r") as file:
                dict_list = json.load(file)
    except FileNotFoundError:
        return []
    
    tickets = []
    for data in dict_list:
        tickets.append(dict_to_ticket(data))
    return tickets
    
tickets = loads_tickets()

#A fixed set of two technicians (id, "name")

technicians = [
    Technician(1, "Joe"),
    Technician(2, "Jenny")
]

#Necessary to enure technician exists 

def find_technician(tech_id):
    for tech in technicians:
        if tech.id == tech_id:
            return tech
    return None
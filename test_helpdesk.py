from helpdesk import Ticket, find_technician, technicians

def test_close_ticket():
    ticket = Ticket(1, "title", "description", "submitted_by", "priority")
    ticket.close() 
    assert ticket.status == "Closed"
    
def test_new_ticket_defaults():
    ticket = Ticket(1, "title", "description", "submitted_by", "priority", )
    assert ticket.status == "Open"
    assert ticket.assigned_technician is None
    
def test_find_technician_found():
    technician = find_technician(1)
    assert technician.name == "Joe"

def test_find_technician_not_found():
    technician = find_technician(9999)
    assert technician is None

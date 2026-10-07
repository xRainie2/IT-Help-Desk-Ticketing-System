from flask import Flask,  render_template, request, redirect
from flask import send_from_directory
from helpdesk import tickets, Ticket, save_tickets, technicians, find_technician


app = Flask(__name__)
@app.route("/")

def home():
    return "Hello, help desk!"

@app.route("/tickets")
def show_tickets():
    search = request.args.get("search")
    status = request.args.get("status")
    filtered_tickets = []
    if status == None:
        filtered_tickets = tickets
    else:
        for ticket in tickets:
            if ticket.status == status:
                filtered_tickets.append(ticket)
    if search == None:
        pass
    else:
        search_results = []
        for ticket in filtered_tickets:
            if search.lower() in ticket.title.lower():
                search_results.append(ticket)
        filtered_tickets = search_results
               
    return render_template("tickets.html", tickets=filtered_tickets, technicians=technicians)

@app.route("/new", methods=["GET", "POST"])
def new_ticket():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        submitted_by = request.form["submitted_by"]
        priority = request.form["priority"]
        file = request.files["upload"]
        
        if file.filename != "":
            file.save("uploads/" + file.filename)
            upload_filename = file.filename
        else:
            upload_filename = None  
        
        id = len(tickets) + 1
        ticket = Ticket(id, title, description, submitted_by, priority)
        ticket.upload = upload_filename  
        tickets.append(ticket)
        save_tickets()
        return redirect("/tickets")
    
    
    return render_template("new_ticket.html")

@app.route("/update/<int:ticket_id>", methods=["POST"])
def update_ticket(ticket_id):
    new_status = request.form["status"]
    for ticket in tickets:
        if ticket.id == ticket_id:
            ticket.update_status(new_status)
            
    save_tickets()
    return redirect("/tickets")

@app.route("/assign/<int:ticket_id>", methods=["POST"])
def assign_ticket(ticket_id):
    tech_id = int(request.form["technician_id"])
    technician = find_technician(tech_id)
    for ticket in tickets:
        if ticket.id == ticket_id:
            ticket.assign_technician(technician)
    save_tickets()
    return redirect("/tickets")

@app.route("/uploads/<filename>")
def get_upload(filename):
    return send_from_directory("upload", filename)


if __name__ == "__main__":
    app.run(debug=True)
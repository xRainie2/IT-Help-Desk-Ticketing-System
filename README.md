# IT Help Desk Ticketing System

A full-stack ticketing system built from scratch in Python, starting as a command-line tool and growing into a Flask web application. Built as a learning project to practice object-oriented design, file persistence, and web development fundamentals.

## Features

- **Create, view, and update tickets** — each ticket tracks a title, description, submitter, priority, and status
- **Technician assignment** — assign tickets to technicians from a managed list
- **File attachments** — attach a screenshot or file to a ticket to illustrate an issue
- **Search and filter** — filter tickets by status, or search by keyword in the title (combinable)
- **Persistent storage** — tickets are saved to and loaded from a JSON file, so data survives restarts
- **Two interfaces**:
  - A command-line version with input validation
  - A Flask web application with HTML forms and a styled ticket table
- **Automated tests** — a `pytest` suite covering ticket defaults, status changes, and technician lookup

## Tech Stack

- **Python** — core application logic, object-oriented design (`Ticket` and `Technician` classes)
- **Flask** — web framework for routes and request handling
- **Jinja2** — HTML templating (loops, conditionals, and variable rendering inside templates)
- **JSON** — lightweight file-based persistence
- **HTML / CSS** — front-end structure and styling
- **pytest** — automated testing

## Project Structure

```
IT Help Desk Ticketing System/
├── helpdesk.py            # Core logic: Ticket & Technician classes, save/load functions
├── app.py                 # Flask application and routes
├── ticketing_cli.py        # Command-line version of the system
├── test_helpdesk.py        # pytest test suite
├── templates/
│   ├── tickets.html        # Ticket table view, with search/filter controls
│   └── new_ticket.html     # New ticket form
├── static/
│   └── style.css           # Styling for the web app
├── uploads/                 # Uploaded ticket attachments
└── tickets.json             # Saved ticket data
```

## How to Run

### Web version
```bash
pip install flask
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

### Command-line version
```bash
python ticketing_cli.py
```

### Running tests
```bash
pip install pytest
python -m pytest test_helpdesk.py
```

## Screenshots

* <img width="2558" height="901" alt="table of tickets" src="https://github.com/user-attachments/assets/12e8ec84-6e75-49ac-85b7-53ee2f12fe8d" />
* <img width="2559" height="1271" alt="new ticket 2 202202" src="https://github.com/user-attachments/assets/7e924c8e-e445-4554-815b-68da5c7abed7" />


## What I Learned

This project was built incrementally to deeply understand each concept before adding the next layer:

- Moved from plain dictionaries to object-oriented design (`Ticket`, `Technician` classes) to bundle data with the behavior that acts on it
- Implemented JSON serialization/deserialization for objects, including nested objects (a `Ticket` referencing an assigned `Technician`)
- Learned the difference between a CLI's input loop and a web app's request/response model, and restructured the codebase to separate core logic from the interface so both could share it
- Handled real-world edge cases: missing files on first run, invalid user input, and preventing a failed lookup from silently overwriting valid data
- Built and styled a Flask web app with forms, dynamic routes, and file uploads
- Implemented filtering and search using URL query parameters, and learned the GET vs. POST distinction for when each is appropriate
- Wrote automated tests with `pytest`, including the difference between testing a method's return value versus its side effects on an object

## Possible Future Improvements

- Switch from JSON storage to a SQLite database
- Expand test coverage to the Flask routes themselves
- User authentication for technicians
- Highlight the active filter/search in the UI

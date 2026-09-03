Yasmin Ali Abdi
Date: August 20, 2026
Course: Software Engineering Essentials

Day 5 Assignment: Technical Writing

Exercise A: User Manual Procedure

Task: Creating and Activating a Python Virtual Environment and Installing a Package
Prerequisites:
- A computer running Windows, macOS, or Linux
- Python 3 installed on your computer
- Command Prompt (Windows) or Terminal (macOS/Linux) open
- Internet connection
- Basic knowledge of navigating folders using the command line

Steps:
1. Create a new project folder
   Action: Type `mkdir my_project` and press Enter.
   Expected Result: A new folder named "my_project" is created.

2. Navigate into the folder
   Action: Type `cd my_project` and press Enter.
   Expected Result: You are now inside the "my_project" folder.

3. Create the virtual environment
   Action: Type `python -m venv venv` and press Enter.
   Expected Result: A new folder named "venv" is created inside your project folder.

4. Activate the virtual environment (Windows)
   Action: Type `venv\Scripts\activate` and press Enter.
   Expected Result: The prompt changes to show `(venv)` at the beginning of the command line.

   OR (macOS/Linux):
   Action: Type `source venv/bin/activate` and press Enter.
   Expected Result: The prompt changes to show `(venv)` at the beginning of the command line.

5. Install a package
   Action: Type `pip install requests` and press Enter.
   Expected Result: The `requests` library downloads and installs successfully.

6. Verify the installation
   Action: Type `pip list` and press Enter.
   Expected Result: The `requests` package appears in the list of installed packages.

Screenshot Description:

Include a screenshot showing:
- The terminal or command prompt window
- The `(venv)` indicator at the beginning of the command line
- The output of `pip list` showing the `requests` package installed

Troubleshooting:

Most common error: "python is not recognized" (Windows) or "python: command not found" (macOS/Linux).

How to fix:
- Windows: Reinstall Python and check "Add Python to PATH"
- macOS/Linux: Try `python3` instead of `python`
- Check if Python is installed: type `python --version` or `python3 --version`



Exercise B: API Reference Entry

Endpoint: POST /tasks

Description: Creates a new task in the project management system for the authenticated user. The task requires a title and can include optional details like a description, assignee, due date, and priority level.

Request Headers:
- Authorization: Bearer token (required) - Authenticates the user making the request
- Content-Type: application/json (required) - Indicates that the request body is in JSON format

Request Parameters (JSON Body):


Parameter
Type
Required
Description
title
string
Yes
The title of the task
description
string
No
Optional description of the task
assignee
string (User ID)
No
ID of the user assigned to the task
due_date
string (date)
No
Due date in YYYY-MM-DD format
priority
string
No
Must be: low, medium, high (default: medium)



Response Codes:
- 201 Created: Task was successfully created
- 400 Bad Request: Missing required fields or invalid data format
- 401 Unauthorized: Invalid or missing authentication token
- 403 Forbidden: User does not have permission to create tasks
- 500 Internal Server Error: Server encountered an unexpected error

Example Request:

POST /tasks
Authorization: Bearer your_access_token_here
Content-Type: application/json

{
    "title": "Complete project proposal",
    "description": "Write the final draft of the project proposal and send to the client",
    "assignee": "user_12345",
    "due_date": "2026-09-15",
    "priority": "high"
}

Example Response:

{
    "status": "success",
    "message": "Task created successfully",
    "data": {
        "id": "task_67890",
        "title": "Complete project proposal",
        "description": "Write the final draft of the project proposal and send to the client",
        "assignee": {
            "id": "user_12345",
            "name": "Alice Mwangi"
        },
        "due_date": "2026-09-15",
        "priority": "high",
        "created_at": "2026-08-20T14:30:00Z",
        "updated_at": "2026-08-20T14:30:00Z"
    }
}



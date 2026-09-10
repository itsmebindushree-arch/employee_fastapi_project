# Employee Management API

A beginner-friendly Employee Management REST API built using Python, FastAPI and Pydantic.

## Technologies Used

* Python 3.12
* FastAPI
* Pydantic
* Uvicorn
* Swagger UI
* Git

## Project Structure

```text
employee-management-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── services.py
│
├── requirements.txt
└── README.md
```

## Employee Fields

* id - Auto-generated integer
* name - Employee name
* email - Employee email
* department - Employee department
* primary_skill - Primary technical skill
* location - Employee location
* work_mode - WFH or WFO
* is_active - Active status, default is true
* created_at - Employee creation timestamp

## APIs

| Method | Endpoint          | Description              |
| ------ | ----------------- | ------------------------ |
| GET    | `/health`         | Check application health |
| POST   | `/employees`      | Create an employee       |
| GET    | `/employees`      | List all employees       |
| GET    | `/employees/{id}` | Get employee by ID       |
| PUT    | `/employees/{id}` | Update employee          |
| DELETE | `/employees/{id}` | Delete employee          |

## Validation

The API includes the following validations:

* Name is required
* Email is required
* Department is required
* Primary skill is required
* Location is required
* Email must be valid
* Email must be unique
* Work mode accepts only `WFH` or `WFO`
* Employee ID must be greater than zero
* Returns `404` when an employee does not exist
* Returns clear validation errors for invalid requests

## Installation

### 1. Clone the project

```bash
git clone <repository-url>
```

### 2. Open the project

```bash
cd employee-management-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Run:

```bash
uvicorn app.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test all API endpoints.

## Data Storage

Employee records are temporarily stored in a Python list.

No database is used in this task.

Therefore, employee data will be reset whenever the application restarts.

## What I Learned

Through this project, I learned:

* How to create a FastAPI application
* How REST API endpoints work
* How to create GET, POST, PUT and DELETE APIs
* How to use Pydantic models for request validation
* How to validate email addresses
* How to implement unique email validation
* How to return appropriate HTTP status codes
* How to use Swagger UI for API testing
* How to organize a FastAPI project into multiple files
* Basic Git version control and meaningful commits

## Difficulties Faced

Some of the challenges faced during development were:

* Understanding FastAPI project structure
* Understanding request and response models
* Implementing unique email validation
* Handling employee-not-found cases
* Understanding how Swagger UI can be used to test APIs
* Setting up the Python virtual environment

## Assumptions Made

* Employee data is stored temporarily in a Python list as requested.
* Employee IDs start from 1 and are automatically generated.
* `is_active` defaults to `true` when an employee is created.
* Work mode accepts only `WFH` or `WFO`.
* Email addresses must be unique.
* Data is expected to reset when the application restarts.

## Future Improvements

The following are intentionally not included in this task:

* Database
* Authentication
* Frontend
* Docker

These can be introduced in later stages.

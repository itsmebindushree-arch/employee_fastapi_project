from datetime import datetime, timezone

from fastapi import HTTPException

from .schemas import EmployeeCreate, EmployeeUpdate


# Temporary employee storage
employees = []

# Auto-generated employee ID
next_employee_id = 1


def create_employee(employee_data: EmployeeCreate):
    global next_employee_id

    # Check whether email already exists
    for employee in employees:
        if employee["email"].lower() == employee_data.email.lower():
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    employee = {
        "id": next_employee_id,
        "name": employee_data.name,
        "email": employee_data.email,
        "department": employee_data.department,
        "primary_skill": employee_data.primary_skill,
        "location": employee_data.location,
        "work_mode": employee_data.work_mode,
        "is_active": True,
        "created_at": datetime.now(timezone.utc)
    }

    employees.append(employee)

    next_employee_id += 1

    return employee


def get_all_employees():
    return employees


def get_employee_by_id(employee_id: int):
    if employee_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Employee ID must be greater than 0"
        )

    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


def update_employee(employee_id: int, employee_data: EmployeeUpdate):
    if employee_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Employee ID must be greater than 0"
        )

    employee = None

    for item in employees:
        if item["id"] == employee_id:
            employee = item
            break

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    # Check duplicate email
    for item in employees:
        if (
            item["email"].lower() == employee_data.email.lower()
            and item["id"] != employee_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    employee["name"] = employee_data.name
    employee["email"] = employee_data.email
    employee["department"] = employee_data.department
    employee["primary_skill"] = employee_data.primary_skill
    employee["location"] = employee_data.location
    employee["work_mode"] = employee_data.work_mode
    employee["is_active"] = employee_data.is_active

    return employee


def delete_employee(employee_id: int):
    if employee_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Employee ID must be greater than 0"
        )

    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)

            return {
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )
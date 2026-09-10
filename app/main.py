from fastapi import FastAPI

from .schemas import EmployeeCreate, EmployeeResponse, EmployeeUpdate
from .services import (
    create_employee,
    delete_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
)


app = FastAPI(
    title="Employee Management API",
    description="Beginner FastAPI project for managing employee records",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Employee Management API is running"
    }


@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=201
)
def add_employee(employee: EmployeeCreate):
    return create_employee(employee)


@app.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def list_employees():
    return get_all_employees()


@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(employee_id: int):
    return get_employee_by_id(employee_id)


@app.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee_details(
    employee_id: int,
    employee: EmployeeUpdate
):
    return update_employee(employee_id, employee)


@app.delete("/employees/{employee_id}")
def remove_employee(employee_id: int):
    return delete_employee(employee_id)
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    department: str = Field(..., min_length=1)
    primary_skill: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    work_mode: Literal["WFH", "WFO"]


class EmployeeUpdate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    department: str = Field(..., min_length=1)
    primary_skill: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    work_mode: Literal["WFH", "WFO"]
    is_active: bool


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    primary_skill: str
    location: str
    work_mode: Literal["WFH", "WFO"]
    is_active: bool
    created_at: datetime
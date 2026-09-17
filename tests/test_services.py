"""Service-level verification using SQLite without requiring a MySQL server."""

import os
import unittest

os.environ["DATABASE_URL"] = "sqlite+pysqlite:///:memory:"

from fastapi import HTTPException
from pydantic import ValidationError

from app.database import Base, SessionLocal, engine
from app.schemas import EmployeeCreate, EmployeeUpdate
from app.services import (
    create_employee,
    delete_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
)


class EmployeeServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        Base.metadata.create_all(engine)
        self.db = SessionLocal()
        self.payload = {
            "name": "Aarav Mehta",
            "email": "aarav.mehta@example.com",
            "department": "Engineering",
            "primary_skill": "Python",
            "location": "Pune",
            "work_mode": "WFH",
        }

    def tearDown(self) -> None:
        self.db.close()
        Base.metadata.drop_all(engine)

    def test_crud_duplicate_check_and_timestamp_preservation(self) -> None:
        employee = create_employee(self.db, EmployeeCreate(**self.payload))
        self.assertEqual(employee.id, 1)
        self.assertTrue(employee.is_active)
        self.assertEqual(employee.email, "aarav.mehta@example.com")
        created_at = employee.created_at

        self.assertEqual(len(get_all_employees(self.db)), 1)
        self.assertEqual(get_employee_by_id(self.db, employee.id).id, employee.id)

        with self.assertRaises(HTTPException) as duplicate_error:
            create_employee(
                self.db,
                EmployeeCreate(**{**self.payload, "email": "AARAV.MEHTA@EXAMPLE.COM"}),
            )
        self.assertEqual(duplicate_error.exception.status_code, 409)

        updated = update_employee(
            self.db,
            employee.id,
            EmployeeUpdate(**{**self.payload, "name": "Aarav Kumar", "is_active": False}),
        )
        self.assertFalse(updated.is_active)
        self.assertEqual(updated.created_at, created_at)

        delete_employee(self.db, employee.id)
        self.assertEqual(get_all_employees(self.db), [])

        with self.assertRaises(HTTPException) as missing_error:
            get_employee_by_id(self.db, employee.id)
        self.assertEqual(missing_error.exception.status_code, 404)

    def test_blank_required_text_is_rejected(self) -> None:
        with self.assertRaises(ValidationError):
            EmployeeCreate(**{**self.payload, "name": "   "})


if __name__ == "__main__":
    unittest.main()
